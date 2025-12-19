# Video 1 – Introduction to LangGraph & Agentic AI Playlist

## What is this playlist about?

* A new YouTube playlist focused on **Agentic AI using LangGraph**.
* The creator received many requests to explain LangGraph, so he decided to teach it in a structured way.
* He spent **3–4 months researching and preparing** the curriculum.

---

## Why this Playlist?

There are **3 main reasons**:

### **1️⃣ Timing**

* Right now is the perfect time to learn **Agentic AI**.
* Everywhere—YouTube, Twitter, Instagram—you will see the term **“Agentic AI”**.
* Industry leaders believe Agentic AI will be the **next big thing** in computer science.
* Generative AI tools like **ChatGPT** are mature enough now, enabling powerful AI agents in the coming years.

### **2️⃣ High Demand**

* Viewers repeatedly asked for a **LangGraph playlist**.
* There is huge interest in this topic across the industry.

### **3️⃣ Progressive Learning**

The channel has already covered:

* **Machine Learning**
* **Deep Learning**
* **LangChain and Generative AI**

Now students are ready to learn **LangGraph and Agentic AI**.

---

## Vision Behind This Playlist

The creator has **three goals** for learners:

### ⭐ Goal 1: Easy Learning

* Even beginners should be able to build **Agentic AI applications**.

### ⭐ Goal 2: Strong Fundamentals

* Gain a **strong command** over LangGraph concepts.

### ⭐ Goal 3: Conceptual Understanding

* Even if LangGraph is replaced by another tool, you should be able to learn the new one easily.

---

## Curriculum (Tentative Modules)

> *Note: May change as Agentic AI is evolving fast.*

### **Module 1 – Foundations of Agentic AI**

* What is Agentic AI?
* Difference between:

  * Agentic AI vs AI Agent
  * Agentic AI vs Generative AI
  * Traditional RAG vs Agentic RAG
* Frameworks for building agents

### **Module 2 – LangGraph Fundamentals**

* What is a LangGraph?
* Key concepts:

  * Graph
  * State
  * Nodes
  * Edges
  * Conditional edges
  * Loops
* Build **basic AI workflows** using LangGraph

### **Module 3 – Advanced LangGraph Concepts**

* Persistence
* Memory
* Human-in-the-loop
* Breakpoints
* Checkpoints
* Time travel
* Build **industry-level agents**

### **Module 4 – Building AI Agents**

Understand design patterns such as:

* ReAct
* Reflection
* Self-Ask with Search
* Planning
* Multi-agent systems

### **Module 5 – Agentic RAG**

* Combine **Agents + RAG**
* Architectures:

  * C-RAG
  * Self-RAG
* Build advanced RAG systems using agents

### **Module 6 – Production & Deployment**

* Build a **real project**
* Add:

  * UI
  * Debugging tools
  * Observability
  * LangSmith integration
* Deploy and showcase in **resume/interviews**

---

## Prerequisites

To follow the playlist smoothly, you should know:

### ✔ Python (Intermediate Level)

* OOP concepts
* Typing module
* Pydantic
* Async IO

### ✔ Basics of LLMs

### ✔ LangChain

* LangGraph is built on top of LangChain
* The creator recommends watching the **LangChain playlist first**

# Generative AI vs Agentic AI — Video 2

## 1. Introduction

This playlist teaches Agentic AI using LangGraph. Before learning Agentic AI, it’s important to understand how it differs from Generative AI.

## 2. What is Generative AI?

Generative AI (GenAI) refers to AI models that can create new content such as:

* Text (ChatGPT, Gemini, Claude)
* Images (DALL·E, Midjourney)
* Code (Code Llama)
* Speech (ElevenLabs)
* Videos (Sora, Runway ML)

### Simple Definition

Generative AI models learn from existing data and create new data that looks like it was created by humans.

### How GenAI Works

* It does not focus on input-output relationships like traditional AI.
* It learns the pattern and distribution of data.
* It generates new samples from that learned distribution.

### Example

Give GenAI thousands of cat images → it learns what a cat looks like → generates a new cat image.

## 3. Traditional AI vs Generative AI

| Feature     | Traditional AI                         | Generative AI             |
| ----------- | -------------------------------------- | ------------------------- |
| Purpose     | Predict or classify                    | Create new content        |
| Learning    | Finds relations between input & output | Learns data distribution  |
| Examples    | Spam detection, cancer detection       | ChatGPT, Midjourney       |
| Output Type | Label or number                        | Text, Image, Audio, Video |

## 4. Applications of Generative AI

* Creative Writing: blogs, email drafting
* Software Development: code generation, debugging
* Customer Support: chatbots
* Education: learning assistance
* Design: thumbnails, infographics, AI-generated ads

## 5. Scenario — HR Hiring Workflow

**Goal:** Hire a Backend Engineer

### Hiring Steps

1. Write Job Description (JD)
2. Post job on platforms like LinkedIn
3. Shortlist candidates
4. Schedule interviews
5. Conduct interviews
6. Send offer letter
7. Onboard the candidate

## 6. Four Levels of AI Solutions

