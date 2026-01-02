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

# 📘 LangGraph Conditional Workflows – Simple English Notes

*(Agentic AI using LangGraph – Video 7)*

---

## 1️⃣ What we learned before this video

In the LangGraph playlist, we have already learned **two types of workflows**:

### ✅ 1. Sequential Workflow

* Tasks run **one after another**
* Linear execution

**Example:**

```
Task1 → Task2 → Task3 → Task4
```

---

### ✅ 2. Parallel Workflow

* Multiple tasks run **at the same time**
* Branching happens, but **all branches execute**

**Example:**

```
        → Task2 →
Task1                 → Task4
        → Task3 →
```

---

## 2️⃣ What is a Conditional Workflow? (NEW TOPIC)

### 🔹 Definition

A **Conditional Workflow** is a workflow where:

* Multiple branches exist
* **Only ONE branch executes**
* The branch is chosen based on a **condition**

👉 It is exactly like **if–else** in programming.

---

### 🔹 Difference between Parallel & Conditional Workflow

| Parallel Workflow      | Conditional Workflow         |
| ---------------------- | ---------------------------- |
| All branches run       | Only one branch runs         |
| No condition           | Condition decides path       |
| Tasks execute together | Tasks are mutually exclusive |

---

### 🔹 Example Flow

```
Task1
  |
  |-- if condition A → Task2 → Task4
  |
  |-- if condition B → Task3 → Task4
```

🚫 **Task2 and Task3 never run together**

---

### ⚠️ Why Conditional Workflows are IMPORTANT

* Almost every **real-world agentic AI system needs conditions**
* Just like `if-else` is critical in programming,
  **conditional branching is critical in LangGraph**

---

## 3️⃣ How we approach this topic

We build **2 workflows**:

### 1️⃣ Non-LLM workflow

* Quadratic Equation Solver
* Focus: **Concept clarity**

### 2️⃣ LLM-based workflow

* Customer Review Handling
* Focus: **Real-world AI system**

---

# 🧮 WORKFLOW 1: Quadratic Equation (Non-LLM)

---

## 4️⃣ Quadratic Equation Refresher

### General Form

```
ax² + bx + c = 0
```

### Discriminant

```
D = b² - 4ac
```

### Conditions

| Discriminant (D) | Roots             |
| ---------------- | ----------------- |
| D > 0            | Two real roots    |
| D = 0            | One repeated root |
| D < 0            | No real roots     |

---

## 5️⃣ Workflow Design

### Steps

1. Take input `a, b, c`
2. Display equation
3. Calculate discriminant
4. Conditionally choose:

   * Real roots
   * Repeated root
   * No real roots
5. End workflow

---

## 6️⃣ State Definition

```python
from typing import TypedDict

class QuadState(TypedDict):
    a: float
    b: float
    c: float
    equation: str
    discriminant: float
    result: str
```

---

## 7️⃣ Create Graph

```python
from langgraph.graph import StateGraph

graph = StateGraph(QuadState)
```

---

## 8️⃣ Node 1: Show Equation

```python
def show_equation(state: QuadState):
    eq = f"{state['a']}x² + {state['b']}x + {state['c']}"
    return {"equation": eq}
```

---

## 9️⃣ Node 2: Calculate Discriminant

```python
def calculate_discriminant(state: QuadState):
    d = state["b"]**2 - 4 * state["a"] * state["c"]
    return {"discriminant": d}
```

---

## 🔟 Connect Initial Nodes

```python
graph.add_node("show_equation", show_equation)
graph.add_node("calculate_discriminant", calculate_discriminant)

graph.add_edge("START", "show_equation")
graph.add_edge("show_equation", "calculate_discriminant")
```

---

## 1️⃣1️⃣ Root Calculation Nodes

### ✔️ Real Roots

```python
import math

def real_roots(state: QuadState):
    d = state["discriminant"]
    a = state["a"]
    b = state["b"]
    r1 = (-b + math.sqrt(d)) / (2 * a)
    r2 = (-b - math.sqrt(d)) / (2 * a)
    return {"result": f"Roots are {r1} and {r2}"}
```

---

### ✔️ Repeated Root

```python
def repeated_root(state: QuadState):
    a = state["a"]
    b = state["b"]
    r = -b / (2 * a)
    return {"result": f"Repeated root is {r}"}
```

---

### ❌ No Real Roots

```python
def no_real_roots(state: QuadState):
    return {"result": "No real roots"}
```

---

## 1️⃣2️⃣ Condition Function (MOST IMPORTANT)

```python
def check_condition(state: QuadState):
    d = state["discriminant"]
    if d > 0:
        return "real_roots"
    elif d == 0:
        return "repeated_root"
    else:
        return "no_real_roots"
```

---

## 1️⃣3️⃣ Conditional Edges

```python
graph.add_conditional_edges(
    "calculate_discriminant",
    check_condition
)
```

---

## 1️⃣4️⃣ End Connections

```python
graph.add_edge("real_roots", "END")
graph.add_edge("repeated_root", "END")
graph.add_edge("no_real_roots", "END")

workflow = graph.compile()
```

---

## 1️⃣5️⃣ Run Workflow

```python
workflow.invoke({"a": 4, "b": -5, "c": -4})
```

---

### 🎯 Key Learning (Workflow 1)

Conditional routing is done using:

* A **condition function**
* `add_conditional_edges()`

---

# 🤖 WORKFLOW 2: LLM-Based Review Handling

---

## 16️⃣ Problem Statement

We receive a **customer review** and must:

* Detect sentiment
* Respond differently for:

  * Positive review
  * Negative review

---

## 17️⃣ Workflow Design

```
Review
  ↓
Find Sentiment (LLM)
  ↓
IF Positive → Positive Response
IF Negative → Diagnosis → Negative Response
```

---

## 18️⃣ Structured Output: Sentiment Schema

```python
from pydantic import BaseModel
from typing import Literal

class SentimentSchema(BaseModel):
    sentiment: Literal["positive", "negative"]
```

---

## 19️⃣ LLM Setup

```python
from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-4o-mini")

structured_model = model.with_structured_output(SentimentSchema)
```

---

## 20️⃣ Review State

```python
from typing import TypedDict

class ReviewState(TypedDict):
    review: str
    sentiment: Literal["positive", "negative"]
    diagnosis: dict
    response: str
```

---

## 21️⃣ Node: Find Sentiment

```python
def find_sentiment(state: ReviewState):
    prompt = f"Find sentiment of this review:\n{state['review']}"
    result = structured_model.invoke(prompt)
    return {"sentiment": result.sentiment}
```

---

## 22️⃣ Condition Function

```python
def check_sentiment(state: ReviewState):
    if state["sentiment"] == "positive":
        return "positive_response"
    else:
        return "run_diagnosis"
```

---

## 23️⃣ Positive Response Node

```python
def positive_response(state: ReviewState):
    prompt = f"Write a warm thank you reply for:\n{state['review']}"
    res = model.invoke(prompt)
    return {"response": res.content}
```

---

## 24️⃣ Diagnosis Schema

```python
class DiagnosisSchema(BaseModel):
    issue_type: Literal["UI", "Performance", "Bug", "Support", "Other"]
    tone: Literal["Calm", "Frustrated", "Angry"]
    urgency: Literal["Low", "Medium", "High"]
```

---

## 25️⃣ Diagnosis Node

```python
diagnosis_model = model.with_structured_output(DiagnosisSchema)

def run_diagnosis(state: ReviewState):
    prompt = f"Diagnose this review:\n{state['review']}"
    result = diagnosis_model.invoke(prompt)
    return {"diagnosis": result.model_dump()}
```

---

## 26️⃣ Negative Response Node

```python
def negative_response(state: ReviewState):
    d = state["diagnosis"]
    prompt = f"""
User has issue: {d['issue_type']}
Tone: {d['tone']}
Urgency: {d['urgency']}
Write empathetic response.
"""
    res = model.invoke(prompt)
    return {"response": res.content}
```

---

## 27️⃣ Final Graph Connections

```python
graph.add_conditional_edges("find_sentiment", check_sentiment)

graph.add_edge("positive_response", "END")
graph.add_edge("run_diagnosis", "negative_response")
graph.add_edge("negative_response", "END")
```

---

## 🎯 Final Takeaways

* Conditional workflows = **if–else logic for agents**
* Core steps:

  1. Write condition function
  2. Return next node name
  3. Use `add_conditional_edges()`

👉 This concept is used **almost everywhere in advanced Agentic AI systems**
# 📘 LangGraph Iterative (Looping) Workflow – Simple English Notes

This README explains **Iterative (Looping) Workflows in LangGraph** using a real-world example. It covers concepts, design, and complete runnable code.

---

## 1️⃣ What We Learned Before

In the **Agentic AI using LangGraph** playlist, we already learned three workflow types:

### ✅ Sequential Workflow

* Tasks run one after another
* Linear execution

```
Task1 → Task2 → Task3
```

---

### ✅ Parallel Workflow

* Multiple tasks run at the same time
* All branches execute

```
      → Task2 →
Task1              → Task4
      → Task3 →
```

---

### ✅ Conditional Workflow

* Multiple branches exist
* Only **one branch runs**
* Decision based on condition (if–else)

---

## 2️⃣ Iterative (Looping) Workflow

### 🔹 What is an Iterative Workflow?

An **Iterative (Looping) Workflow** is a workflow where:

* Tasks run again and again
* Output is gradually improved
* Loop stops when a condition is satisfied

👉 Just like a **while loop** in programming.

### 🔹 Why It Is Important

* AI output is rarely perfect on first try
* Needed for:

  * Generate
  * Evaluate
  * Improve

Used in:

* Content generation
* Code refinement
* Planning agents
* Self‑improving AI systems

---

## 3️⃣ Real-Life Use Case: Content Automation

### Problem

* You create YouTube videos
* No time to post on:

  * Twitter (X)
  * LinkedIn
  * Instagram

### Solution

Build an automated workflow that:

1. Takes a topic
2. Generates a tweet
3. Evaluates quality
4. Improves it until approved

---

## 4️⃣ High-Level Workflow Design

### Components

| Component     | Role                   |
| ------------- | ---------------------- |
| Generator LLM | Creates tweet          |
| Evaluator LLM | Judges quality         |
| Optimizer LLM | Improves tweet         |
| Loop          | Repeats until approved |

### 🔁 Flow

```
Topic
  ↓
Generate Tweet
  ↓
Evaluate Tweet
  ├── Approved → END
  └── Needs Improvement
          ↓
     Optimize Tweet
          ↓
       Evaluate Again
```

---

## 5️⃣ Defining Workflow State

In LangGraph, **state is mandatory**.

```python
from typing import TypedDict, Literal
from typing_extensions import Annotated
import operator

class TweetState(TypedDict):
    topic: str
    tweet: str
    evaluation: Literal["approved", "needs_improvement"]
    feedback: str
    iteration: int
    max_iteration: int

    tweet_history: Annotated[list[str], operator.add]
    feedback_history: Annotated[list[str], operator.add]
```

### Why These Fields?

* `topic` → input topic
* `tweet` → current tweet
* `evaluation` → decision
* `feedback` → evaluator comments
* `iteration` → loop counter
* `max_iteration` → safety stop
* `tweet_history` → all tweets
* `feedback_history` → all feedback

---

## 6️⃣ Creating LLMs

```python
from langchain_openai import ChatOpenAI

generator_llm = ChatOpenAI(model="gpt-4o")
evaluator_llm = ChatOpenAI(model="gpt-4o-mini")
optimizer_llm = ChatOpenAI(model="gpt-4o")
```

👉 In real projects, select the best model per task.

---

## 7️⃣ Node 1: Generate Tweet

```python
from langchain.schema import SystemMessage, HumanMessage

def generate_tweet(state: TweetState):
    messages = [
        SystemMessage(content="You are a funny and clever Twitter influencer."),
        HumanMessage(content=f"""
Write a short, original, hilarious tweet on the topic: {state['topic']}

Rules:
- No Q&A format
- Max 280 characters
- Use humor, sarcasm, irony
- Simple English
""")
    ]

    response = generator_llm.invoke(messages)

    return {
        "tweet": response.content,
        "tweet_history": [response.content]
    }
```

---

## 8️⃣ Node 2: Evaluate Tweet (Structured Output)

### Evaluation Schema

```python
from pydantic import BaseModel
from typing import Literal

class TweetEvaluation(BaseModel):
    evaluation: Literal["approved", "needs_improvement"]
    feedback: str
```

### Evaluator Function

