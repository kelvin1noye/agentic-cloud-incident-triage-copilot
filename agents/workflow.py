import os
from typing import Dict

from dotenv import load_dotenv
from openai import OpenAI

from agents.prompts import (
    ACTION_PROMPT,
    HYPOTHESIS_PROMPT,
    INTAKE_PROMPT,
    RETRIEVAL_PROMPT,
    REVIEW_PROMPT,
)

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")

if not OPENAI_API_KEY:
    raise ValueError(
        "OPENAI_API_KEY is not set. Create a .env file based on .env.example."
    )

client = OpenAI(api_key=OPENAI_API_KEY)


IncidentState = Dict[str, str]


def call_llm(system_prompt: str, user_prompt: str) -> str:
    """
    Call the OpenAI Responses API and return the model output as text.
    """
    response = client.responses.create(
        model=OPENAI_MODEL,
        input=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
    )
    return response.output_text.strip()


def load_runbooks(runbook_dir: str = "data/runbooks") -> str:
    """
    Load all markdown runbooks into a single text blob.
    """
    if not os.path.isdir(runbook_dir):
        raise FileNotFoundError(
            f"Runbook directory '{runbook_dir}' was not found."
        )

    docs = []
    for filename in sorted(os.listdir(runbook_dir)):
        if filename.endswith(".md"):
            path = os.path.join(runbook_dir, filename)
            with open(path, "r", encoding="utf-8") as file:
                docs.append(f"\n## FILE: {filename}\n{file.read()}")

    if not docs:
        raise ValueError(f"No markdown runbooks found in '{runbook_dir}'.")

    return "\n".join(docs)


def intake_agent(state: IncidentState) -> IncidentState:
    prompt = f"Incident report:\n{state['incident_text']}"
    state["intake_output"] = call_llm(INTAKE_PROMPT, prompt)
    return state


def retrieval_agent(state: IncidentState) -> IncidentState:
    runbooks = load_runbooks()
    state["retrieved_context"] = runbooks

    prompt = f"""Incident analysis:
{state['intake_output']}

Runbook content:
{runbooks}
"""
    state["retrieval_output"] = call_llm(RETRIEVAL_PROMPT, prompt)
    return state


def hypothesis_agent(state: IncidentState) -> IncidentState:
    prompt = f"""Incident analysis:
{state['intake_output']}

Retrieved guidance:
{state['retrieval_output']}
"""
    state["hypothesis_output"] = call_llm(HYPOTHESIS_PROMPT, prompt)
    return state


def action_agent(state: IncidentState) -> IncidentState:
    prompt = f"""Incident analysis:
{state['intake_output']}

Retrieved guidance:
{state['retrieval_output']}

Root-cause hypotheses:
{state['hypothesis_output']}
"""
    state["action_output"] = call_llm(ACTION_PROMPT, prompt)
    return state


def review_agent(state: IncidentState) -> IncidentState:
    draft = f"""Incident analysis:
{state['intake_output']}

Retrieved guidance:
{state['retrieval_output']}

Root-cause hypotheses:
{state['hypothesis_output']}

Draft action plan:
{state['action_output']}
"""
    state["final_output"] = call_llm(REVIEW_PROMPT, draft)
    return state


def run_workflow(incident_text: str) -> IncidentState:
    """
    Run the full multi-agent incident triage workflow.
    """
    state: IncidentState = {"incident_text": incident_text}
    state = intake_agent(state)
    state = retrieval_agent(state)
    state = hypothesis_agent(state)
    state = action_agent(state)
    state = review_agent(state)
    return state

from agents.prompts import CONFIDENCE_PROMPT

def confidence_agent(state: IncidentState) -> IncidentState:
    prompt = f"""
Evaluate the following incident response brief:

{state['final_output']}
"""
    output = call_llm(CONFIDENCE_PROMPT, prompt)

    state["final_output"] = state["final_output"] + "\n\n---\n\n" + output
    return state