### 1️⃣ Simple Generative AI Chatbot

**Capabilities:** Helps draft JD, emails, interview questions
**Problems:**

* Reactive (waits for input)
* No memory
* Generic advice
* Cannot take actions

### 2️⃣ RAG-based Chatbot (Retrieval Augmented Generation)

**Improvement:** Connect to company documents like:

* Old JDs, hiring strategies, onboarding policies
  **Benefits:**
* Company-specific answers
  **Limitation:** Still reactive, cannot act independently

### 3️⃣ Tool-Augmented Chatbot

**Improvements:** Connect with tools such as:

* LinkedIn API, resume parser, email sender, calendar tools
  **Benefits:**
* Can take real actions (post jobs, send emails, schedule interviews)
  **Limitation:** Still not proactive

### 4️⃣ Agentic AI (Final Stage)

**Capabilities:**

* Understands the goal
* Plans steps automatically
* Executes autonomously
* Has memory & context
* Adapts to changes
* Makes decisions

**Example Behavior:**

* Notices low applications → updates JD + boosts LinkedIn post
* Tracks onboarding and notifies only when approval is needed

## 7. Key Differences — Generative AI vs Agentic AI

| Feature            | Generative AI  | Agentic AI                     |
| ------------------ | -------------- | ------------------------------ |
| Goal               | Create content | Achieve a goal end-to-end      |
| Nature             | Reactive       | Proactive & autonomous         |
| Needs user prompt? | Yes            | Only once                      |
| Uses tools?        | Optional       | Mandatory                      |
| Memory             | Not always     | Yes                            |
| Planning           | No             | Yes                            |
| Adaptability       | No             | Yes                            |
| Components         | Only LLM       | LLM + Memory + Tools + Planner |

## 8. One-Line Understanding

**Generative AI = capability** → creates content
**Agentic AI = behavior** → achieves goals autonomously using GenAI + tools + memory + planning

## 9. Conclusion

Generative AI started the revolution, but Agentic AI is the next big leap where AI becomes:

* Autonomous
* Context-aware
* Action-driven
* Goal-oriented

Agentic AI doesn't just answer — it acts, plans, and completes tasks like a real digital employee.


# Agentic AI – Video 3

## What is Agentic AI?

Agentic AI is a type of AI that:

* Takes a goal from a user
* Plans how to achieve it
* Executes tasks automatically
* Adapts when situations change
* Asks for help only when needed

➡️ It does things proactively, unlike normal chatbots which are only reactive.

---

### Example Difference

| Generative AI (ChatGPT)         | Agentic AI                                        |
| ------------------------------- | ------------------------------------------------- |
| Answers only what you ask       | Takes your goal and completes the entire workflow |
| Reactive                        | Proactive                                         |
| No planning                     | Makes plans and executes                          |
| Needs instructions step-by-step | Works independently                               |

---

## Example

**Goal:** Hire a Backend Engineer

Agentic AI will:

* Understand the goal
* Create a job description (JD)
* Post on job portals
* Monitor applicants
* Modify strategy if no applications
* Parse resumes, shortlist candidates
* Schedule interviews using calendar
* Send offer letters
* Onboard selected candidate

➡️ You gave one goal → AI handled everything end-to-end.

---

## Key Characteristics of Agentic AI (6 Traits)

### 1. Autonomy

* Works independently without step-by-step human commands
* Takes actions on its own
* Shows autonomy in:

  * Execution
  * Decision-making
  * Tool selection

**Control Mechanisms:**

* Permission limits
* Human approval checkpoints
* Guardrails (policies)

### 2. Goal-Oriented

* Always works toward a defined goal
* Stores goals in memory
* Handles:

  * Plain goals → "Hire a backend engineer"
  * Goals with constraints → "Hire remotely, 2–4 years experience"
* Goals can be updated midway

### 3. Planning

Agentic AI works in two phases:

```
PLAN → EXECUTE → REPLAN (if something fails) → EXECUTE
```

Planning steps:

* Generate multiple plans
* Evaluate plans (cost, risk, tools, constraints)
* Select the best plan

### 4. Reasoning

Used in planning and execution to:

* Understand goal
* Break tasks into steps
* Decide tools to use
* Handle errors
* Decide when to involve human

**Reasoning = thinking logic of the agent**

### 5. Adaptability

Changes strategy if:

* Something fails (e.g., API is down)
* External feedback changes (low applicants)
* Goal changes midway

➡️ Agent modifies actions without restarting.

### 6. Context Awareness

Agent remembers:

* The main goal
* Task progress
* Past chats
* Tool responses
* User preferences
* Guardrails

**Memory Types:**

* Short-term memory → current session data
* Long-term memory → policies, user preferences, history

➡️ Without context, an agent cannot operate across multiple days or steps.

---

## Core Components of Agentic AI (5 Components)

| Component        | Function                                                            |
| ---------------- | ------------------------------------------------------------------- |
| **Brain (LLM)**  | Understands goals, plans, reasons, selects tools, communicates      |
| **Orchestrator** | Executes steps in correct order, handles loops, conditions, retries |
| **Tools**        | External actions: APIs, email, database, search, RAG                |
| **Memory**       | Stores short-term and long-term information                         |
| **Supervisor**   | Human approval system, applies rules, handles escalations           |