```python
structured_evaluator = evaluator_llm.with_structured_output(TweetEvaluation)

def evaluate_tweet(state: TweetState):
    messages = [
        SystemMessage(content="You are a ruthless Twitter critic."),
        HumanMessage(content=f"""
Evaluate the tweet below:

Tweet:
{state['tweet']}

Return:
- evaluation (approved / needs_improvement)
- feedback
""")
    ]

    result = structured_evaluator.invoke(messages)

    return {
        "evaluation": result.evaluation,
        "feedback": result.feedback,
        "feedback_history": [result.feedback]
    }
```

---

## 9️⃣ Node 3: Optimize Tweet

```python
def optimize_tweet(state: TweetState):
    messages = [
        SystemMessage(content="You improve tweets using feedback."),
        HumanMessage(content=f"""
Improve this tweet based on feedback:

Tweet: {state['tweet']}
Feedback: {state['feedback']}

Rules:
- Under 280 characters
- No Q&A
""")
    ]

    response = optimizer_llm.invoke(messages)

    return {
        "tweet": response.content,
        "iteration": state["iteration"] + 1,
        "tweet_history": [response.content]
    }
```

---

## 🔟 Routing Logic (Loop Decision)

```python
def route_evaluation(state: TweetState):
    if (
        state["evaluation"] == "approved"
        or state["iteration"] >= state["max_iteration"]
    ):
        return "approved"
    else:
        return "needs_improvement"
```

---

## 1️⃣1️⃣ Building the LangGraph

```python
from langgraph.graph import StateGraph, END

graph = StateGraph(TweetState)

graph.add_node("generate", generate_tweet)
graph.add_node("evaluate", evaluate_tweet)
graph.add_node("optimize", optimize_tweet)

graph.add_edge("start", "generate")
graph.add_edge("generate", "evaluate")

graph.add_conditional_edges(
    "evaluate",
    route_evaluation,
    {
        "approved": END,
        "needs_improvement": "optimize"
    }
)

graph.add_edge("optimize", "evaluate")

workflow = graph.compile()
```

---

## 1️⃣2️⃣ Running the Workflow

```python
initial_state = {
    "topic": "Indian Railways",
    "iteration": 1,
    "max_iteration": 5,
    "tweet_history": [],
    "feedback_history": []
}

result = workflow.invoke(initial_state)
```

---

## 1️⃣3️⃣ Output Analysis

* Tweet may be approved in first iteration
* Or after multiple improvements
* `tweet_history` shows evolution
* `feedback_history` shows reasoning

---

## 1️⃣4️⃣ Key Takeaways ⭐

* Iterative workflows enable **self‑improving AI**
* LangGraph loops are created using:

  * Conditional edges
  * Normal edges
* Always use `max_iteration` to avoid infinite loops
* Used in:

  * AI writing agents
  * Code agents
  * Planning agents
  * Autonomous systems

---

🚀 **You now know how to build looping agents in LangGraph!**

# 📘 Building a Chatbot with Memory using LangGraph

*(Simple English Notes + Code)*

---

## 1️⃣ What we have learned so far in the LangGraph playlist

Till now, we have learned:

* LangGraph fundamentals
* Basics of Agentic AI
* Different types of workflows:

  * ✅ Sequential Workflow
  * ✅ Parallel Workflow
  * ✅ Conditional Workflow
  * ✅ Iterative / Looping Workflow

At this point, we know enough basics to start building real Agentic AI applications.

---

## 2️⃣ What we are building now

We will now deep dive and build a real chatbot using LangGraph.

### This chatbot will support:

* Normal chatting (LLM-based chat)
* Memory (remember past conversation)

### Later we will add:

* RAG (document-based answers)
* Tools (actions)
* UI
* LangSmith integration

### Advanced concepts we will cover:

* Memory
* Persistence
* Checkpointers
* Human-in-the-loop (HITL)
* Retry logic
* Fault tolerance

👉 **This video = Part 1**
We build a **basic chatbot with memory support**.

---

## 3️⃣ Chatbot = Workflow (Important Concept)

A chatbot is basically a **workflow**.

### Our chatbot workflow:

* It is a **Sequential Workflow**
* It has **only ONE node**

### Flow:

```
START
  ↓
User Message
  ↓
Chat Node (LLM)
  ↓
AI Response
  ↓
END
```

This process repeats while the user keeps chatting.

---

## 4️⃣ What is the STATE of this workflow?

In LangGraph, **every workflow needs a state**.

### For a chatbot, what is the most important data?

👉 **Conversation messages**

So our state will store:

* All messages exchanged between **user and AI**

---

## 5️⃣ Defining the Chat State

### Why not just `list[str]`?

Because LangChain / LangGraph works with **message objects**, not plain strings.

### Types of messages:

* `HumanMessage`
* `AIMessage`
* `SystemMessage`
* `ToolMessage`

All of them inherit from **BaseMessage**.

### ✅ Chat State Definition

```python
from typing import Annotated, TypedDict
from langgraph.graph.message import add_messages
from langchain_core.messages import BaseMessage

class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]
```

### Why `add_messages` reducer?

* Default state behavior **replaces old values**
* We want to **append messages**, not replace them
* `add_messages` is optimized for message lists

---

## 6️⃣ Creating the Graph

```python
from langgraph.graph import StateGraph, START, END

graph = StateGraph(ChatState)
```

---

## 7️⃣ Creating the Chat Node

This node:

* Takes messages from state
* Sends them to the LLM
* Stores the AI response back in state

### Chat Node Function

```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI()

def chat_node(state: ChatState):
    messages = state["messages"]
    response = llm.invoke(messages)

    return {
        "messages": [response]
    }
```

---

## 8️⃣ Adding Node & Edges

```python
graph.add_node("chat_node", chat_node)

graph.add_edge(START, "chat_node")
graph.add_edge("chat_node", END)
```

---

## 9️⃣ Compile the Graph

```python
chatbot = graph.compile()
```

### Workflow structure:

```
START → chat_node → END
```

---

## 🔟 Testing the chatbot (Single message)

```python
from langchain_core.messages import HumanMessage

initial_state = {
    "messages": [HumanMessage(content="What is the capital of India?")]
}

result = chatbot.invoke(initial_state)

print(result["messages"][-1].content)
```

✅ **Output:**

```
The capital of India is New Delhi.
```

---

## 1️⃣1️⃣ Problem: This is NOT a real chatbot yet

❌ It answers only one question
❌ Conversation does not continue

A real chatbot should:

* Keep chatting
* Remember previous messages

---

## 1️⃣2️⃣ Adding a Chat Loop (Console Chatbot)

```python
while True:
    user_input = input("You: ")

    if user_input.strip().lower() in ["exit", "quit", "bye"]:
        print("Chat ended.")
        break

    response = chatbot.invoke({
        "messages": [HumanMessage(content=user_input)]
    })

    ai_reply = response["messages"][-1].content
    print("AI:", ai_reply)
```

---

## 1️⃣3️⃣ BIG PROBLEM: Chatbot forgets everything 😵

### Example:

```
User: Hi, my name is Nitesh
AI: Hello Nitesh!

User: What is my name?
AI: Sorry, I don't know.
```

### Why this happens?

* Each `invoke()` call starts fresh
* State is **not persisted**
* Previous conversation is lost

---

## 1️⃣4️⃣ Why state is getting erased?

* Each loop iteration calls `chatbot.invoke()`
* Workflow runs → reaches `END`
* State is discarded
* Next call starts from scratch

---

## 1️⃣5️⃣ Solution: Persistence (Memory)

### What is Persistence?

Persistence means:

* Do **NOT** delete state after workflow ends
* Store it somewhere:

  * RAM (memory)
  * Database (production)

👉 For now, we use **RAM-based memory**.

---

## 1️⃣6️⃣ Adding Memory using Checkpointer

### Import `MemorySaver`

```python
from langgraph.checkpoint.memory import MemorySaver
```

### Create a Checkpointer

```python
checkpointer = MemorySaver()
```

### Compile graph with persistence

```python
chatbot = graph.compile(checkpointer=checkpointer)
```

---

## 1️⃣7️⃣ Thread ID (VERY IMPORTANT)

### What is a thread?

* One conversation = one thread
* Different users = different threads

```python
thread_id = "nitesh-chat"
```

---

## 1️⃣8️⃣ Passing config while invoking

```python
config = {
    "configurable": {
        "thread_id": thread_id
    }
}
```

### Updated invoke call

```python
response = chatbot.invoke(
    {
        "messages": [HumanMessage(content=user_input)]
    },
    config=config
)
```

---

## 1️⃣9️⃣ Now chatbot REMEMBERS 🎉

### Example:

```
User: Hi my name is Nitesh
AI: Hello Nitesh!

User: What is my name?
AI: Your name is Nitesh.
```

### Math example:

```
User: Add 10 to 100
AI: 110

User: Multiply the result by 2
AI: 220
```

---

## 2️⃣0️⃣ Why memory works now (Behind the scenes)

* After each workflow execution:

  * State is saved in RAM
* Next `invoke()`:

  * Previous state is fetched
  * New messages are appended

### Thanks to:

* `add_messages` reducer
* `MemorySaver` checkpointer
* `thread_id`

---

## 2️⃣1️⃣ Important Limitation of RAM Memory

❌ If program restarts → memory is lost

### Production systems use:

* Databases (Postgres, Redis, etc.)

So chatbot remembers conversations even after restart.

---

## 2️⃣2️⃣ Summary

### What we built:

* ✅ LangGraph-based chatbot
* ✅ Message-based state
* ✅ Reducer-based history handling
* ✅ Loop-based chatting
* ✅ Memory using persistence
* ✅ Thread-based conversations

---

🎯 **Next Steps:**

* Deep dive into **Persistence**
* Understanding **Threads & Checkpointers**
* Adding **RAG, Tools, UI, and HITL**

---

🚀 You are now building **industry-grade Agentic AI systems** with LangGraph!

# 📘 LangGraph Persistence – Simple English Notes (with Code)

---

## 1️⃣ What is Persistence in LangGraph?

**Persistence** means:

👉 Ability to **save and restore the state of a workflow over time**

### In simple words:

* Normally, when a LangGraph workflow finishes → **state is lost**
* With persistence → **state is saved**

Later you can:

* Resume workflow
* Recover after crash
* Resume chat
* Debug past executions

📌 **Persistence = Memory for workflows**

---

## 2️⃣ Two Core Concepts You Already Know

### 🔹 1. Graph

* Workflow is a **graph**
* Nodes = tasks
* Edges = execution order

Example:

```
START → Task1 → Task2 → END
```

---

### 🔹 2. State

* **State = dictionary**
* Stores important data during workflow execution

Example:

```python
state = {
    "messages": [],
    "topic": "pizza",
    "joke": ""
}
```

✔ Every node can:

* Read state
* Update state

---

## 3️⃣ Default LangGraph Behavior (Without Persistence)

* Workflow executes
* State keeps changing
* Workflow ends
* ❌ State is erased from memory (RAM)

👉 You **cannot access old state later**

---

## 4️⃣ What Persistence Changes

With persistence:

* State is saved externally
* State can be restored later
* Works across crashes, restarts, sessions

📌 This enables:

* Fault tolerance
* Chat history
* Resume workflows
* Debugging (time travel)

---

## 5️⃣ Speciality of Persistence ⭐

❗ **Very Important Point**

Persistence does **NOT** store only final state
It stores **ALL intermediate states**

### Example workflow:

| Step   | State Value |
| ------ | ----------- |
| Start  | name = "A"  |
| Node 1 | name = "B"  |
| Node 2 | name = "C"  |
| End    | name = "C"  |

✔ All values **A → B → C** are stored

---

## 6️⃣ Why This is Powerful?

### 🔹 1. Fault Tolerance

* If workflow crashes:

  * Resume from **last saved checkpoint**
  * Not from start

### 🔹 2. Chatbots (Resume Chat)

* Old conversations can be restored
* Exactly how ChatGPT resumes chats

---

## 7️⃣ Where is State Stored?

👉 In some **database**

Examples:

* In-memory (RAM) → demo only
* PostgreSQL → production
* Redis → production

---

## 8️⃣ Checkpointer (MOST IMPORTANT)

### 🔹 What is a Checkpointer?

* Persistence is implemented using **Checkpointers**
* Checkpointer:

  * Splits workflow into checkpoints
  * Saves state at each checkpoint

📌 Checkpoints are created at **every superstep**

---

### 🔹 What is a Superstep?

* A **superstep** = group of nodes running together
* Parallel nodes = one superstep

Each superstep → **1 checkpoint**

---

## 9️⃣ Example of Checkpointer (Numbers Example)

### State

