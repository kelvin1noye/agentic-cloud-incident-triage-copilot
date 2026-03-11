# agentic-cloud-incident-triage-copilot

Agentic Cloud Incident Triage Copilot is a lightweight **agentic AI** project that demonstrates how specialized AI agents can support cloud operations and incident-response workflows.

## Overview

This project simulates an AI-assisted incident triage workflow for cloud environments. A user submits a short incident description, and the system uses a sequence of specialized agents to:

- analyze the incident
- retrieve relevant runbook context
- generate likely root-cause hypotheses
- recommend immediate triage actions
- review and refine the final incident brief

## Why I Built It

I built this project to demonstrate practical **agent-based workflow design** for cloud operations and DevSecOps environments. The goal was to create a simple but credible example of how AI agents can support incident-response decision making through structured task handoffs.


---

# Agent Roles

## Intake Agent
Analyzes the incoming incident description and extracts:

- incident summary
- affected service
- probable incident category
- estimated severity
- potential business impact

---

## Retrieval Agent
Searches the runbook knowledge base and retrieves relevant operational guidance related to the incident.

---

## Hypothesis Agent
Generates several **likely root-cause hypotheses** and identifies:

- why each hypothesis is plausible
- what evidence would confirm it
- what evidence would weaken it

---

## Action Planning Agent
Creates a recommended triage plan including:

- priority diagnostic checks
- rollback considerations
- escalation triggers
- operational risks

---

## Review Agent
Validates the draft response and improves:

- clarity
- structure
- operational safety
- removal of speculative or redundant guidance

---

## Confidence & Escalation Agent
Evaluates the final incident brief and determines:

- overall confidence level
- whether escalation to human responders is recommended
- risks associated with incorrect remediation

This agent simulates **AI governance patterns used in enterprise AI systems**.

---

# Example Use Case

### Input


## Example Use Case

**Input**

Production API latency spike affecting claims submission service after deployment

**Output**

A structured incident brief with:
- incident summary
- likely root causes
- immediate triage steps
- escalation guidance
- assumptions and confidence notes

## Tech Stack

- Python
- OpenAI API
- Markdown-based local runbooks
- Multi-agent workflow design


## Architecture

The system uses a multi-agent workflow where each agent performs a specific operational task before passing structured output to the next stage.

Incident Input → Intake Agent → Retrieval Agent → Hypothesis Agent → Action Agent → Review Agent → Final Incident Brief


## Example Output

Incident Summary
Production API latency spike following recent deployment.

Likely Root Causes
1. Inefficient database queries introduced in deployment
2. Database connection pool exhaustion
3. Upstream dependency slowdown

Immediate Triage Steps
1. Review deployment logs
2. Check database connection metrics
3. Compare pre/post deployment latency
4. Consider rollback

Escalation Guidance
Notify application owner if latency exceeds SLA thresholds.

Assumptions and Confidence
Moderate confidence based on runbook guidance.

---

Confidence Level: Medium

Escalation Recommendation:
Notify incident commander if customer impact continues beyond 15 minutes.

Risk Notes:
Automated triage recommendations may not detect external dependency failures.

## Key Concepts Demonstrated

- Agent-based workflow orchestration
- Retrieval-augmented reasoning using operational runbooks
- Multi-agent task specialization
- Structured AI-assisted incident triage
- Practical AI use cases for cloud operations and DevSecOps environments

- ## Demo

Example terminal session:

$ python app.py

Enter incident description:
Production API latency spike affecting claims service

--- Final Incident Brief ---
[generated response]

## Project Structure

```text
cloud-incident-triage-copilot/
├── app.py
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
├── data/
│   └── runbooks/
│       ├── api_latency.md
│       ├── database_connectivity.md
│       └── deployment_rollback.md
└── agents/
    ├── __init__.py
    ├── prompts.py
    └── workflow.py