---

## Summary

```
Agentic AI = Goal + Planning + Reasoning + Autonomy + Tools + Memory + Supervisor
```

It behaves like a **digital employee** capable of executing full workflows, not just answering questions.

---

## How to Identify Agentic AI

Ask these 6 questions:

| Question                  | If YES → Agentic |
| ------------------------- | ---------------- |
| Is it autonomous?         | ✔️               |
| Is it goal-driven?        | ✔️               |
| Does it plan steps?       | ✔️               |
| Does it reason?           | ✔️               |
| Can it adapt?             | ✔️               |
| Does it remember context? | ✔️               |

➡️ If all are YES → It’s Agentic AI.

# Agentic AI using LangGraph 

## 1. video 4

* This is the **4rd video** in the *Agentic AI using LangGraph* playlist.
* Previous videos covered:

  * Difference between **Generative AI** and **Agentic AI**
  * What **Agentic AI** is, with a real example (Automated Hiring)
  * Characteristics, traits, and components of Agentic AI
* This video shifts focus to **practical development** of Agentic AI applications.

---

## 2. Why Frameworks Are Needed for Agentic AI

* Agentic AI applications are **complex**.
* You cannot write everything **from scratch in Python**.
* Many frameworks exist, such as:

  * CrewAI
  * Microsoft Autogen
  * Others
* This playlist uses **LangGraph**:

  * Built by the **LangChain team**
  * One of the **top frameworks** for Agentic AI

---

## 3. Goals of This Video

By the end of this video, you will understand:

* Why **LangGraph** exists
* What **LangGraph** is (technical overview)
* **LangChain vs LangGraph**
* When to use **LangChain** and when to use **LangGraph**

---

## 4. Prerequisites

You should already know:

* What **LangChain** is
* Basic LangChain components
* How simple LangChain code works

👉 If not, first watch:

* LangChain Introduction
* LangChain Components

---

## 5. Quick Recap: What is LangChain?

### Definition

> LangChain is an open-source library that simplifies building LLM-based applications.

### Why LangChain Exists

LLM-based applications require many parts:

* Prompts
* Models
* Retrieval
* Memory
* Tools

LangChain **simplifies and connects** all these parts.

---

## 6. Core LangChain Building Blocks

### 1. Models

* Unified interface for:

  * OpenAI
  * Anthropic (Claude)
  * HuggingFace
  * Ollama
* Easy to switch models **without rewriting code**

### 2. Prompts

* Helps design and manage prompts
* Supports prompt templates and reuse

### 3. Retrievers

* Fetch relevant data from:

  * Vector databases
  * Knowledge bases
* Used for **RAG (Retrieval-Augmented Generation)** applications

### 4. Chains (Most Important)

* Connect components in a **linear sequence**
* Output of one step becomes input of the next step
* Best for:

  * Chatbots
  * Summarizers
  * Simple multi-step workflows

---

## 7. What Can You Build with LangChain?

* Chatbots
* Text summarizers
* Multi-step report generators
* RAG-based systems
* Basic agent-like workflows using tools

⚠️ **Limitation**:

* Works best for **linear workflows**
* Struggles with **complex, non-linear logic**

---

## 8. Workflow vs Agent (Very Important Concept)

### Workflow

* Steps are predefined by the developer
* Executes in the same order every time
* Static

### Agent

* LLM decides:

  * Steps
  * Order
  * Tool usage
* Dynamic and autonomous

👉 The automated hiring example shown is a **workflow**, not a full agent.

---

## 9. Automated Hiring Workflow (Overview)

Steps include:

* Receive hiring request
* Create job description (JD)
* Human approval
* Post job
* Wait & monitor applications
* Modify JD if needed (loop)
* Shortlist candidates
* Schedule interviews
* Conduct interviews
* Send offers
* Handle acceptance / rejection
* Onboarding

This workflow:

* Has loops
* Has conditions
* Has wait times
* Runs for **days or weeks**

---

## 10. Challenge 1: Control Flow Complexity

### Problem with LangChain

* LangChain chains are **linear**
* This workflow is **non-linear**:

  * Conditional branches
  * Loops
  * Jumps

### Result

* Requires a lot of custom **Python glue code**
* Glue code is:

  * Hard to maintain
  * Hard to debug
  * Error-prone

---

## 11. How LangGraph Solves Control Flow

### Key Idea

* Represent the workflow as a **graph**

  * Nodes = tasks
  * Edges = control flow

### Benefits

* Native support for:

  * Conditions
  * Loops
  * Jumps
* No glue code
* Cleaner and more maintainable logic

---

## 12. Challenge 2: State Handling

### What is State?

All important data during workflow execution, such as:

* Job description
* Approval status
* Application count
* Interview results
* Offer status

State **changes over time**.

### LangChain Problem

* LangChain is **stateless**
* Memory only stores conversation text
* State must be manually managed using dictionaries

---

## 13. LangGraph State Management