```python
numbers: List[int]
```

### Execution

| Checkpoint     | State           |
| -------------- | --------------- |
| Start          | [1]             |
| Node 1         | [1, 2]          |
| Parallel Nodes | [1, 2, 3, 4, 5] |
| End            | [1, 2, 3, 4, 5] |

✔ All saved in database

---

## 🔟 Threads (VERY IMPORTANT)

### 🔹 What is a Thread?

* Every workflow execution gets a **thread_id**
* Helps separate multiple executions

Example:

```
Thread 1 → Pizza joke
Thread 2 → Pasta joke
```

📌 Without `thread_id` → all states get mixed

---

### 🔹 Why Threads Matter?

* Resume **specific execution**
* Resume **specific chat**
* Load correct state from database

---

## 1️⃣1️⃣ Basic Persistence Code (In-Memory Demo)

### 🔹 Imports

```python
from langgraph.graph import StateGraph
from langgraph.checkpoint.memory import MemorySaver
```

---

### 🔹 Define State

```python
from typing import TypedDict

class JokeState(TypedDict):
    topic: str
    joke: str
    explanation: str
```

---

### 🔹 Node Functions

```python
def generate_joke(state: JokeState):
    joke = f"Why did the {state['topic']} go to the doctor? Because it felt cheesy!"
    return {"joke": joke}


def generate_explanation(state: JokeState):
    explanation = f"It is funny because {state['topic']} is related to cheese."
    return {"explanation": explanation}
```

---

### 🔹 Build Graph

```python
graph = StateGraph(JokeState)

graph.add_node("generate_joke", generate_joke)
graph.add_node("generate_explanation", generate_explanation)

graph.set_entry_point("generate_joke")
graph.add_edge("generate_joke", "generate_explanation")
graph.set_finish_point("generate_explanation")
```

---

### 🔹 Enable Persistence

```python
checkpointer = MemorySaver()

workflow = graph.compile(checkpointer=checkpointer)
```

---

### 🔹 Run Workflow (with Thread ID)

```python
config = {"configurable": {"thread_id": "1"}}

workflow.invoke(
    {"topic": "pizza"},
    config=config
)
```

---

## 1️⃣2️⃣ Get Final State

```python
workflow.get_state(config)
```

---

## 1️⃣3️⃣ Get State History (All Checkpoints)

```python
workflow.get_state_history(config)
```

✔ Shows:

* Initial state
* Before each node
* After each node

---

## 1️⃣4️⃣ Resume Workflow After Crash

```python
workflow.invoke(
    None,  # resume
    config=config
)
```

✔ Workflow resumes from last checkpoint

---

## 1️⃣5️⃣ Time Travel ⏳

### 🔹 What is Time Travel?

* Go back to any checkpoint
* Replay workflow from there
* Debug complex workflows

---

### 🔹 Get Specific Checkpoint State

```python
workflow.get_state(
    config=config,
    checkpoint_id="checkpoint-id-here"
)
```

---

### 🔹 Replay from Checkpoint

```python
workflow.invoke(
    None,
    config={
        "configurable": {
            "thread_id": "1",
            "checkpoint_id": "checkpoint-id-here"
        }
    }
)
```

---

## 1️⃣6️⃣ Update Past State (Advanced)

```python
workflow.update_state(
    config=config,
    checkpoint_id="checkpoint-id-here",
    values={"topic": "samosa"}
)
```

✔ Creates a **new branch of execution**

---

## 1️⃣7️⃣ Benefits of Persistence (FINAL)

✅ **1. Short-Term Memory**

* Resume chat conversations

✅ **2. Fault Tolerance**

* Resume after crashes

✅ **3. Human-in-the-Loop (HITL)**

* Pause workflow
* Wait for human input
* Resume later

✅ **4. Time Travel**

* Replay execution
* Debug workflows

---

## 🎯 Final Summary

* Persistence = backbone of LangGraph
* Implemented using **Checkpointers**
* Uses **Threads** to separate executions

### Enables:

* Chat memory
* Crash recovery
* HITL
* Debugging

📌 **Without persistence → LangGraph is incomplete**

# 📘 Building a Chatbot UI using LangGraph + Streamlit

*(Simple English Notes with Code)*

---

## 1️⃣ What problem are we solving?

In the previous video, we built a LangGraph chatbot with:

* Working logic ✅
* Short-term memory ✅

❌ **But there was one big problem**
The chatbot had **no UI (User Interface)**.

We were chatting with it only inside:

* Jupyter Notebook
* Terminal

👉 This is **not user-friendly**.

---

## 2️⃣ Goal of this video

We will:

* ✅ Give our LangGraph chatbot a **proper web UI**
* ✅ Build a **chat-style interface (like ChatGPT)**
* ✅ Use **Streamlit** to create the frontend
* ✅ Connect **Streamlit (Frontend)** with **LangGraph (Backend)**

---

## 3️⃣ Final Output (What we will build)

* Clean chat UI
* User and AI messages appear differently
* Automatic scrolling
* Chatbot remembers previous messages
* Supports:

  * General questions
  * Follow-up questions
  * Memory-based questions ("What is my name?")

---

## 4️⃣ Tech Stack Used

| Layer         | Technology              |
| ------------- | ----------------------- |
| Backend       | LangGraph               |
| LLM           | LangChain-supported LLM |
| Frontend      | Streamlit               |
| Memory        | LangGraph Checkpointer  |
| State Storage | Streamlit Session State |

---

## 5️⃣ High-Level Architecture

```
User
  ↓
Streamlit UI (Frontend)
  ↓
LangGraph Chatbot (Backend)
  ↓
LLM
  ↓
Response → UI
```

---

## 6️⃣ Project Structure

```
project/
│
├── langgraph_backend.py   # Chatbot logic (LangGraph)
├── streamlit_frontend.py  # UI code (Streamlit)
├── .env                   # API keys
└── venv/                  # Virtual environment
```

---

## 7️⃣ Backend Code (LangGraph)

This code is the **same as the previous chatbot**, no major changes.

### 🔹 Key Points

* Defines state
* Creates a simple graph
* Uses **InMemory Checkpointer**
* Exposes a `chatbot` object

### 🔹 Example (Simplified)

```python
from langgraph.graph import StateGraph, END
from langchain_core.messages import HumanMessage, AIMessage
from langgraph.checkpoint.memory import MemorySaver

class ChatState(dict):
    messages: list

def chat_node(state):
    # Call LLM here
    response = llm.invoke(state["messages"])
    return {"messages": state["messages"] + [response]}

builder = StateGraph(ChatState)
builder.add_node("chat", chat_node)
builder.set_entry_point("chat")
builder.add_edge("chat", END)

checkpointer = MemorySaver()
chatbot = builder.compile(checkpointer=checkpointer)
```

---

## 8️⃣ Why we split Backend & Frontend?

| Backend            | Frontend        |
| ------------------ | --------------- |
| LangGraph workflow | Streamlit UI    |
| LLM calls          | Input box       |
| Memory             | Message display |

👉 **Clean separation = scalable design**

---

## 9️⃣ Streamlit Chat UI – Core Components

Streamlit provides **two special chat components**:

### 1️⃣ `st.chat_message()`

Used to display messages

### 2️⃣ `st.chat_input()`

Used to take user input

---

## 🔟 Displaying Chat Messages

### User Message

```python
import streamlit as st

with st.chat_message("user"):
    st.text("Hi")
```

### Assistant Message

```python
with st.chat_message("assistant"):
    st.text("Hello! How can I help you?")
```

👉 Streamlit automatically shows icons for:

* user 👤
* assistant 🤖

---

## 1️⃣1️⃣ Chat Input Box

```python
user_input = st.chat_input("Type here...")
```

* Appears at the bottom
* Press **Enter** to submit
* Value stored in `user_input`

---

## 1️⃣2️⃣ Problem: Messages disappear on new input

### Why?

Streamlit **reruns the entire script** every time:

* User presses Enter
* User interacts with UI

❌ Old messages are lost

---

## 1️⃣3️⃣ Solution: `st.session_state`

### What is Session State?

* A dictionary that **persists across reruns**
* Data stays until the page is refreshed

---

## 1️⃣4️⃣ Initialize Message History

```python
if "message_history" not in st.session_state:
    st.session_state.message_history = []
```

---

## 1️⃣5️⃣ Message Format (Very Important)

Each message is stored as a dictionary:

```python
{
    "role": "user",        # or "assistant"
    "content": "Hello"
}
```

All messages are stored inside a list.

---

## 1️⃣6️⃣ Display Full Chat History

```python
for msg in st.session_state.message_history:
    with st.chat_message(msg["role"]):
        st.text(msg["content"])
```

---

## 1️⃣7️⃣ Add New User Message

```python
if user_input:
    st.session_state.message_history.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.text(user_input)
```

---

## 1️⃣8️⃣ Dummy Chatbot (Copy-Cat Bot)

Assistant replies with the **same message**:

```python
assistant_reply = user_input

st.session_state.message_history.append({
    "role": "assistant",
    "content": assistant_reply
})

with st.chat_message("assistant"):
    st.text(assistant_reply)
```

✅ This confirms:

* UI works
* Memory works
* Session state works

---

## 1️⃣9️⃣ Connecting Streamlit to LangGraph

### Import chatbot object

```python
from langgraph_backend import chatbot
from langchain_core.messages import HumanMessage
```

---

## 2️⃣0️⃣ Calling `chatbot.invoke()`

```python
response = chatbot.invoke(
    {
        "messages": [HumanMessage(content=user_input)]
    },
    config={
        "configurable": {
            "thread_id": "thread-1"
        }
    }
)
```

⚠️ `thread_id` is **required** because:

* We are using a checkpointer
* Needed for memory tracking

---

## 2️⃣1️⃣ Extract AI Response

```python
ai_message = response["messages"][-1].content
```

---

## 2️⃣2️⃣ Display AI Response

```python
st.session_state.message_history.append({
    "role": "assistant",
    "content": ai_message
})

with st.chat_message("assistant"):
    st.text(ai_message)
```

---

## 2️⃣3️⃣ Final Result

🎉 You now have:

* LangGraph-powered chatbot
* Streamlit UI
* Persistent memory
* Real AI responses
* Clean frontend–backend separation

---

## 2️⃣4️⃣ Key Takeaways

* Streamlit reruns scripts → use `session_state`
* Chat UI = `chat_message` + `chat_input`
* LangGraph backend stays clean
* UI logic stays simple
* This design scales easily (RAG, tools, streaming)

---

🚀 **You now have a production-ready foundation for Agentic AI chatbots.**

# 📘 Streaming Responses in a LangGraph Chatbot

(Simple English Notes)

---

## 1️⃣ Background: What We Have Built So Far

In the **Agentic AI using LangGraph** series, we are building a chatbot step by step.

So far, we have already added:

* ✅ Basic chatbot (LLM chat)
* ✅ Short-term memory (chat remembers previous messages)
* ✅ UI using **Streamlit**

Now, we are solving **one important UX problem**.

---

## 2️⃣ The Problem with Long Responses (Without Streaming)

### ❌ Current behavior

When we ask a long question, for example:

> "Write a 500-word blog on cricket"

What happens?

* The screen stays **blank** for 5–10 seconds
* Suddenly, the **entire response appears at once**

### ❌ Why this is bad?

* User has to wait silently
* Feels like the app is frozen
* Large text appearing suddenly is hard to read

👉 This is **not how ChatGPT behaves**

---

## 3️⃣ What is Streaming? (Core Concept)

### ✅ Definition (Simple)

**Streaming means:**

> The model sends output **token by token** as soon as it generates them
> instead of waiting for the full response.

### Two ways an LLM can respond

| Without Streaming                | With Streaming                    |
| -------------------------------- | --------------------------------- |
| Generate full answer → send once | Generate token → send immediately |
| Blank screen for seconds         | Text appears gradually            |
| Poor UX                          | Excellent UX                      |

📌 The typing / typewriter effect you see in ChatGPT = **Streaming**

---

## 4️⃣ Why Streaming is Important (Very Important)

### 🔹 1. Faster perceived response

* Even if full response takes 10 seconds
* User sees output immediately
* App feels alive, not frozen

---

### 🔹 2. Human-like conversation

* Feels like someone is typing
* Builds trust
* Keeps user engaged

---

### 🔹 3. Required for voice & multimodal apps

Example: **Alexa / Voice Assistant**

❌ Without streaming:

* Silence for 10 seconds
* Then sudden speech

✅ With streaming:

* Device starts speaking immediately
* Feels natural

---

### 🔹 4. Much better for long outputs (Code, Blogs)

