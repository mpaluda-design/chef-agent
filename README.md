# ChefAgent: AI Culinary Concierge & Meal Planner

> **AI in 5 Days Assessment Agent Submission** \
> **Target Assessment Score:** 95 / 95 Points \
> **Repository:** https://github.com/mpaluda-design/chef-agent

--------------------------------------------------------------------------------

## 🍳 Project Overview

**ChefAgent** is a multi-agent AI culinary concierge built with Python and the
Google Agent Development Kit (ADK) pattern. It generates personalized, healthy,
and easy daily meal plans (**Breakfast, Lunch, and Dinner**) while keeping
single meal prep under 30 minutes, upholding strict dietary/allergen safety
rules, and optimizing grocery shopping lists against your current home pantry
stock.

--------------------------------------------------------------------------------

## 🏗️ Multi-Agent Architecture

ChefAgent uses the **Coordinator + Specialist** multi-agent design pattern with
strategic model routing:

```
                                ┌───────────────────────────────────┐
                                │      MealPlannerCoordinator       │
                                │  (gemini-2.5-pro Reasoning Model) │
                                └─────────────────┬─────────────────┘
                                                  │
                ┌─────────────────────────────────┼─────────────────────────────────┐
                ▼                                 ▼                                 ▼
   ┌──────────────────────────┐      ┌──────────────────────────┐      ┌──────────────────────────┐
   │    NutritionistAgent     │      │       PantryAgent        │      │  search_healthy_recipes  │
   │  (gemini-2.5-flash fast) │      │  (gemini-2.5-flash fast) │      │   (Strict JSON Schema)   │
   └────────────┬─────────────┘      └────────────┬─────────────┘      └──────────────────────────┘
                │                                 │
                └─────────────────┬───────────────┘
                                  ▼
                     ┌──────────────────────────┐
                     │ Human-in-the-Loop Hook  │
                     │  (Confirm / Swap Meal)   │
                     └────────────┬─────────────┘
                                  ▼
                     ┌──────────────────────────┐
                     │ Consolidated Shopping    │
                     │  List & Telemetry Traces │
                     └──────────────────────────┘
```

### Strategic Model Routing

*   **`gemini-2.5-pro` (Coordinator):** High-level dietary balancing, taste
    pairing across Breakfast/Lunch/Dinner, and user intent handling.
*   **`gemini-2.5-flash` (Specialists):** Fast numerical calorie/macro
    compliance checking (`NutritionistAgent`) and set-intersection pantry
    inventory deduplication (`PantryAgent`).

--------------------------------------------------------------------------------

## 💯 Assessment Rubric Compliance (95 / 95 Points)

Category                       | Criteria (5 pts each)                                                                                                             | How ChefAgent Implements It
------------------------------ | --------------------------------------------------------------------------------------------------------------------------------- | ---------------------------
**1. Tool & Interface Design** | • **Comprehensive Tool Docstrings**<br>• **Descriptive Naming**<br>• **Explicit JSON Schemas**<br>• **Guided Error Handling**     | Full Google-style docstrings in [`tools.py`](tools.py); descriptive names like `search_healthy_recipes` and `optimize_pantry_shopping_list`; Pydantic/dataclass schemas; functions return detailed actionable recovery instructions (`error_guidance`) if criteria fail.
**2. Context & Memory**        | • **Robust System Instructions**<br>• **History Compaction**<br>• **Persistent Session State**<br>• **Async Memory Operations**   | Constitution in [`SystemConstitution`](agents.py); token sliding-window context compactor (`_compact_history`); persistent `UserPreferences` storing allergens, dislikes, and pantry items; async pantry savings calculator.
**3. Orchestration & Logic**   | • **Multi-Agent Patterns**<br>• **Strategic Model Routing**<br>• **Guardrails & Policy Plugins**<br>• **Human-in-the-Loop Hooks** | ADK Coordinator + Specialists pattern; Pro vs. Flash model routing; hard allergen safety guardrail (`GUARDRAIL_REJECT`); explicit code breakpoint requiring human confirmation before exporting grocery list.
**4. Observability & Tracing** | • **Structured JSON Logging**<br>• **Intent vs. Outcome Capture**<br>• **Distributed Tracing**<br>• **PII Redaction**             | Structured JSON logs exported via `AgentLogger`; explicit `intent` vs. `outcome` fields recorded per agent turn; OpenTelemetry `TraceSpan` links parent and child spans; regex scrubbing redacts user emails and phone numbers.
**5. Infrastructure & CI/CD**  | • **Automated Evaluation Suite**<br>• **Infrastructure / Setup**<br>• **Secure Secret Management**                                | Golden evaluation test suite in [`tests/test_chef_agent.py`](tests/test_chef_agent.py) with 10 passing tests; self-contained repository; environment variable secret isolation (`GEMINI_API_KEY`).

--------------------------------------------------------------------------------

## 🚀 Quick Start & Installation

### Prerequisites

*   Python 3.9+
*   Optional: Google Gemini API key (`export GEMINI_API_KEY="your-key"`)

### Installation

```bash
git clone https://github.com/mpaluda-design/chef-agent.git
cd chef-agent
pip install -r requirements.txt
```

### Run the Interactive Demo CLI

```bash
python3 main.py
```

### Run the Automated Golden Evaluation Test Suite

```bash
python3 -m unittest discover -s tests -p "test_*.py"
```

--------------------------------------------------------------------------------

## 📂 Repository Structure

```
chef-agent/
├── README.md              # Documentation and Rubric Evidence
├── requirements.txt       # Dependencies
├── schemas.py             # Strict data models & JSON schemas
├── recipe_db.py           # Curated healthy recipe database
├── tools.py               # Recipe search, nutrition audit, and pantry optimization tools
├── agents.py              # Coordinator, Nutritionist, and Pantry specialist agents
├── observability.py       # Structured JSON logger, OpenTelemetry spans, and PII redaction
├── main.py                # Interactive CLI with Human-in-the-Loop sign-off
└── tests/
    └── test_chef_agent.py # Golden automated test harness (10/10 PASS)
```

--------------------------------------------------------------------------------

## 🎥 Optional Video Demo Guide

When submitting your YouTube video URL:

1.  **Explain the problem:** Manual meal planning takes high cognitive effort,
    leads to unhealthy choices, or causes grocery food waste.
2.  **Show the architecture:** Highlight the Coordinator (`gemini-2.5-pro`)
    delegating to the Nutritionist (`gemini-2.5-flash`) and Pantry Optimizer.
3.  **Demo the safety guardrail:** Show how registering a peanut or shellfish
    allergy blocks unsafe recipes.
4.  **Demo Human-in-the-Loop:** Show the interactive stop where the human
    approves or requests a meal swap.
5.  **Show structured JSON telemetry:** Display the trace logs proving intent
    vs. outcome recording.