* LangGraph is **stateful**
* You define a **state object**
* Every node:

  * Can read state
  * Can update state
* State flows automatically across nodes

👉 LangChain = Stateless
👉 LangGraph = Stateful

---

## 14. Challenge 3: Event-Driven Execution

### Two Types of Execution

* **Sequential**: Runs start → end without stopping
* **Event-driven**:

  * Pauses
  * Waits for an external event
  * Resumes later

### Hiring Workflow Needs Event-Driven Execution

* Wait 7 days after job posting
* Wait 48 hours after JD modification
* Wait for candidate response
* Wait for human approvals

### LangChain Limitation

* No pause / resume support
* Workflow must be manually broken

### LangGraph Advantage

* Built-in pause & resume
* Uses checkpoints
* Can resume exactly where it stopped

---

## 15. Challenge 4: Fault Tolerance

### Problem

Long-running workflows can fail due to:

* API failure
* Server crash
* Network issues

### LangChain

* If it fails → start from the beginning

### LangGraph

* Supports:

  * Retry logic (small failures)
  * Recovery from last checkpoint (big failures)

---

## 16. Challenge 5: Human in the Loop

### Meaning

* Workflow pauses for **human decision**
* Examples:

  * JD approval
  * Offer approval

### LangChain

* Works only for short waits
* Not suitable for long approvals (hours or days)

### LangGraph

* First-class support
* Can pause indefinitely
* Resume after human input

---

## 17. Feature: Nested Workflows (Subgraphs)

### Concept

* A node can itself be a **graph**
* Enables:

  * Modular design
  * Reusability
  * Multi-agent systems

### Example

* “Conduct Interview” can be a full workflow:

  * Question generation
  * Multiple rounds
  * Evaluation

---

## 18. Observability (Monitoring & Debugging)

### Why Important

* Debug errors
* Audit decisions
* Understand agent behavior

### LangChain + LangSmith

* Tracks LangChain code
* ❌ Cannot track glue code

### LangGraph + LangSmith

* Full visibility
* Tracks:

  * Node execution
  * State changes
  * Human inputs
  * Decision paths

---

## 19. Final Summary

### What is LangGraph?

> LangGraph is an orchestration framework to build **stateful, multi-step, event-driven workflows** using LLMs.

Think of LangGraph as:

> **A flowchart engine for LLMs**

---

## 20. When to Use What?

### Use LangChain when:

* Simple linear flows
* Chatbots
* Summarizers
* Basic RAG

### Use LangGraph when:

* Complex workflows
* Conditions & loops
* Human-in-the-loop
* Event-driven execution
* Long-running systems
* Multi-agent systems

---

## 21. Important Note

* LangGraph does **not** replace LangChain
* LangGraph is built **on top of LangChain**
* You still use from LangChain:

  * Prompts
  * Models
  * Retrievers
  * Tools

👉 **LangChain = Components**
👉 **LangGraph = Orchestration**

# 📘 Agentic AI using LangGraph – Simple English Notes (Video 5)

---

## 1. About This Video

* This is the **4th video** in the *Agentic AI using LangGraph* playlist.
* The previous video covered **LangChain vs LangGraph** comparison.
* This video is **fully dedicated to LangGraph core concepts**.

### 🎯 Goal

* Understand concepts first → **coding becomes easy** in the next videos.

---

## 2. What is LangGraph? (Quick Revision)

### Definition

**LangGraph is an orchestration framework for LLM workflows.**

### In Simple Words

* You give an **LLM workflow** to LangGraph.
* LangGraph converts that workflow into a **graph**.
* LangGraph then **executes the workflow automatically**.

---

## 3. Why “Graph”?

### Graph Structure

* **Nodes** → Tasks
* **Edges** → Execution flow (what runs next)

### Example Tasks (Nodes)

* Call an LLM
* Call a tool
* Make a decision
* Store memory

### What Edges Tell

* After this task → **which task should run next**

---

## 4. Key Features of LangGraph

LangGraph supports:

* ✅ Sequential execution
* ✅ Parallel execution
* ✅ Branching (if / else)
* ✅ Loops (retry, iteration)
* ✅ Memory (conversation / state)
* ✅ Resume from failure

👉 Because of this, LangGraph is **ideal for Agentic and Production-grade AI systems**.

---

## 5. What is an LLM Workflow?

### Workflow (General)

A workflow is:

> A series of tasks executed in order to achieve a goal.

**Example – Hiring Workflow**

* Create JD
* Post job
* Shortlist candidates
* Interview
* Onboard

### LLM Workflow

An **LLM workflow** is a workflow where:

* Many steps depend on **LLMs**

**Examples**

* JD writing → LLM
* Resume shortlisting → LLM
* Interview Q&A → LLM

---

## 6. Common LLM Workflow Patterns

### 1️⃣ Prompt Chaining

**Idea:**
Break a complex task into smaller LLM calls.

**Example – Report Generation**

* LLM → Create outline
* LLM → Write detailed report from outline
* Add checks (word limit, quality)

✅ Easy to debug
✅ Easy to validate intermediate outputs