* Code appearing line-by-line is easier to understand
* Sudden full code dump is confusing

---

### 🔹 5. Saves tokens & money 💰

* User can stop generation midway
* Fewer tokens generated
* Lower API cost (LLMs charge per token)

---

### 🔹 6. Useful for agent progress updates

Example:

> "Booking movie ticket…"

Streaming updates:

* Opening BookMyShow
* Selecting movie
* Selecting seats
* Making payment

👉 User always knows what is happening

---

## 5️⃣ How Streaming Works in LangGraph (Key Idea)

### ❗ One small but powerful change

**Before:**

```python
chatbot.invoke(initial_state, config)
```

**Now:**

```python
chatbot.stream(initial_state, config, stream_mode="messages")
```

### Important difference

* `.invoke()` → returns full result
* `.stream()` → returns a **generator**

---

## 6️⃣ Python Generator (Very Important)

### What is a Generator?

A generator:

* Produces values one at a time
* Uses `yield` instead of `return`

Example:

```python
def demo():
    yield "Hello"
    yield "World"
```

👉 Generators are perfect for **streaming tokens**

---

## 7️⃣ Backend: Streaming from LangGraph

### Calling `.stream()`

```python
from langchain_core.messages import HumanMessage

stream = chatbot.stream(
    {
        "messages": [HumanMessage(content=user_input)]
    },
    config={"configurable": {"thread_id": "1"}},
    stream_mode="messages"
)
```

This returns a **generator**.

Each item contains:

* `message_chunk`
* `metadata`

---

### Printing tokens one by one (Backend test)

```python
for message_chunk, metadata in stream:
    if message_chunk.content:
        print(message_chunk.content, end=" ")
```

✅ Output now appears **token by token**

---

## 8️⃣ Important Note About Backend

👉 **No backend changes are required permanently**

* Backend logic remains the same
* Streaming is mainly handled in **frontend (Streamlit)**

---

## 9️⃣ Frontend: Streaming in Streamlit

Streamlit provides a built-in function:

### ✅ `st.write_stream()`

* Accepts a generator
* Automatically shows **typewriter effect**

---

## 🔟 Streamlit UI Code (Core Change)

### Before (Non-Streaming)

```python
response = chatbot.invoke(...)
st.chat_message("assistant").write(response)
```

---

### After (Streaming)

```python
with st.chat_message("assistant"):
    ai_message = st.write_stream(
        message_chunk.content
        for message_chunk, metadata in chatbot.stream(
            {
                "messages": [HumanMessage(content=user_input)]
            },
            config={"configurable": {"thread_id": "1"}},
            stream_mode="messages"
        )
        if message_chunk.content
    )
```

---

## 1️⃣1️⃣ Saving the Final Response in Session State

After streaming completes:

```python
st.session_state.messages.append({
    "role": "assistant",
    "content": ai_message
})
```

This ensures:

* Chat history is preserved
* Memory works correctly

---

## 1️⃣2️⃣ Common Bug (Very Important)

### ❌ Mistake

```python
HumanMessage(content="What is the recipe to make pasta?")
```

### ✅ Correct

```python
HumanMessage(content=user_input)
```

Otherwise, the chatbot will always respond to the **same hardcoded question**.

---

## 1️⃣3️⃣ Final Result 🎉

Now your chatbot:

* ✅ Streams responses token-by-token
* ✅ Feels like ChatGPT
* ✅ No waiting on blank screen
* ✅ Better UX
* ✅ Works perfectly for long answers & code

---

## 1️⃣4️⃣ Final Summary

### What we learned

* What streaming is
* Why streaming is critical for LLM apps
* How LangGraph streaming works
* How Python generators help
* How to implement streaming in Streamlit

📌 **Streaming is a small feature but gives 10x better user experience**

📘 Resume Chat Feature in LangGraph Chatbot

(Simple English Notes with Code)

1️⃣ What we have built so far (Recap)

In the Agentic AI using LangGraph series, we have been improving a chatbot step by step.

So far, we have added:

✅ Basic chatbot (console-based)
✅ Streamlit UI
✅ Streaming responses (token-by-token output)

👉 Streaming improved user experience because output appears instantly instead of waiting.

2️⃣ What is the goal of this video?

In this video, we add an important real-world feature:

🔄 Resume Chat Feature

Just like ChatGPT, users can:

Start a new chat

Resume old conversations

Each conversation has its own memory

Example:

One chat remembers “My name is Nitesh”

Another chat remembers “My name is Rahul”

3️⃣ Final UI after this feature

The chatbot UI will have two sections:

🖥️ Main Area

Chat with the AI

Messages appear with memory

📂 Sidebar

New Chat button

My Conversations list

Click any conversation to resume it

4️⃣ Important Architecture Decision
❗ No backend changes needed

Our chatbot is built in two parts:

Layer	Tech
Backend	LangGraph
Frontend	Streamlit

👉 Resume Chat is purely a frontend feature
Backend already supports threads & state.

5️⃣ Breaking the feature into small tasks

Instead of coding everything at once, we divide it into small tasks:

Build Sidebar UI

Generate dynamic Thread IDs

Store all thread IDs

Start New Chat

Resume Old Chat

👉 This approach makes coding easy and bug-free

6️⃣ Task 1: Sidebar UI
What we want in sidebar:

Title

New Chat button

My Conversations section

Code (Streamlit)
st.sidebar.title("LangGraph Chatbot")

if st.sidebar.button("New Chat"):
    pass

st.sidebar.header("My Conversations")


✅ Sidebar UI is now visible

7️⃣ Task 2: Dynamic Thread ID generation
❌ Problem

Earlier we used:

thread_id = "thread1"


This fails when multiple chats exist.

✅ Solution: Use UUID
Utility function
import uuid

def generate_thread_id():
    return str(uuid.uuid4())

Store thread ID in session
if "thread_id" not in st.session_state:
    st.session_state.thread_id = generate_thread_id()

Use thread ID in LangGraph config
config = {
    "configurable": {
        "thread_id": st.session_state.thread_id
    }
}

8️⃣ Task 3: Display current thread ID
st.sidebar.text(st.session_state.thread_id)


Now users can see which conversation is active.

9️⃣ Task 4: New Chat functionality
What should happen when user clicks “New Chat”?

✔ Generate new thread ID
✔ Replace old thread ID
✔ Clear message history

Utility function: Reset Chat
def reset_chat():
    st.session_state.thread_id = generate_thread_id()
    st.session_state.message_history = []

Button click logic
if st.sidebar.button("New Chat"):
    reset_chat()


✅ New empty chat opens
✅ Old messages disappear
❌ But old threads are lost (problem)

🔴 Problem Found

When creating a new chat:

Old conversations disappear

Thread IDs are lost

1️⃣0️⃣ Task 5: Store all conversations (Thread List)
Create a list in session
if "chat_threads" not in st.session_state:
    st.session_state.chat_threads = []

Utility function: Add Thread
def add_thread(thread_id):
    if thread_id not in st.session_state.chat_threads:
        st.session_state.chat_threads.append(thread_id)

Add thread on page load
add_thread(st.session_state.thread_id)

Add thread inside reset_chat()
def reset_chat():
    new_id = generate_thread_id()
    st.session_state.thread_id = new_id
    st.session_state.message_history = []
    add_thread(new_id)

1️⃣1️⃣ Show all threads in Sidebar
for tid in st.session_state.chat_threads:
    st.sidebar.text(tid)


✅ All conversation IDs stay visible
✅ Old chats are not lost

1️⃣2️⃣ Make threads clickable (Buttons)
for tid in st.session_state.chat_threads:
    if st.sidebar.button(str(tid)):
        pass


Now threads are clickable.

1️⃣3️⃣ Resume chat: Load old messages
How do we fetch messages from LangGraph?

LangGraph stores state per thread_id.

Fetch state
state = chatbot.get_state({
    "configurable": {"thread_id": thread_id}
})
messages = state.values["messages"]

1️⃣4️⃣ Convert LangGraph messages → UI format

LangGraph format:

HumanMessage

AIMessage

UI format:

{
  "role": "user" | "assistant",
  "content": "text"
}

Utility function: Load Conversation
from langchain_core.messages import HumanMessage

def load_conversation(thread_id):
    state = chatbot.get_state({
        "configurable": {"thread_id": thread_id}
    })
    msgs = state.values["messages"]

    temp_messages = []

    for msg in msgs:
        role = "user" if isinstance(msg, HumanMessage) else "assistant"
        temp_messages.append({
            "role": role,
            "content": msg.content
        })

    st.session_state.message_history = temp_messages
    st.session_state.thread_id = thread_id

1️⃣5️⃣ Connect Resume Logic to Sidebar Button
for tid in reversed(st.session_state.chat_threads):
    if st.sidebar.button(str(tid)):
        load_conversation(tid)


✅ Clicking a thread:

Loads old messages

Restores memory

Sets correct thread ID

1️⃣6️⃣ Final Result (Demo)

✔ Multiple conversations
✔ Each has its own memory
✔ Resume works perfectly
✔ New chat doesn’t destroy old chats

Example:

Chat 1 → “My name is Nitesh”

Chat 2 → “My name is Rahul”

Switching works correctly

1️⃣7️⃣ Small UI Improvement

Show latest chat first

for tid in reversed(st.session_state.chat_threads):
    ...

🧠 Homework for You

Instead of showing raw UUIDs:

👉 Generate human-readable titles like:

“Factorial Code”

“AI Job Crisis Blog”

“Python Swap Program”

(Hint: Use first user message as title)

🔥 Important Limitation (Next Video Topic)

Currently:

Memory is stored in RAM

Page refresh → all chats lost

Why?

We are using InMemory Checkpointer

Next Video:

✅ Connect LangGraph to a database
✅ Persistent conversations
✅ Chats survive refresh

# 📘 LangGraph Chatbot – Database Persistence using SQLite Checkpointer

(Simple English Notes with Code)

---

## 1️⃣ What we have built so far (Recap)

In the previous videos of **Agentic AI using LangGraph**, we built a chatbot step by step.

### ✅ Progress till now

* Basic LangGraph chatbot (console-based)
* UI added using Streamlit
* Streaming responses
* Thread-based conversations

👉 Each thread represents a **separate conversation**.

👉 Users can **switch between past chats**.

### 🧠 Current chatbot features

* Start a new chat
* Resume old conversations
* Ask memory-based questions like:

  * *"What is my name?"*
* Different threads remember different users

---

## 2️⃣ The Big Problem (Very Important)

### ❌ What was wrong?

We were using **InMemorySaver** for memory.

That means:

* All conversations were stored in **RAM**
* When:

  * App stops ❌
  * Page refreshes ❌

👉 **All chats are lost**

### Example

* You say: *"Hi, my name is Nitesh"*
* App restarts
* Bot forgets everything 😢

---

## 3️⃣ Goal of This Video

### ✅ What we want to achieve

* Store conversations **permanently**
* Chats should **not disappear**
* Even after:

  * App restart
  * Browser refresh
  * Multiple days later

👉 **Solution: Database-based persistence**

---

## 4️⃣ LangGraph Persistence Options

LangGraph supports different **Checkpointers**:

| Checkpointer  | Storage    | Use case                 |
| ------------- | ---------- | ------------------------ |
| InMemorySaver | RAM        | Testing only             |
| SQLiteSaver   | SQLite DB  | Learning / Prototyping ✅ |
| PostgresSaver | PostgreSQL | Production               |

👉 In this video, we use **SQLiteSaver**

---

## 5️⃣ Step 1: Install SQLite Checkpointer

This is **not built-in** yet.

```bash
pip install langgraph-checkpoint-sqlite
```

---

## 6️⃣ Backend Changes (Most Important Part)

### 🔹 Replace InMemorySaver

❌ Old:

```python
from langgraph.checkpoint.memory import MemorySaver
checkpointer = MemorySaver()
```

✅ New:

```python
from langgraph.checkpoint.sqlite import SQLiteSaver
import sqlite3
```

---

### 🔹 Create SQLite Database Connection

```python
conn = sqlite3.connect(
    "chatbot.db",
    check_same_thread=False
)
```

#### ❓ Why `check_same_thread=False`?

* SQLite normally allows **single-thread access**
* Our chatbot uses **multiple threads**
* This disables SQLite’s thread restriction

---

### 🔹 Create SQLite Checkpointer

```python
checkpointer = SQLiteSaver(conn)
```

✅ That’s it!

Now LangGraph automatically:

* Stores messages
* Stores state
* Stores checkpoints

---

## 7️⃣ Testing Database Persistence (Backend)

### 🔹 Send a message

