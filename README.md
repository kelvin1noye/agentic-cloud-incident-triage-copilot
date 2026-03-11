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

## Agent Workflow

Incident Input → Intake Agent → Retrieval Agent → Hypothesis Agent → Action Agent → Review Agent

### 1. Intake Agent
Parses the incident and identifies likely severity, service impact, and incident category.

### 2. Retrieval Agent
Pulls relevant operational context from local runbooks.

### 3. Hypothesis Agent
Generates likely root-cause hypotheses and identifies what evidence would confirm or weaken each one.

### 4. Action Planning Agent
Produces recommended triage steps, rollback considerations, and escalation guidance.

### 5. Review Agent
Reviews the full draft for clarity, duplication, and unsafe or overly speculative guidance before producing the final incident brief.

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
Production API latency spike following recent deployment affecting claims submission service.

Likely Root Causes
1. Recent deployment introduced inefficient database queries.
2. Database connection pool exhaustion.
3. Upstream dependency latency causing cascading slowdowns.

Immediate Triage Steps
1. Review deployment logs and release notes.
2. Check database connection pool metrics.
3. Compare latency metrics before and after deployment.
4. Consider rollback if deployment correlates with the issue.

Escalation Guidance
Notify application owner and incident commander if latency persists beyond SLA thresholds.

Assumptions and Confidence
Moderate confidence based on runbook guidance and incident pattern matching.

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