---

### 2️⃣ Routing

**Idea:**
One LLM decides **which expert should handle the task**.

**Example – Customer Support Bot**

* Refund query → Refund LLM
* Technical query → Tech LLM
* Sales query → Sales LLM

👉 One LLM acts as a **decision maker (router)**.

---

### 3️⃣ Parallelization

**Idea:**
Run multiple tasks **at the same time**, then merge results.

**Example – YouTube Content Moderation**

* Check community guidelines
* Check misinformation
* Check sexual content

All checks run **in parallel**, results are merged → final decision.

---

### 4️⃣ Orchestrator–Worker Pattern

**Idea:**

* Tasks are **not predefined**
* Orchestrator LLM decides tasks dynamically

**Example – Research Assistant**

* Scientific query → Google Scholar
* Political query → Google News
* Social topic → Blogs / Articles

👉 Orchestrator assigns work to workers **based on input**.

---

### 5️⃣ Evaluator–Optimizer

**Idea:**
Improve output through **iteration + feedback loop**.

**Two LLMs**

* Generator → Creates output
* Evaluator → Checks quality and gives feedback

**Examples**

* Blog writing
* Email drafting
* Story / poem writing

The process repeats until the evaluator is satisfied.

---

## 7. Graphs, Nodes & Edges (Most Important Concept)

### Node

* Represents **one task**
* Behind the scenes → **Python function**

### Edge

* Connects nodes
* Defines **execution order**

### Types of Edges

* Sequential
* Parallel
* Conditional (if / else)
* Looping

👉 **Nodes = What to do**
👉 **Edges = When to do**

---

## 8. Example: UPSC Essay Evaluation Workflow

### High-Level Flow

1. Generate essay topic
2. User writes essay
3. Evaluate essay:

   * Clarity
   * Depth
   * Language
4. Calculate score
5. If score ≥ threshold → Success
6. Else → Feedback + Retry loop

### Graph View

* Each step = Node
* Retry = Loop edge
* Pass / Fail = Conditional edge

---

## 9. What is State in LangGraph?

### Definition

**State = shared memory flowing through the graph**

### What State Contains

* User input
* Scores
* Intermediate results
* Final output

### Key Properties

* Shared by all nodes
* Mutable (can change)
* Evolves over time

### Technical Form

* Usually a **TypedDict (Python)**
* Sometimes a **Pydantic model**

---

## 10. How State Works Internally

1. State is passed to the first node
2. Node updates part of the state
3. Updated state goes to the next node
4. Process continues until the workflow ends

---

## 11. Reducers (Very Important)

### Problem

If multiple nodes update the same state key:

* Replace value?
* Add value?
* Merge value?

### Reducer Decides

**How updates are applied to state**

### Examples

* Replace → Overwrite old value
* Add → Append to list
* Merge → Combine results

### Why Reducers Matter

**Chatbot Example**

* Replace messages → Old chats lost ❌
* Append messages → Full conversation kept ✅

**UPSC Essay Example**

* Store all attempts
* Track improvement over time

---

## 12. LangGraph Execution Model (Behind the Scenes)

Inspired by **Google Pregel** (large-scale graph processing).

### Execution Steps

#### 1️⃣ Graph Definition

* Define nodes
* Define edges
* Define state

#### 2️⃣ Compile

* Validate graph structure
* Check orphan nodes
* Ensure logical correctness

#### 3️⃣ Invoke

* Pass initial state to the first node

---

### Message Passing

* State moves through edges
* Nodes update state partially

### Supersteps

* One superstep may contain:

  * One node execution
  * OR multiple parallel node executions

Used because **parallel nodes run together**.

### When Execution Stops

* No active nodes
* No messages flowing

---

## 13. Why This Matters

* You don’t manually call functions
* LangGraph automatically handles:

  * Execution order
  * Parallelism
  * State passing
  * Loops
  * Failures

---

## 14. Final Takeaways

* **LangGraph** = Graph-based LLM orchestration
* **Nodes** = Python functions
* **Edges** = Execution logic
* **State** = Shared, evolving memory
* **Reducers** = State update rules
* **Execution** = Automatic and scalable

👉 **Next Video:** First practical LangGraph workflow 🚀

# 📘 Agentic AI using LangGraph – Sequential Workflows (Simple Notes)

---

## 1. What this video is about

This video is the **first practical video** in the *Agentic AI using LangGraph* playlist.

### Before this video, we covered (Theory):

* Difference between **Generative AI vs Agentic AI**
* What **Agentic AI** is (deep conceptual understanding)
* Why **LangGraph** is needed when **LangChain** already exists
* Core concepts of **LangGraph**

👉 Now, theory is complete.
👉 From this video onwards, **hands-on coding starts**.

---

## 2. Goal of this video

This video has **two main goals**:

1. Teach you **basic LangGraph syntax** (your first LangGraph code)
2. Enable you to build **any simple sequential workflow** on your own

---

## 3. What is a Sequential Workflow?

A **Sequential Workflow** means:

* Tasks run **one after another**
* No branching
* No parallel paths

**Example:**