```python
response = chatbot.invoke(
    {"messages": [("user", "Hi my name is Nitesh")]},
    config={"configurable": {"thread_id": "thread-1"}}
)

print(response)
```

### 🔹 What happens?

* A file **chatbot.db** is created
* Messages are saved inside the database

---

### 🔹 Restart program & ask again

```python
response = chatbot.invoke(
    {"messages": [("user", "What is my name?")]},
    config={"configurable": {"thread_id": "thread-1"}}
)
```

✅ Output:

```
Your name is Nitesh
```

👉 Memory is restored from database 🎉

---

## 8️⃣ Thread-wise Memory (Very Powerful Feature)

### Thread 1

```python
thread_id = "thread-1"
Hi my name is Nitesh
```

### Thread 2

```python
thread_id = "thread-2"
Hi my name is Rahul
```

### Asking the same question

```text
What is my name?
```

| Thread   | Answer |
| -------- | ------ |
| thread-1 | Nitesh |
| thread-2 | Rahul  |

👉 Same chatbot, **different memories per thread**

---

## 9️⃣ Viewing SQLite Database (Optional but Recommended)

### Best way (VS Code)

1. Install **SQLite Viewer** extension
2. Open `chatbot.db`
3. View:

   * Threads
   * Messages
   * Checkpoints

You’ll observe:

* Multiple checkpoints per thread
* Each execution creates **3 checkpoints**:

  * Start
  * Chat node
  * End

---

## 🔟 Extracting All Existing Threads (Backend)

### ❓ Why needed?

Frontend must:

* Show old threads
* Not start from an empty list

---

### 🔹 Get all checkpoints

```python
checkpoints = checkpointer.list(None)
```

---

### 🔹 Extract unique thread IDs

```python
def retrieve_all_threads():
    all_threads = set()

    for checkpoint in checkpointer.list(None):
        thread_id = checkpoint.config["configurable"]["thread_id"]
        all_threads.add(thread_id)

    return list(all_threads)
```

✅ Returns:

```python
["thread-1", "thread-2"]
```

---

## 1️⃣1️⃣ Frontend Changes (Streamlit)

### ❌ Old behavior

```python
chat_threads = []
```

### ✅ New behavior (Fetch from database)

```python
from langgraph_database_backend import chatbot, retrieve_all_threads

chat_threads = retrieve_all_threads()
```

---

## 1️⃣2️⃣ Final Result (What We Achieved)

### ✅ Features now available

* Persistent chat history
* Thread-based memory
* Database-backed storage

Chats survive:

* Refresh
* Restart
* Days later

### 🧑‍💻 User Experience

* Old chats automatically load
* Conversations resume exactly where left off
* Works just like **ChatGPT**

---

## 1️⃣3️⃣ Key Takeaways

* **Persistence = Game changer**
* SQLite is perfect for:

  * Learning
  * Prototyping
* Thread IDs control memory isolation
* LangGraph handles database logic internally

---

🎉 You have now built a **persistent, production-style chatbot foundation using LangGraph**!

# 📘 LangGraph Chatbot – Observability & Thread-based Tracing using LangSmith

*(Simple English Notes with Code)*

---

## 1️⃣ Recap: Journey So Far (Agentic AI using LangGraph)

Till now in this playlist, we have covered:

### Theory

* What is Agentic AI
* What is LangGraph
* Why LangGraph is needed

### Practical Learning

* LangGraph fundamentals
* Different workflow types
* A real chatbot project

### Chatbot Features Built So Far

✅ GUI (UI for users)

✅ Streaming responses (no waiting for full answer)

✅ Database persistence (chats are not lost after restart)

📌 **Result**

If a user chats today, closes the app, and opens it after days →
👉 Old chats are still available.

---

## 2️⃣ What We Are Adding Today: Observability

### 🔹 What is Observability?

In simple words:

> **Observability = Ability to see what is happening inside your chatbot**

For our chatbot, it means:

* Tracking user messages
* Tracking LLM responses
* Recording token usage
* Measuring latency
* Understanding system behavior internally

---

## 3️⃣ Tool Used for Observability: LangSmith

LangSmith is used to:

* Trace each chatbot interaction
* Debug LLM behavior
* Monitor performance
* Analyze token usage & latency

📌 **Important**

LangSmith works automatically once configured.
👉 No code change needed in chatbot logic initially.

---

## 4️⃣ High-Level Concept: Tracing

Every time a user:

* Sends a message
* Gets a reply from chatbot

➡️ That full interaction is saved as a **TRACE**

A trace contains:

* Input
* Output
* Tokens used
* Execution time
* Node details
* Model used

---

## 5️⃣ Step 1: Create LangSmith Account & API Key

### 🔹 Website

```
https://smith.langchain.com
```

### Steps:

1. Sign up / Login
2. Go to **Settings**
3. Open **API Keys**
4. Click **Create API Key**
5. Copy the key safely

---

## 6️⃣ Step 2: Environment Variable Setup (MOST IMPORTANT)

Create a `.env` file in your project folder.

### ✅ Required Environment Variables

```
LANGSMITH_TRACING=true
LANGSMITH_ENDPOINT=https://api.smith.langchain.com
LANGSMITH_API_KEY=your_api_key_here
LANGSMITH_PROJECT=chatbot-project
```

📌 **Meaning**

* `LANGSMITH_TRACING=true` → enables tracing
* `LANGSMITH_ENDPOINT` → LangSmith backend
* `LANGSMITH_API_KEY` → authentication
* `LANGSMITH_PROJECT` → project name in dashboard

⚠️ Once this is set → tracing starts automatically

---

## 7️⃣ No Code Change Needed (Initial Setup)

After adding env variables:

* Run your chatbot normally
* LangSmith automatically records traces behind the scenes

---

## 8️⃣ What Happens After Running Chatbot?

1. User sends a message
2. Chatbot replies normally
3. LangSmith:

   * Captures a trace
   * Stores it under your project
4. Project appears in LangSmith Dashboard

---

## 9️⃣ Understanding LangSmith Dashboard Structure

### 🔹 Project

Top-level container

Example:

```
chatbot-project
```

### 🔹 Trace

Each user turn = 1 trace

Example:

* User asks: *"Roadmap for AI Engineering"*
* Bot replies

➡️ That = **1 trace**

### 🔹 Trace Details

Inside a trace you can see:

* Node name (Chat node)
* Model used (ChatOpenAI / Cerebras etc.)
* Input text
* Output text
* Token usage (input + output)
* Latency
* Status
* Start & end time

---

## 🔴 Problem Without Threads

If user:

* Opens multiple conversations (threads)
* Switches between them

❌ All traces go into the same list

❌ Conversations get mixed

❌ Hard to analyze user-wise or session-wise chats

---

## ✅ Solution: Thread-based Tracing

LangSmith supports **Threads**.

Each conversation thread:

* Has its own trace group
* Keeps chat history clean & organized

---

## 1️⃣0️⃣ Requirement for Thread Logging

You must explicitly pass **one of these** while invoking the chatbot:

* `thread_id`
* `session_id`
* `conversation_id`

---

## 1️⃣1️⃣ Code Change Required (IMPORTANT)

### 🔹 Old Config (Before)

```python
config = {
    "configurable": {
        "thread_id": session["thread_id"]
    }
}
```

### 🔹 New Config (With Thread Metadata for LangSmith)

```python
config = {
    "configurable": {
        "thread_id": session["thread_id"]
    },
    "metadata": {
        "thread_id": session["thread_id"]
    },
    "run_name": "chat_turn"
}
```

### ✅ What Changed?

| Field                | Purpose                              |
| -------------------- | ------------------------------------ |
| `metadata.thread_id` | Enables thread grouping in LangSmith |
| `run_name`           | Improves trace readability           |

---

## 1️⃣2️⃣ Why `run_name = "chat_turn"`?

Default trace name = **LangGraph** (not informative)

Now:

* Each trace is clearly labeled as **chat_turn**
* Easy to understand: 1 turn = 1 user-message + AI-reply

---

## 1️⃣3️⃣ Result After Thread Integration

LangSmith Dashboard Shows:

✅ Projects
✅ Traces
✅ Threads section

Each thread:

* Represents one conversation
* Contains ordered turns
* Shows human ↔ AI messages cleanly

---

## 1️⃣4️⃣ Multiple Conversations Example

### Conversation 1

```
Hi
My name is Nitesh
Who created you?
```

➡️ Stored as **Thread 1**
➡️ Contains **3 traces**

---

### Conversation 2

```
Hi my name is Rahul
What is roadmap to study AI?
```

➡️ Stored as **Thread 2**
➡️ Completely separate & clean

---

## 1️⃣5️⃣ Benefits of Thread-based Observability

✅ Clean conversation tracking
✅ Easy debugging
✅ Easy production monitoring
✅ Understand user behavior
✅ Analyze latency & cost per conversation

✅ Essential for:

* Tools
* RAG
* MCP
* Multi-agent systems

---

## 1️⃣6️⃣ Why This Matters in Production

When chatbot is live:

* You cannot guess bugs
* You must observe behavior
* You must trace failures

📌 **LangSmith = Production-grade observability**

---

## 🔚 Final Summary

| Feature              | Status |
| -------------------- | ------ |
| UI                   | ✅      |
| Streaming            | ✅      |
| Persistence          | ✅      |
| Observability        | ✅      |
| Thread-based tracing | ✅      |

🚀 **Your chatbot is now production-ready**

# 📘 LangGraph Chatbot – Adding Tools (Actions)

*(Simple English Notes with Code)*

---

## 1️⃣ Recap: What We Have Built So Far

We are building an **Agentic AI Chatbot using LangGraph**.

Till now, our chatbot has:

* ✅ GUI (Streamlit UI)
* ✅ Short-term memory
* ✅ Database persistence
* ✅ Streaming responses

### ❌ Current Limitation

The chatbot can **only talk**.

It cannot perform actions like:

* Calculations
* Internet search
* Fetch stock prices

---

## 2️⃣ Goal of This Video

👉 **Add ACTION capabilities using Tools**

After this:

* Chatbot can chat normally
* Chatbot can perform tasks using tools

### Tools we will add:

1️⃣ Calculator tool (numerical calculations)

2️⃣ Internet search tool (DuckDuckGo)

3️⃣ Stock price tool (real-time price)

---

## 3️⃣ What Are Tools? (Simple Explanation)

A **Tool** is a function that the chatbot can call to perform real work.

Examples:

* Calculator → math
* Search → internet
* Stock API → live prices

📌 The **LLM decides when to call a tool**.

---

## 4️⃣ High-Level Workflow (Before vs After)

### ❌ Old Workflow (Chat only)

```
START → Chat Node → END
```

### ✅ New Workflow (Chat + Actions)

```
START → Chat Node
          |
          |-- Normal chat → END
          |
          |-- Tool needed → Tool Node → Chat Node → END
```

---

## 5️⃣ Two NEW Important Concepts

### 🔹 1. ToolNode

**ToolNode** is a **pre-built LangGraph node**.

It:

* Holds all tools
* Executes the correct tool automatically

📌 Think of it as a **Tool Executor**.

---

### 🔹 2. tools_condition

`tools_condition` decides:

* Should we continue chatting?
* OR should we call a tool?

It creates a **conditional flow** in the graph.

---

## 6️⃣ Why Tool Output Must Go Back to LLM

### ❌ Problem (Without Loop)

* Tool returns raw JSON
* Output is not user-friendly
* Multi-step reasoning is not possible

Example:

```
"Apple stock price → calculate cost of 50 shares"
```

❌ Impossible without a loop

---

### ✅ Solution: Create a Loop

```
Chat Node → Tool Node → Chat Node → Tool Node → Chat Node → END
```

With this loop, the LLM:

* Reads tool output
* Decides the next step
* Formats the final user-friendly answer

---

## 7️⃣ Required Imports

```python
from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode, tools_condition

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool

from langchain_community.tools import DuckDuckGoSearchRun
from dotenv import load_dotenv
```

---

## 8️⃣ Create the LLM

```python
load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini")
```

---

## 9️⃣ Define Tools

### 🔹 Tool 1: DuckDuckGo Search (Prebuilt)

```python
search_tool = DuckDuckGoSearchRun()
```

---

### 🔹 Tool 2: Calculator (Custom Tool)

```python
@tool
def calculator(a: int, b: int, operation: str) -> int:
    """
    Performs basic arithmetic operations between two numbers.
    operation can be add, subtract, multiply, divide
    """
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        return a / b
    else:
        return "Invalid operation"
```

📌 **Docstring is VERY IMPORTANT** – the LLM reads it to decide when to use this tool.