```
Task 1 → Task 2 → Task 3 → END
```

This video covers:

* Simple **non-LLM workflow**
* Simple **LLM workflow**
* **Prompt chaining** workflow

---

## 4. Installation & Setup

### Step 1: Create a project folder

```
LangGraph_Tutorials/
```

Open this folder in **VS Code**.

---

### Step 2: Create virtual environment

```bash
python -m venv myenv
```

Activate it (Windows):

```bash
myenv\Scripts\activate
```

---

### Step 3: Install required libraries

```bash
pip install langgraph langchain langchain-openai python-dotenv
```

**Why these libraries?**

* `langgraph` → Workflow engine
* `langchain` → LLM tools (models, prompts, loaders)
* `langchain-openai` → OpenAI models
* `python-dotenv` → Environment variables

---

## 5. Why Jupyter Notebook?

We use **Jupyter Notebook (.ipynb)** because:

* LangGraph graphs can be **visualized**
* Easier debugging
* Better learning experience

---

## 6. First Workflow (Non-LLM) – BMI Calculator

### Problem

* **Input:** weight, height
* **Process:** Calculate BMI
* **Output:** Updated state

---

## 7. Core LangGraph Concept

Every LangGraph workflow follows **4 steps**:

1. Define **State**
2. Add **Nodes**
3. Add **Edges**
4. **Compile & Execute**

---

## 8. Define State (TypedDict)

State = shared memory that flows through the graph.

```python
from typing import TypedDict

class BMIState(TypedDict):
    weight_kg: float
    height_m: float
    bmi: float
```

---

## 9. Create the Graph

```python
from langgraph.graph import StateGraph

graph = StateGraph(BMIState)
```

---

## 10. Define Node (Python Function)

Each **node = Python function**

```python
def calculate_bmi(state: BMIState) -> BMIState:
    weight = state["weight_kg"]
    height = state["height_m"]

    bmi = weight / (height ** 2)
    state["bmi"] = round(bmi, 2)

    return state
```

---

## 11. Add Node to Graph

```python
graph.add_node("calculate_bmi", calculate_bmi)
```

---

## 12. Add Start & End Edges

```python
from langgraph.graph import START, END

graph.add_edge(START, "calculate_bmi")
graph.add_edge("calculate_bmi", END)
```

---

## 13. Compile the Graph

```python
workflow = graph.compile()
```

---

## 14. Execute the Workflow

```python
initial_state = {
    "weight_kg": 80,
    "height_m": 1.73
}

final_state = workflow.invoke(initial_state)
print(final_state)
```

**Output:**

```python
{
 'weight_kg': 80,
 'height_m': 1.73,
 'bmi': 26.73
}
```

---

## 15. Visualize the Graph (Jupyter Only)

```python
workflow.get_graph().draw_mermaid_png()
```

Graph:

```
START → calculate_bmi → END
```

---

## 16. Making Workflow Slightly Complex (BMI Category)

Now we add:

* A **second node**
* BMI category: Underweight / Normal / Overweight / Obese

---

## 17. Update State

```python
class BMIState(TypedDict):
    weight_kg: float
    height_m: float
    bmi: float
    category: str
```

---

## 18. New Node – Label BMI

```python
def label_bmi(state: BMIState) -> BMIState:
    bmi = state["bmi"]

    if bmi < 18.5:
        state["category"] = "Underweight"
    elif bmi < 25:
        state["category"] = "Normal"
    elif bmi < 30:
        state["category"] = "Overweight"
    else:
        state["category"] = "Obese"

    return state
```

---

## 19. Add Node & Edges

```python
graph.add_node("label_bmi", label_bmi)

graph.add_edge("calculate_bmi", "label_bmi")
graph.add_edge("label_bmi", END)
```

Graph:

```
START → calculate_bmi → label_bmi → END
```

---

## 20. Execute Again

```python
final_state = workflow.invoke({
    "weight_kg": 80,
    "height_m": 1.73
})

print(final_state)
```

**Output:**

```python
{
 'weight_kg': 80,
 'height_m': 1.73,
 'bmi': 26.73,
 'category': 'Overweight'
}
```

---

# 🚀 LLM Workflow (LangGraph + LangChain)

## 21. LLM Workflow Idea

* Input: **question**
* Node calls **LLM**
* Output: **answer**

---

## 22. Environment Setup

Create a `.env` file:

```
OPENAI_API_KEY=your_api_key_here
```

---

## 23. Imports

```python
from langgraph.graph import StateGraph, START, END
from langchain_openai import ChatOpenAI
from typing import TypedDict
from dotenv import load_dotenv

load_dotenv()
model = ChatOpenAI()
```

---

## 24. Define State

```python
class LLMState(TypedDict):
    question: str
    answer: str
```

---

## 25. Node Function

```python
def llm_qa(state: LLMState) -> LLMState:
    question = state["question"]

    prompt = f"Answer the following question:\n{question}"
    response = model.invoke(prompt)

    state["answer"] = response.content
    return state
```

---

## 26. Build Graph

```python
graph = StateGraph(LLMState)

graph.add_node("llm_qa", llm_qa)
graph.add_edge(START, "llm_qa")
graph.add_edge("llm_qa", END)

workflow = graph.compile()
```

---

## 27. Execute

```python
final_state = workflow.invoke({
    "question": "How far is the Moon from Earth?"
})

print(final_state["answer"])
```

---

# 🔗 Prompt Chaining Workflow

Prompt chaining = **multiple LLM calls in sequence**

---

## 28. Prompt Chaining Use Case

* Generate **outline**
* Generate **blog using outline**

---

## 29. State Definition

```python
class BlogState(TypedDict):
    title: str
    outline: str
    content: str
```

---

## 30. Node 1 – Create Outline

```python
def create_outline(state: BlogState) -> BlogState:
    title = state["title"]

    prompt = f"Generate a detailed outline for a blog on the topic: {title}"
    response = model.invoke(prompt)

    state["outline"] = response.content
    return state
```

---

## 31. Node 2 – Create Blog

```python
def create_blog(state: BlogState) -> BlogState:
    title = state["title"]
    outline = state["outline"]

    prompt = f"""
    Write a detailed blog on the topic \"{title}\"
    using the following outline:
    {outline}
    """

    response = model.invoke(prompt)
    state["content"] = response.content
    return state
```

---

## 32. Build Prompt Chaining Graph

```python
graph = StateGraph(BlogState)

graph.add_node("create_outline", create_outline)
graph.add_node("create_blog", create_blog)

graph.add_edge(START, "create_outline")
graph.add_edge("create_outline", "create_blog")
graph.add_edge("create_blog", END)

workflow = graph.compile()
```

---

## 33. Execute Prompt Chaining

```python
final_state = workflow.invoke({
    "title": "Rise of AI in India"
})

print(final_state["outline"])
print(final_state["content"])
```

---

## 34. Why LangGraph is Powerful

Unlike LangChain chains:

* Intermediate outputs are accessible
* State evolves step-by-step
* Better debugging
* More control over workflows

---

## 35. Homework (Important)

Add **one more node**:

* `evaluate_blog`

**Prompt:**

```
Based on this outline and blog,
rate the blog from 1–10.
Return only an integer score.
```

Update:

* **State** → add `score`
* **Graph** → add new node + edge

---

## 36. Final Takeaway

* LangGraph is **overkill for simple linear workflows**
* But extremely powerful for:

  * Complex agents
  * Conditional logic
  * Multi-step reasoning
  * Agentic AI systems

---

# 📘 Agentic AI using LangGraph – Parallel Workflows (Simple Notes)

---

## 1️⃣ What this video is about

This video continues the **Agentic AI using LangGraph** playlist.

### Till now, we learned:

* What Agentic AI is
* Why LangGraph is used
* LangGraph core concepts
* Sequential (linear) workflows
* First practical example (from the last video)

### In this video:

* 👉 We learn **Parallel Workflows using LangGraph**
* 👉 Two examples are covered:

  * **Non-LLM parallel workflow** (Cricket stats)
  * **LLM-based parallel workflow** (UPSC Essay Evaluation)

---

## 2️⃣ What is a Parallel Workflow?

* Multiple nodes run **at the same time**
* Nodes **do not depend** on each other
* All nodes use the **same input state**
* Outputs from nodes are **merged later**

📌 **Example**:

* Strike Rate
* Boundary %
* Balls per Boundary

All these can be calculated independently, so they can run in parallel.

---

## 3️⃣ Example 1 – Cricket Batsman Parallel Workflow (Non-LLM)

### 🎯 Goal

Given batsman data:

* Runs
* Balls
* Fours
* Sixes

Calculate **in parallel**:

* Strike Rate
* Boundary Percentage
* Balls per Boundary

Then generate a **summary**.

---

## 4️⃣ Workflow Structure

```
START
 ├── Calculate Strike Rate
 ├── Calculate Boundary %
 ├── Calculate Balls per Boundary
      ↓
    Summary
      ↓
     END
```

---

## 5️⃣ Define State (Very Important)

The state holds **all data used in the workflow**.

```python
from typing import TypedDict

class BatsmanState(TypedDict):
    runs: int
    balls: int
    fours: int
    sixes: int
    strike_rate: float
    boundary_percent: float
    balls_per_boundary: float
    summary: str
```

---

## 6️⃣ Create Nodes (Functions)

### 6.1 Calculate Strike Rate

```python
def calculate_strike_rate(state: BatsmanState):
    sr = (state["runs"] / state["balls"]) * 100
    return {"strike_rate": sr}  # partial update
```

---

### 6.2 Calculate Balls per Boundary

```python
def calculate_balls_per_boundary(state: BatsmanState):
    bpb = state["balls"] / (state["fours"] + state["sixes"])
    return {"balls_per_boundary": bpb}
```

---

### 6.3 Calculate Boundary Percentage

```python
def calculate_boundary_percent(state: BatsmanState):
    boundary_runs = (state["fours"] * 4) + (state["sixes"] * 6)
    percent = (boundary_runs / state["runs"]) * 100
    return {"boundary_percent": percent}
```