# 📘 Agentic AI using LangGraph – MCP (Model Context Protocol)

---

## 1️⃣ Playlist Status & Recap

This video resumes the **Agentic AI using LangGraph** playlist after a long pause.

### What we have covered so far (18 videos)

#### Foundations

* What is Agentic AI
* Difference between Generative AI vs Agentic AI
* LangChain vs LangGraph

#### LangGraph Core Concepts

* Nodes
* State
* Edges
* Execution flow

#### Workflow Types

* Sequential workflow
* Parallel workflow
* Conditional workflow
* Iterative (looping) workflow

#### Chatbot Project (Step-by-step)

* Basic LangGraph chatbot
* UI using Streamlit
* Streaming responses
* Resume chat (threads)
* Database persistence (SQLite)
* Observability using LangSmith
* Tools (Calculator, Web Search, Stock Price)

---

## 2️⃣ Today’s Topic: MCP (Model Context Protocol)

### Why this video exists

The playlist was paused mainly because the creator was working deeply on **MCP**, which has become very popular in the last **6 months**.

Now, **MCP is being integrated into the chatbot**.

---

## 3️⃣ What is MCP? (Very Simple Explanation)

**MCP = Improved and standardized way to connect tools with LLM applications**

You can think of MCP as:

> A better, cleaner, future‑proof replacement for traditional *tool calling*

### Short definition

* MCP is **not a completely new idea**
* It is a **standardized way** to connect tools
* It clearly separates:

  * Tool logic
  * Client (chatbot) logic

---

## 4️⃣ Problem with Normal Tools (Important)

### Current tool approach

In LangChain / LangGraph, tools are:

* Library‑based tools (e.g., DuckDuckGo search)
* User‑defined tools (custom Python functions)

### Example tools already used

* Search tool
* Calculator tool
* Stock price tool

---

## 5️⃣ Example Problem: GitHub Integration

Suppose:

* Your chatbot already has **3 tools**
* Manager asks you to add **GitHub integration**
* Chatbot should answer questions about:

  * Pull Requests
  * Commits
  * Files

### What do you do today?

You must:

* Write custom GitHub tools
* Handle:

  * Authentication
  * Headers
  * API URLs
  * JSON parsing

### Example: GitHub Pull Request Tool (Conceptual)

```python
def get_pull_requests(owner, repo, state="open", limit=5):
    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}"
    }
    url = f"https://api.github.com/repos/{owner}/{repo}/pulls"
    response = requests.get(url, headers=headers)
    return response.json()
```

---

## 6️⃣ The BIG Problem: Brittleness

### Why this approach is dangerous

* GitHub updates API versions
* URLs change
* JSON fields change
* Attribute names change

### Example changes

```
/pulls  → /pull_requests
title   → title_name
user    → user_name
```

### 💥 Result

* Chatbot crashes
* All tools break
* You must update code everywhere

---

## 7️⃣ Scaling Problem (N × M Explosion)

If:

* **N** tools
* **M** chatbots

Then:

```
Maintenance cost = N × M
```

If you integrate:

* GitHub
* Gmail
* Slack
* Jira

👉 You spend more time **maintaining tools** than building features

---

## 8️⃣ How MCP Solves This

### Core MCP Idea: Separation of Concerns

| Client (Chatbot) | Server (Tools)      |
| ---------------- | ------------------- |
| Only config code | All tool logic      |
| Stable           | Can change          |
| No API logic     | Handles API changes |

### Key Rule

* Tool code stays on **MCP server**
* Client code **NEVER changes**

---

## 9️⃣ MCP Architecture (Simple)

### MCP Server

* Owns tool logic
* Handles APIs
* Handles version changes

### MCP Client

* Just connects via config
* Auto‑discovers tools

---

## 🔟 From Tool Code → MCP Config Code

### Old way (lots of code)

* Multiple Python functions
* API handling
* Error handling

### MCP way (only config)

```python
client = MultiServerMCPClient(
    servers={
        "math": {
            "transport": "stdio",
            "command": ["python", "main.py"]
        }
    }
)
```

✅ No tool logic on client side

---

## 1️⃣1️⃣ Why Async is Required

### Important clarification

* MCP libraries are **async‑only**
* Therefore, your **LangGraph chatbot must be async**

---

## 1️⃣2️⃣ Converting LangGraph Chatbot to Async

### Key changes

#### 1. Make chat node async

```python
async def chat_node(state):
    response = await llm.ainvoke(state["messages"])
    return {"messages": [response]}
```

#### 2. Use `ainvoke` instead of `invoke`

```python
result = await chatbot.ainvoke(input_data)
```

#### 3. Async entry point

```python
if __name__ == "__main__":
    asyncio.run(main())
```

---

## 1️⃣3️⃣ Why Async Matters (Intuition)

### Sequential (slow)

* Weather API → wait
* Cricket score API → wait

### Async (fast)

* Weather API ⏳
* Cricket score API ⏳
* Both run together

👉 Faster, concurrent execution

---

## 1️⃣4️⃣ Building MCP Client in LangGraph

### Install library

```bash
pip install langchain-mcp-adapters
```

or

```bash
uv add langchain-mcp-adapters
```

---

## 1️⃣5️⃣ Connecting to Local MCP Server (Math Server)

```python
from langchain_mcp_adapters.client import MultiServerMCPClient

client = MultiServerMCPClient(
    servers={
        "math": {
            "transport": "stdio",
            "command": ["python", "main.py"]
        }
    }
)
```

### Fetch tools from server

```python
tools = await client.get_tools()
llm = llm.bind_tools(tools)
```

✔ Tools are auto‑discovered
✔ No manual tool definition

---

## 1️⃣6️⃣ Adding a Remote MCP Server (Expense Tracker)

```python
client = MultiServerMCPClient(
    servers={
        "math": {...},
        "expense": {
            "transport": "streamable_http",
            "url": "https://expense-mcp-server.com"
        }
    }
)
```

---

## 1️⃣7️⃣ What the Expense MCP Server Provides

* add_expense
* list_expenses
* summarize_expenses

💡 No expense logic written in chatbot
💡 Everything comes from MCP server

---

## 1️⃣8️⃣ Example Usage (No Client Code Change)

* Add an expense of ₹500 for Udemy course on 10th Nov
* List my expenses for November
* Summarize my expenses

All handled automatically via MCP 🎯

---

## 1️⃣9️⃣ Mixing Tools + MCP (Allowed)

You can:

* Use normal tools (search, stock)
* Use MCP servers (math, expense)

👉 Mixing is allowed
👉 MCP is recommended for future‑proofing

---

## 2️⃣0️⃣ Real Project Notes (Important)

### Tech stack issues

* MCP → async only
* LangGraph → sync + async
* Streamlit → mostly sync
* SQLite → sync

### Fixes used

* Converted backend to async
* Used `aiosqlite` instead of `sqlite`
* Used async streaming (`astream`)

⚠️ **Not production‑ready**

### For production

* FastAPI backend
* React / Next.js frontend

---

## 2️⃣1️⃣ Why MCP Is the Future

* Industry standard
* Used by ChatGPT internally
* Stable
* Scalable
* No client maintenance

---

## 2️⃣2️⃣ What’s Next?

➡️ **Next video topic**

* RAG (Retrieval Augmented Generation)
* Ask questions on internal documents
* PDFs
* Knowledge bases

---

## ✅ Final Takeaway

**Tools = brittle**
**MCP = robust, scalable, future‑proof**

If you are building **serious agentic AI systems**, MCP is the right choice.


---

### 🔹 Tool 3: Stock Price Tool (Custom API Tool)

```python
@tool
def get_stock_price(symbol: str) -> dict:
    """
    Returns the current stock price of a company using Alpha Vantage API.
    """
    import requests, os

    api_key = os.getenv("ALPHA_VANTAGE_API_KEY")
    url = (
        "https://www.alphavantage.co/query"
        f"?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}"
    )

    response = requests.get(url).json()
    return response
```

---

## 🔟 Bind Tools to LLM

```python
tools = [search_tool, calculator, get_stock_price]
llm_with_tools = llm.bind_tools(tools)
```

---

## 1️⃣1️⃣ Define State

```python
from typing import TypedDict, List
from langchain_core.messages import BaseMessage

class State(TypedDict):
    messages: List[BaseMessage]
```

---

## 1️⃣2️⃣ Chat Node

```python
def chat_node(state: State):
    response = llm_with_tools.invoke(state["messages"])
    return {"messages": state["messages"] + [response]}
```

---

## 1️⃣3️⃣ Create ToolNode

```python
tool_node = ToolNode(tools)
```

---

## 1️⃣4️⃣ Build the Graph

```python
graph = StateGraph(State)

graph.add_node("chat", chat_node)
graph.add_node("tools", tool_node)

graph.add_edge(START, "chat")

graph.add_conditional_edges(
    "chat",
    tools_condition,
    {
        "tools": "tools",
        END: END
    }
)

# 🔁 IMPORTANT LOOP
graph.add_edge("tools", "chat")

chatbot = graph.compile()
```

---

## 1️⃣5️⃣ Test the Workflow

### Normal Chat

```python
chatbot.invoke({
    "messages": [HumanMessage(content="Hello")]
})
```

### Calculator Tool

```python
chatbot.invoke({
    "messages": [HumanMessage(content="What is the product of 2 and 3?")]
})
```

### Stock Tool (Multi-step Reasoning)

```python
chatbot.invoke({
    "messages": [
        HumanMessage(content="What is the stock price of Apple and cost of 50 shares?")
    ]
})
```

---

## 1️⃣6️⃣ Why This Design Is Powerful

* ✅ Clean, user-friendly output
* ✅ Multi-step reasoning
* ✅ Unlimited tools possible
* ✅ True Agentic behavior

---

## 1️⃣7️⃣ Fix Streaming Issue (Frontend)

### ❌ Problem

Tool messages were also being streamed.

### ✅ Solution: Stream only AI messages

```python
from langchain_core.messages import AIMessage

if isinstance(message, AIMessage):
    st.write_stream(message.content)
```

---

## 1️⃣8️⃣ Optional UX Improvement

* ✔ Show status container in Streamlit
* ✔ Display which tool is being used
* ✔ Improves user trust & transparency

---

## 1️⃣9️⃣ Final Result

Your chatbot can now:

* Chat normally 🧠
* Perform calculations 🧮
* Search internet 🌐
* Fetch live stock prices 📈
* Chain multiple tools automatically 🔁

* # 📘 LangGraph Chatbot → RAG Chatbot (Simple English Notes)

---

## 1️⃣ Recap: What we have built so far

In the **Agentic AI using LangGraph** playlist, we are building **one chatbot as a running project**.

So far, we have added these features step by step:

* ✅ Basic chatbot (LLM chat)
* ✅ UI using Streamlit
* ✅ Streaming responses (token by token)
* ✅ Chat persistence (resume chat)
* ✅ Observability using LangSmith
* ✅ Tools (Calculator, Web Search, Stock Price)
* ✅ MCP (Model Context Protocol)

Each new feature helped us learn **one new LangGraph concept**.

---

## 2️⃣ Goal of this Video: Convert Chatbot into a RAG Chatbot

### ❌ Before

* Chatbot could only answer using LLM knowledge
* Could NOT answer questions from your documents

### ✅ After (RAG)

* Upload a PDF / document
* Ask questions based on that document
* Tools still work (calculator, stock price, etc.)

📌 **Result → Multi-Utility Chatbot**

---

## 3️⃣ What is RAG? (Quick Recap)

**RAG = Retrieval Augmented Generation**

**Meaning:**

> Give extra context (documents) to the LLM while answering questions.

---

## 4️⃣ Why do we need RAG?

### 🔹 Reason 1: Outdated Knowledge

* LLMs have a knowledge cutoff
* For latest info → external data is needed
* ChatGPT itself uses RAG + Web Search

### 🔹 Reason 2: Private Data

LLMs do NOT know:

* Your PDFs
* Company documents
* Personal files
* Internal reports

📌 **RAG allows:**

> Connecting private documents with LLM safely

### 🔹 Reason 3: Hallucination

* LLMs sometimes give confident but wrong answers
* Example: fake research paper links

📌 **RAG helps by:**

* Forcing LLM to answer only from given context
* Reduces hallucination

---

## 5️⃣ Core Idea of RAG (Very Important)

### 🔹 In-Context Learning

LLM answers based on:

* Your question
* Extra context (retrieved documents)
* Its own language ability

### ❌ Wrong approach

* Paste full book / full codebase → ❌ Token limit exceeded

### ✅ Correct approach

* Retrieve only relevant parts
* Send filtered context to LLM

---

## 6️⃣ High-Level RAG Architecture

### Step-by-step Flow

```
Document → Split → Embed → Store → Retrieve → Prompt → Answer
```

### Detailed Explanation

1️⃣ Load document (PDF, text, web page)
2️⃣ Split document into small chunks
3️⃣ Generate embeddings for each chunk
4️⃣ Store embeddings in a vector database
5️⃣ User asks a question
6️⃣ Question is embedded
7️⃣ Retriever finds most similar chunks
8️⃣ Retrieved chunks + question sent to LLM
9️⃣ LLM generates final answer

---

## 7️⃣ Libraries Used

* langchain
* langgraph
* langchain-openai
* faiss-cpu
* pypdf
* streamlit

---

## 8️⃣ Step 1: Load PDF Document

```python
from langchain.document_loaders import PyPDFLoader

loader = PyPDFLoader("intro_to_ml.pdf")
documents = loader.load()
```

---

## 9️⃣ Step 2: Split Document into Chunks

```python
from langchain.text_splitter import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = text_splitter.split_documents(documents)
```

📌 **Chunking is important to:**

* Maintain context
* Avoid token overflow

---

## 🔟 Step 3: Generate Embeddings

```python
from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small"
)
```

---

## 1️⃣1️⃣ Step 4: Store in Vector Database (FAISS)

```python
from langchain.vectorstores import FAISS

vectorstore = FAISS.from_documents(
    chunks,
    embedding=embeddings
)
```

---

## 1️⃣2️⃣ Step 5: Create Retriever

```python
retriever = vectorstore.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 4}
)
```

📌 **Retriever returns top-4 most relevant chunks**

---

## 1️⃣3️⃣ Testing Retriever (Important Demo)

```python
docs = retriever.invoke("What is a decision tree?")
len(docs)
```

**Output → 4**

Each item contains:

* page_content
* metadata

---

## 1️⃣4️⃣ Wrap RAG as a Tool (Very Important)

```python
from langchain.tools import tool

@tool
def rag_tool(query: str):
    """
    Use this tool when the user asks questions
    based on uploaded documents.
    """
    docs = retriever.invoke(query)

    context = [doc.page_content for doc in docs]
    metadata = [doc.metadata for doc in docs]

    return {
        "query": query,
        "context": context,
        "metadata": metadata
    }
```

📌 **RAG is treated as just another tool**

---

## 1️⃣5️⃣ Bind Tools to LLM

```python
tools = [rag_tool, calculator_tool, stock_price_tool]

llm = llm.bind_tools(tools)
```

---

## 1️⃣6️⃣ LangGraph Nodes

### 🔹 Chat Node

* Decides whether a tool is needed

### 🔹 Tool Node

* Executes RAG tool

```python
from langgraph.graph import StateGraph

graph = StateGraph(ChatState)

graph.add_node("chat", chat_node)
graph.add_node("tools", tool_node)

graph.add_edge("chat", "tools")
graph.add_edge("tools", "chat")

graph.set_entry_point("chat")

app = graph.compile()
```

---

## 1️⃣7️⃣ Full Chat Flow

```
User Question
   ↓
Chat Node (decision)
   ↓
RAG Tool (retrieve docs)
   ↓
Chat Node (final answer)
   ↓
End
```

---

## 1️⃣8️⃣ Example Query

```python
app.invoke({
    "messages": [
        ("human", "Using the PDF, explain how to split a node in a decision tree")
    ]
})
```

⏱️ Takes **~8–9 seconds**
(because retrieval + LLM processing)

---

## 1️⃣9️⃣ Observability with LangSmith

LangSmith shows:

* Chat node execution
* Tool invocation
* Retrieved chunks
* Final response

📌 **Visual Flow:**

```
Chat → Tool → Chat
```

---

## 2️⃣0️⃣ Integrating RAG into Existing Project

### 🆕 New Files Added

* `langgraph_rag_backend.py`
* `streamlit_rag_frontend.py`

### 🔹 Backend Changes

* Created `ingest_pdf()` function
* Added RAG tool with other tools

### 🔹 Frontend Changes

* PDF upload option in sidebar
* Minor thread handling updates

---

## 2️⃣1️⃣ Key Takeaway

* ✅ RAG in LangGraph is very simple
* ✅ Treat RAG as a tool
* ✅ Same agent architecture
* ✅ Production-ready design

---

## 2️⃣2️⃣ What’s Next?

* More LangGraph concepts
* Advanced agents
* Agent orchestration
* Real-world Agentic AI systems

---

## 🎯 Final Summary (One Line)

> **If you know tools in LangGraph, RAG is just another tool.**
>
> 📘 Human-in-the-Loop (HITL) in Agentic AI using LangGraph

(Simple English Notes with Examples & Code)

1️⃣ What is this video about?

In this video, we learn a very important concept used in real-world Agentic AI systems:

👉 HITL – Human in the Loop

This concept becomes mandatory when you build serious AI agents like:

Chatbots

Payment agents

Booking systems

Customer support bots

Tool-using AI systems

2️⃣ What is HITL (Human in the Loop)?

Simple definition:

HITL is a design approach where a human participates at important decision points in an AI workflow.

Instead of letting AI do everything automatically, we pause, ask a human, and continue only after approval.

In short:

AI works autonomously ✅

But critical decisions need human approval ✅

3️⃣ Why Agentic AI Needs Human Oversight

Agentic AI systems are created for autonomy.

Example: Customer Support

Companies like:

Swiggy

Zomato

Amazon

Receive thousands of repetitive requests:

“Order not delivered”

“Refund not received”

These can be handled by AI agents → saves human effort

❌ Problem with Full Autonomy

Current LLMs are not perfect:

They can misunderstand user intent

They can hallucinate

They can make wrong assumptions

So we cannot fully trust AI for:

Payments

Bookings

Deleting data

Sending important emails

👉 That’s why HITL is needed

4️⃣ Real-World HITL Example – Flight Booking
Without HITL ❌

User:

“Book my flight ticket”

AI:

Searches flights

Selects one

Books it

Makes payment ❌

⚠️ Risky and dangerous

With HITL ✅

Flow:

AI searches flights

AI shows best options

AI asks:

“Should I book this flight?”

Human confirms

Ticket is booked

👉 Human judgment controls final action

5️⃣ Core Reasons Why HITL Exists
🔹 Reason 1: Accuracy

LLMs can:

Misinterpret queries

Fail on ambiguous inputs

Example:

User says:

“Book flight for next Friday”

Ambiguity:

This Friday?

Next week’s Friday?

👉 HITL asks:

“Which Friday do you mean?”

🔹 Reason 2: Accountability (Very Important)

AI cannot be blamed
Humans can be held responsible

Example: Gmail Smart Reply

AI generates email reply

Gmail asks user to review

User approves

Then email is sent

👉 Accountability stays with the human

6️⃣ Benefits of HITL in Agentic Systems
✅ 1. Better Accuracy

Human corrects AI mistakes

✅ 2. Improved Safety

Example:

AI wants to delete files

Human confirms first

✅ 3. Ethical Alignment

AI may generate:

Cold replies

Emotionless responses

Human can add:

Empathy

Tone

Company values

✅ 4. Better User Experience

Human + AI synergy = best output

7️⃣ Common HITL Patterns in AI Systems
🔹 1. Action Approval Pattern (Most Common)

Human approval before:

Payments

Sending emails

Deleting files

Booking tickets

🔹 2. Output Review / Edit Pattern

Example:

Blog writing agent

Research agent

Flow:

AI generates draft

Human reviews

Approves or edits

Then publishes

🔹 3. Ambiguity Clarification Pattern

If AI is confused:

It asks the human

Example:

“Do you mean this Friday or next Friday?”

🔹 4. Escalation Pattern

AI gives up and hands control to human

Example:

Customer support chatbot

“Would you like to talk to a human agent?”

8️⃣ HITL from a LangGraph Perspective

LangGraph supports HITL using two core concepts:

🔹 1. interrupt()

Pauses graph execution

Sends message to frontend

Saves current state

🔹 2. Command(resume=...)

Resumes execution

Continues from same node

Uses human input

9️⃣ Conceptual HITL Workflow (LangGraph)

Example: Social Media Tweet Agent

Workflow:

START
 → Research Tweet
 → Generate Draft
 → ❗ INTERRUPT (Ask Human)
 → Post Tweet
 → END

🔟 What Happens During interrupt()?

When LangGraph hits interrupt():

Execution pauses

Current state is saved (via checkpointer)

Message is sent to frontend

Human responds

Graph resumes from same point

1️⃣1️⃣ Basic HITL Code Example (Simple)
Scenario:

Before sending a question to LLM, ask human:

“Do you really want to ask this?”

🔹 HITL Chat Node
from langgraph.types import interrupt
from langchain.schema import AIMessage

def chat_node(state):
    decision = interrupt({
        "type": "approval",
        "reason": "User wants to ask LLM a question",
        "question": state["messages"][-1].content,
        "instruction": "Approve or reject (yes/no)"
    })

    if decision["approved"] == "no":
        return {"messages": [AIMessage(content="Not approved")]}

    response = llm.invoke(state["messages"])
    return {"messages": [response]}

🔹 Graph Definition
from langgraph.graph import StateGraph, END
from langgraph.checkpoint.memory import MemorySaver

graph = StateGraph(ChatState)

graph.add_node("chat", chat_node)
graph.add_edge("start", "chat")
graph.add_edge("chat", END)

checkpointer = MemorySaver()
app = graph.compile(checkpointer=checkpointer)

🔹 First Invoke (Pause Happens)
result = app.invoke(
    {"messages": [HumanMessage(content="Explain gradient descent")]},
    config={"thread_id": "1"}
)


You will receive an interrupt message.

🔹 Resume After Human Input
from langgraph.types import Command

result = app.invoke(
    Command(resume={"approved": "yes"}),
    config={"thread_id": "1"}
)


Graph resumes from same node 🎯

1️⃣2️⃣ Advanced Example – HITL in Tool-Using Chatbot
Tools:

get_stock_price

purchase_stock (risky action)

❌ Without HITL

User:

“Purchase 10 stocks”

AI:

Directly buys ❌

No confirmation

No accountability

✅ With HITL

AI asks:

“Approve buying 10 shares of Apple? (yes/no)”

Only proceeds after approval

🔹 HITL Inside Tool
def purchase_stock(company, quantity):
    decision = interrupt(
        f"Approve buying {quantity} shares of {company}? (yes/no)"
    )

    if decision.lower() != "yes":
        return "Purchase cancelled"

    return f"Successfully purchased {quantity} shares of {company}"

🔹 Frontend / CLI Logic
if interrupt_msg:
    print(interrupt_msg)
    user_decision = input("yes/no: ")

    app.invoke(
        Command(resume=user_decision),
        config={"thread_id": thread_id}
    )

1️⃣3️⃣ Key Takeaways

HITL is mandatory for real-world AI

LangGraph supports HITL natively

Core concepts:

interrupt()

Command(resume=...)

HITL improves:

Accuracy

Safety

Accountability

User trust

✅ Final Summary

HITL = AI power + Human judgment

LangGraph makes HITL:

Simple

Intuitive

Production-ready

You’ll use this a lot in:

RAG systems

Tool-using agents

Finance apps

Enterprise chatbots

# 📘 Subgraphs in Agentic AI using LangGraph

(Simple English Notes with Code)

---

## 1️⃣ Introduction: What are Subgraphs?

Till now, we have learned that:

* Any AI workflow can be represented as a **Graph**
* A graph contains:

  * **Nodes** → tasks (LLM call, tool call, retrieval, etc.)
  * **Edges** → execution flow

### 🔹 Core Idea of Subgraphs

👉 A **Subgraph** is a graph inside another graph.

Normally:

* One node = one task

With subgraphs:

* One node itself can be a **complete graph**

📌 **Definition (Simple)**

A Subgraph is a graph that is embedded and executed as a node inside another graph.

* **Big Graph** = Parent Graph
* **Small internal Graph** = Subgraph

---

## 2️⃣ Why Subgraphs Are Needed in Real GenAI Systems

### 🔹 Simple GenAI App (Beginner Level)

```
User Question → LLM → Answer
```

Simple and easy.

### 🔹 Real-World GenAI Apps (Advanced Level)

Real systems usually include:

* Tools
* RAG (Retrieval Augmented Generation)
* Conditional routing
* Retry logic
* Memory
* HITL (Human-in-the-loop)
* Evaluation
* Guardrails
* Deployment & Monitoring

👉 All this makes the graph **very complex**.