---

### 6.4 Summary Node

```python
def summary_node(state: BatsmanState):
    summary = (
        f"Strike Rate: {state['strike_rate']}\n"
        f"Balls per Boundary: {state['balls_per_boundary']}\n"
        f"Boundary %: {state['boundary_percent']}"
    )
    return {"summary": summary}
```

---

## 7️⃣ Build the Graph

```python
from langgraph.graph import StateGraph, START, END

graph = StateGraph(BatsmanState)

graph.add_node("strike_rate", calculate_strike_rate)
graph.add_node("bpb", calculate_balls_per_boundary)
graph.add_node("boundary_percent", calculate_boundary_percent)
graph.add_node("summary", summary_node)
```

---

## 8️⃣ Define Edges (Parallel Execution)

```python
graph.add_edge(START, "strike_rate")
graph.add_edge(START, "bpb")
graph.add_edge(START, "boundary_percent")

graph.add_edge("strike_rate", "summary")
graph.add_edge("bpb", "summary")
graph.add_edge("boundary_percent", "summary")

graph.add_edge("summary", END)
```

---

## 9️⃣ Compile & Run Workflow

```python
workflow = graph.compile()

initial_state = {
    "runs": 100,
    "balls": 50,
    "fours": 6,
    "sixes": 4
}

result = workflow.invoke(initial_state)
print(result["summary"])
```

---

## 🔟 Important Concept – Partial State Updates ⚠️

### ❌ Wrong (causes error in parallel workflows)

```python
return state
```

### ✅ Correct

```python
return {"strike_rate": sr}
```

📌 **Reason**:

* Parallel nodes must **not overwrite shared state**
* Only return the **field you update**
* This avoids conflicts

👉 **Best Practice**:
Always use **partial state updates**, even in sequential workflows.

---

## 1️⃣1️⃣ Example 2 – UPSC Essay Evaluation (LLM-Based Parallel Workflow)

### 🎯 Goal

Evaluate an essay on:

* Language Quality
* Depth of Analysis
* Clarity of Thought

Each evaluation:

* Runs in parallel
* Uses an LLM
* Returns:

  * Text feedback
  * Score (0–10)

Final node:

* Merges feedback
* Calculates average score

---

## 1️⃣2️⃣ Why Structured Output is Needed

### ❌ Problem

* LLM may return "seven" instead of `7`
* Difficult to calculate average score

### ✅ Solution

* Use **Structured Output**
* Enforce schema using **Pydantic**

---

## 1️⃣3️⃣ Define Evaluation Schema

```python
from pydantic import BaseModel, Field

class EvaluationSchema(BaseModel):
    feedback: str = Field(description="Detailed feedback")
    score: int = Field(ge=0, le=10, description="Score out of 10")
```

---

## 1️⃣4️⃣ Create Structured LLM

```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini")
structured_llm = llm.with_structured_output(EvaluationSchema)
```

---

## 1️⃣5️⃣ UPSC Workflow State

```python
from typing import List
from typing_extensions import Annotated
import operator

class UPSCState(TypedDict):
    essay: str
    language_feedback: str
    analysis_feedback: str
    clarity_feedback: str
    overall_feedback: str
    individual_scores: Annotated[List[int], operator.add]
    average_score: float
```

📌 `operator.add` is a **reducer function** used to merge scores from parallel nodes.

---

## 1️⃣6️⃣ Evaluation Nodes (Parallel)

### Language Evaluation

```python
def evaluate_language(state: UPSCState):
    result = structured_llm.invoke(
        f"Evaluate language quality:\n{state['essay']}"
    )
    return {
        "language_feedback": result.feedback,
        "individual_scores": [result.score]
    }
```

> Analysis and Clarity nodes are similar (only prompt and key name change).

---

## 1️⃣7️⃣ Final Evaluation Node

```python
def final_evaluation(state: UPSCState):
    avg = sum(state["individual_scores"]) / len(state["individual_scores"])

    summary_prompt = f"""
    Language Feedback: {state['language_feedback']}
    Analysis Feedback: {state['analysis_feedback']}
    Clarity Feedback: {state['clarity_feedback']}
    """

    summary = llm.invoke(summary_prompt).content

    return {
        "overall_feedback": summary,
        "average_score": avg
    }
```

---

## 1️⃣8️⃣ Key Concepts Learned 🎯

### ✅ Parallel Workflows

* Nodes run simultaneously
* Use partial state updates

### ✅ Structured Output

* Reliable LLM responses
* Schema-based validation

### ✅ Reducer Functions

* Merge parallel outputs
* Example: `operator.add`

### ✅ LangChain + LangGraph Together

* LangChain → LLM logic
* LangGraph → workflow orchestration

---

## 1️⃣9️⃣ Final Takeaway

Once you understand **nodes, edges, partial state updates, structured output, and reducers**, you can build **very powerful Agentic AI systems**.

This foundation will help you:

* Build real-world AI agents
* Create scalable workflows
* Avoid common parallel execution bugs

---

🚀 **You are now ready to build parallel, production-grade Agentic AI workflows using LangGraph.**