---

## 3️⃣ Real Example: Software Development Agent

Imagine building an **AI Software Development Agent**.

Tasks involved:

* Planning (Team Lead)
* Backend Development
* Frontend Development
* Testing
* Code Review
* DevOps (Deploy & Monitor)

If everything is placed inside **one graph**:

❌ Too complex
❌ Hard to debug
❌ Hard to maintain

---

## 4️⃣ Solution: Multi-Agent Architecture using Subgraphs

Break one big agent into multiple small agents.

| Agent          | Role               |
| -------------- | ------------------ |
| Planning Agent | Planning           |
| Coding Agent   | Backend / Frontend |
| Testing Agent  | Testing            |
| Review Agent   | Code Review        |
| DevOps Agent   | Deployment         |

👉 Each agent = **One Subgraph**

Each subgraph has:

* Its own tools
* Its own memory
* Its own retry logic
* Its own guardrails

---

## 5️⃣ Core Benefits of Subgraphs

### ✅ 1. Modularity

* Break big systems into small logical units
* Works like **functions** in programming

### ✅ 2. Reusability

* Same Coding Agent can be reused for:

  * Backend
  * Frontend

### ✅ 3. Maintainability

* Easier debugging
* Easier upgrades
* Easier testing

---

## 6️⃣ LangGraph-Specific Benefits of Subgraphs

### 🔹 1. Failure Isolation

* If one subgraph fails → others continue
* One failure does **NOT** crash the whole system

### 🔹 2. State Separation

Without subgraphs:

* One giant shared state ❌
* State conflicts ❌

With subgraphs:

* Each subgraph has its own state
* No state pollution

### 🔹 3. Observability (Tracing)

Using **LangSmith**:

* Trace each subgraph separately
* Measure:

  * Token usage
  * Latency
  * Errors per agent

📌 Example:

* Trace Coding Agent separately
* Trace Testing Agent separately

---

## 7️⃣ Ways to Implement Subgraphs in LangGraph

LangGraph provides **two mechanisms**:

### 🔹 Method 1: Invoke a Subgraph from a Node

* Parent graph and subgraph have **separate states**
* Subgraph is invoked inside a node function
* High isolation

### 🔹 Method 2: Add Subgraph as a Node

* Subgraph itself becomes a node
* Parent and subgraph **share the same state**
* Simple design

---

## 8️⃣ Practical Example: English → Hindi Translation

### 🧠 Use Case

1. User asks a question
2. LLM generates answer in English
3. Another LLM translates it into Hindi

---

## ✅ METHOD 1: Subgraph with Isolated State

### Step 1️⃣ Translation Subgraph

#### Subgraph State

```python
from typing import TypedDict

class TranslationState(TypedDict):
    input_text: str
    translated_text: str
```

#### Translation Node

```python
def translate_node(state: TranslationState):
    prompt = f"Translate this text to Hindi:\n{state['input_text']}"
    response = llm.invoke(prompt)

    return {
        "translated_text": response.content
    }
```

#### Build Translation Subgraph

```python
from langgraph.graph import StateGraph, START, END

translation_graph = StateGraph(TranslationState)

translation_graph.add_node("translate", translate_node)
translation_graph.add_edge(START, "translate")
translation_graph.add_edge("translate", END)

translation_subgraph = translation_graph.compile()
```

---

### Step 2️⃣ Parent Graph

#### Parent State

```python
class ParentState(TypedDict):
    question: str
    english_answer: str
    hindi_answer: str
```

#### Generate Answer Node

```python
def generate_answer(state: ParentState):
    response = llm.invoke(state["question"])
    return {"english_answer": response.content}
```

#### Translate Node (Invokes Subgraph)

```python
def translate_answer(state: ParentState):
    result = translation_subgraph.invoke({
        "input_text": state["english_answer"]
    })

    return {
        "hindi_answer": result["translated_text"]
    }
```

#### Build Parent Graph

```python
parent_graph = StateGraph(ParentState)

parent_graph.add_node("generate", generate_answer)
parent_graph.add_node("translate", translate_answer)

parent_graph.add_edge(START, "generate")
parent_graph.add_edge("generate", "translate")
parent_graph.add_edge("translate", END)

app = parent_graph.compile()
```

#### Run

```python
result = app.invoke({
    "question": "What is Artificial Intelligence?"
})

print(result)
```

---

## ✅ METHOD 2: Subgraph as a Node (Shared State)

### Shared State

```python
class SharedState(TypedDict):
    question: str
    english_answer: str
    hindi_answer: str
```

### Subgraph (Uses Shared State)

```python
def translate_node(state: SharedState):
    prompt = f"Translate this to Hindi:\n{state['english_answer']}"
    response = llm.invoke(prompt)

    return {"hindi_answer": response.content}
```

### Build Translation Subgraph

```python
translation_graph = StateGraph(SharedState)
translation_graph.add_node("translate", translate_node)
translation_graph.add_edge(START, "translate")
translation_graph.add_edge("translate", END)

translation_subgraph = translation_graph.compile()
```

### Parent Graph (Subgraph as Node)

```python
parent_graph = StateGraph(SharedState)

parent_graph.add_node("generate", generate_answer)
parent_graph.add_node("translator", translation_subgraph)

parent_graph.add_edge(START, "generate")
parent_graph.add_edge("generate", "translator")
parent_graph.add_edge("translator", END)

app = parent_graph.compile()
```

---

## 9️⃣ Comparison Summary

| Feature    | Method 1 | Method 2 |
| ---------- | -------- | -------- |
| State      | Separate | Shared   |
| Isolation  | High     | Low      |
| Simplicity | Medium   | High     |
| Control    | More     | Less     |

---

## 🔟 Best Practices & Extra Features

### ✅ Persistence

* Add **checkpointer only to the parent graph**
* Subgraphs automatically inherit persistence

### ✅ Streaming

* Subgraphs fully support streaming outputs

### ✅ Observability

* Each subgraph can be traced independently in **LangSmith**

---

## 🔚 Final Takeaway

Subgraphs are **mandatory** for complex Agentic AI systems.

They enable:

* Multi-agent architecture
* Clean design
* Scalable workflows

👉 **Future AI systems = Graphs of Graphs** 🚀


📘  Why Memory Matters in GenAI

( First Principles Approach)

1️⃣ Why Memory is Extremely Important in GenAI

If you want to build real GenAI or Agentic AI applications, memory is not optional.

Think about:

Chatbots (ChatGPT, Gemini)

AI agents

Personal assistants

❌ Without memory:

AI forgets everything

Conversations break

User experience becomes frustrating

👉 Conclusion:
No GenAI system can work properly without memory.

2️⃣ How LLMs Work at Inference (Very Important Foundation)
🔹 LLMs are Stateless by Design

At inference time, an LLM behaves like a pure mathematical function:

𝑦
=
𝑓
𝜃
(
𝑥
)
y=f
θ
	​

(x)

Where:

x = input tokens (your prompt)

θ (theta) = model parameters (fixed after training)

y = output tokens (LLM response)

🔹 Key Observations

θ is fixed (trained earlier, user cannot change it)

x changes every time (new prompt)

Output depends only on current input

📌 Important Result:
👉 LLMs do NOT remember past interactions

3️⃣ What Does “Stateless” Mean?

Stateless system =
Output depends only on current input, not on past inputs.

Example:
User: My name is Nitesh
LLM: Nice to meet you, Nitesh

User: What is my name?
LLM: Sorry, I don’t know your name


💡 Why?

Second call does not know about the first call

Each call is independent

👉 LLMs have NO intrinsic memory

4️⃣ The Core Problem
❌ Fact 1: LLMs have no memory
❌ Fact 2: Almost every GenAI app needs memory

⚠️ This creates a deadlock

So what do we do?

👉 We build memory externally around the LLM

5️⃣ Context Window (Very Important Concept)
🔹 What is Context Window?

Context Window =
Maximum number of tokens an LLM can read at one time before answering.

📷 Camera Analogy:

LLM = Camera

Context Window = Lens

Bigger lens → sees more scene

Examples:

128k tokens ≈ ~200 pages

Gemini models → up to 1 million tokens

📌 This is powerful because:
👉 We can send large conversation history to the model

6️⃣ In-Context Learning

LLMs have two sources of knowledge:

1️⃣ Parametric Knowledge

Learned during training

Stored in parameters

2️⃣ In-Context Knowledge

Provided inside the prompt itself

Example:

Upload a 100-page private PDF

Ask questions from it

Model answers using prompt content, not training data

📌 This ability is called In-Context Learning

7️⃣ First Memory Solution: Short-Term Memory (STM)
🔹 Idea

Since LLMs are stateless, we:
👉 Send conversation history with every request

Formula:
𝑦
2
=
𝑓
𝜃
(
𝑥
1
,
𝑦
1
,
𝑥
2
)
y
2
	​

=f
θ
	​

(x
1
	​

,y
1
	​

,x
2
	​

)

Instead of:

𝑦
2
=
𝑓
𝜃
(
𝑥
2
)
y
2
	​

=f
θ
	​

(x
2
	​

)
8️⃣ Code Example: Short-Term Memory
messages = []

# First user message
messages.append("My name is Nitesh")
response1 = llm.invoke(messages)
messages.append(response1)

# Second user message
messages.append("What is my name?")
response2 = llm.invoke(messages)

print(response2)
# Output: Your name is Nitesh

🔹 What changed?

messages acts as state

System becomes stateful

📌 This is called:

Conversation Buffer

Short-Term Memory

9️⃣ Why It Is Called Short-Term Memory

Stored in RAM

Lost when:

App restarts

Server crashes

New conversation starts

👉 Exists only inside one conversation

🔟 How Chatbots Use Short-Term Memory
🔹 Conversation = Thread

Each chat = one thread

STM is thread-scoped

When:

New chat starts → memory resets

Old chat resumes → memory reloaded

📌 That’s why ChatGPT shows separate conversations.

1️⃣1️⃣ Limitations of Short-Term Memory
❌ Problem 1: Fragile

Server crash → memory lost

❌ Problem 2: Context Window Overflow

Long chats exceed token limits

Model becomes incoherent or hallucinates

✅ Solutions:

Trimming: Keep last N messages

Summarization: Summarize old messages + recent messages

❌ Problem 3: Thread-Scoped (BIGGEST ISSUE)

STM cannot:

Remember user preferences across chats

Learn over time

Personalize the assistant

Do cross-conversation reasoning

📌 Result:

Every new chat = user becomes a stranger again

1️⃣2️⃣ Why We Need Long-Term Memory (LTM)

We need a new type of memory that:

✅ Survives across conversations
✅ Stores important information for days/months
✅ Enables personalization
✅ Compounds learning over time

👉 This is Long-Term Memory

1️⃣3️⃣ What Goes Into Long-Term Memory?

Only important, stable, reusable information.

Examples:

User preferences (Python over Java)

User profile (developer, beginner)

Past decisions and outcomes

What worked / what failed

❌ Not raw chat logs

1️⃣4️⃣ Types of Long-Term Memory
🧠 1. Episodic Memory

Past events

What happened before?

What worked / failed?

🧠 2. Semantic Memory

Facts

User prefers Python

Budget = ₹10,000

System uses PostgreSQL

🧠 3. Procedural Memory

How to do things

Preferred workflows

Rules

Strategies

Learned behaviors

📌 This makes agents feel smarter over time

1️⃣5️⃣ How Long-Term Memory Works (High Level)
4-Step Pipeline

1️⃣ Creation

Detect memory-worthy information

2️⃣ Storage

Save in durable storage (DB, vector DB, KV store)

3️⃣ Retrieval

Fetch relevant memories for current situation

4️⃣ Injection

Inject retrieved memory into short-term memory

Then send to LLM

📌 LTM never talks directly to LLM
👉 Always passes through STM

1️⃣6️⃣ Challenges in Building Memory Systems

Deciding what to remember

Retrieving right memory at right time

Engineering complexity

Multiple storage systems

1️⃣7️⃣ Tools & Libraries for Memory

Popular solutions:

LangMem (LangChain ecosystem)

Mem0

Supermemory

👉 These manage memory so developers can focus on apps

1️⃣8️⃣ Future of Memory in LLMs

Research ongoing for intrinsic memory

Google research: Titans + Mirage

New transformer architectures with built-in memory

📌 Because:

Without memory, GenAI and Agentic AI are impossible

✅ Final Takeaway
Memory Type	Scope	Purpose
Short-Term	One conversation	Continuity
Long-Term	Across conversations	Personalization & learning

👉 Real AI = LLM + Short-Term Memory + Long-Term Memory









