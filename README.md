# 🧠 MiniCPM5-1B — Tool Calling on a CPU Laptop

![License](https://img.shields.io/badge/License-Apache_2.0-green?style=for-the-badge)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Mac%20%7C%20Linux-blue?style=for-the-badge)
![Model](https://img.shields.io/badge/Model-MiniCPM5--1B_1B_Params-purple?style=for-the-badge)
![Size](https://img.shields.io/badge/Size-1.15_GB-orange?style=for-the-badge)
![GPU](https://img.shields.io/badge/GPU-Not_Required-brightgreen?style=for-the-badge)

> **A 1 billion parameter model that knows when it doesn't know — and calls the right tool instead. No cloud, no GPU, just a CPU and a model that's barely 1 GB in size.**

---

## 📺 Watch the Full Video

**Why a 1B Model Is All You Need for Local AI Agents**

[![Watch on YouTube](https://img.shields.io/badge/▶_Watch_on_YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/watch?v=lsCOkUZxGXw)

> A one billion parameter model just refused to do math — and called a calculator instead. No GPU. No cloud. Just a CPU and a model that's barely one gig in size.



---

## ⚡ What Is This?

This repo contains three working demos of **MiniCPM5-1B Agentic Tool Use** — a community fine-tuned version of [MiniCPM-o 2.6](https://huggingface.co/openbmb/MiniCPM-o-2_6) by OpenBMB, specifically trained for tool calling using LoRA.

The core idea: **restraint over hallucination**. Instead of trying to answer everything from memory and guessing wrong, this tiny model recognizes its own limits and routes to the right tool. That's the "cognitive core" concept in action — the model doesn't memorize everything, it just knows *who to ask*.

| Demo | What It Does |
|------|-------------|
| 🔢 **test_tool.py** | Single tool call — model calls a calculator instead of guessing math |
| 💻 **cli_assistant.py** | Smart CLI — converts plain English into terminal commands with user confirmation |
| 📋 **meeting_notes.py** | Meeting notes → structured action items — extracts tasks, assignees, deadlines, and priorities |

---

## 🔑 Why This Model Is Different

Most small models (Phi, Qwen, Gemma) support tool calling in theory, but in practice they still try to answer from memory first. They guess, hallucinate, and pretend they know. MiniCPM5-1B is different for three reasons:

### 1. Training Data — Public and Purpose-Built
OpenBMB released everything. 400B tokens of supervised fine-tuning data — half "deep thinking" data (step-by-step reasoning) and half "hybrid thinking" data (learning *when* to think deeply vs. when to answer quickly). That balance is why the model doesn't get stuck in endless reasoning loops.

### 2. On-Policy Distillation — The Real Secret Sauce
Specialized teacher models (math, code, QA) distilled just the *decision-making ability* back into 1B parameters. Result: average scores went up 16 points while overly long responses dropped 29%. Smarter **and** shorter.

### 3. It Knows What It Doesn't Know
On the AAlmanac hallucination benchmark, most small models score around **-40** (they make stuff up constantly). This model scores **-1** — almost zero. When asked 347 × 892 without a calculator, it didn't guess. It said "I can't do this." That restraint is what makes the whole tool-calling architecture possible.

| Benchmark | Typical 1B Model | MiniCPM5-1B |
|-----------|:---:|:---:|
| Hallucination Score (AAlmanac) | ~-40 | **-1** |
| Context Length | 4K–32K | **128K** |
| Model Size | — | **1.15 GB (Q8)** |

---

## 🧩 The Cognitive Core — Why Restraint Beats Size

This is the idea that ties everything together. Most people think AI progress means "build a bigger model." Karpathy's cognitive core concept flips that: what if the future isn't one giant model that knows everything, but a tiny model that knows *what it doesn't know* and reaches for the right tool?

Think about it like a smart manager. They don't know accounting, law, and engineering — but they know exactly who on their team to assign each task to. That's what this 1B model does. The code just gives it the phone numbers (tools). The model decides who to call and when.

**The old approach (bigger = better):**
- 70B parameter model tries to answer from memory
- Gets it right most of the time, but hallucinates the rest
- Needs expensive GPU, cloud dependency, your data leaves your machine

**The cognitive core approach (small + restrained):**
- 1B parameter model knows its limits
- Calls the right tool instead of guessing
- Runs on CPU, 100% local, your data never leaves your machine

That's not a downgrade. That's a fundamentally different architecture for intelligence. And the demos in this repo prove it works today.

---

## 🌍 Where This Is Heading — Tiny Models Everywhere

The long-term vision isn't about laptops running small models. It's about every device having a tiny brain that knows when to ask for help.

**What a 1B model enables that a 70B model never will:**

| Device | Use Case | Why 1B Works |
|--------|----------|--------------|
| 📱 Phone | On-device assistant that routes tasks locally | Fits in RAM alongside your apps |
| 💻 Laptop | Offline productivity — meeting notes, CLI, docs | No cloud round-trip, instant response |
| 🏠 Smart Home | Voice commands that actually understand intent | Privacy-first — audio never leaves the house |
| 🏭 Factory Sensor | Real-time anomaly detection with tool-based reasoning | Runs on edge hardware, no internet needed |
| 🚗 Car Dashboard | Voice-driven navigation and diagnostics | Low latency, works in tunnels, no cell signal required |

**A year ago:** Small models couldn't stop hallucinating. Every release was "impressive benchmarks, you try it yourself, and disappointment."

**Today:** A 1B model says "I don't know" and picks up the right tool instead. Real progress.

**Tomorrow:** Tiny models baked into every device invisibly. You just talk to your phone or laptop, and the small model behind the scenes routes your request to the right tool — no coding needed on your end. No cloud subscription. No API costs. No data leaving the building.

> *The future isn't one giant model in the cloud. It's tiny local models that know who to ask.*

---

## 🚀 Setup

### Prerequisites

- [LM Studio](https://lmstudio.ai/) (free) — the easiest way to run local models
- Python 3.8+ with `requests` installed
- 16 GB RAM (no GPU needed)

### Step 1 — Download the Model

1. Open **LM Studio**
2. Search for: **`minicpm5-1b-agentic-tooluse`**
3. Select the **Q8** quantization (highest quality, ~1.15 GB)
4. Hit **Download**

> The base model is [MiniCPM-o 2.6](https://huggingface.co/openbmb/MiniCPM-o-2_6) by OpenBMB (Apache 2.0). This is a community fine-tune optimized for tool calling via LoRA.

### Step 2 — Load & Start the Server

1. Click **Load** on the downloaded model
2. Go to the **Developer** tab
3. Click **Start Local Server**

This gives you an OpenAI-compatible API at `http://localhost:1234` that all three scripts use.

### Step 3 — Install Python Dependencies

```bash
pip install requests
```

That's it. One dependency. Everything runs through the local LM Studio server.

---

## 📂 Project Structure

```
.
├── test_tool.py          # Demo 1: Calculator tool call
├── cli_assistant.py      # Demo 2: Smart CLI assistant
├── meeting_notes.py      # Demo 3: Meeting notes → action items
└── README.md
```

---

## 🔢 Demo 1 — Calculator Tool Call (`test_tool.py`)

**What happens:** The model is asked a math question (347 × 892). Instead of guessing, it generates a structured tool call. The script executes it and returns the real answer.

```bash
python test_tool.py
```

**Expected output:**
```
Model wants to call: calculator({'expression': '347 * 892'})
Result: 309524
```

**How it works:**
1. Script sends the question + tool definition to the local model
2. Model recognizes it can't do the math and generates a `calculator` tool call
3. Script catches the tool call, evaluates the expression, and prints the result
4. Model never guesses — it routes

---

## 💻 Demo 2 — Smart CLI Assistant (`cli_assistant.py`)

**What happens:** You type what you want in plain English. The model converts it into a real terminal command, explains what it does, and waits for your confirmation before running anything.

```bash
python cli_assistant.py
```

**Example session:**
```
=== Smart CLI Assistant (MiniCPM5-1B) ===
Type a request in plain English. Type 'quit' to exit.

You: Show me my disk space

Command:     wmic logicaldisk get caption,freespace,size
Explanation: Lists all disk drives with their free space and total size

Run this? (y/n): y

Output:
Caption  FreeSpace     Size
C:       508062949376  536849342464
E:       664619470848  687194767360
```

**Key details:**
- The system prompt tells the model to **always** use the `run_command` tool — never answer directly
- Be specific with your OS context (e.g., "You're running on Windows PowerShell") — this is a 1B model, you have to meet it halfway
- Every command requires explicit `y/n` confirmation before execution — nothing runs without your approval
- Works with any shell command: `systeminfo`, `tasklist`, `dir`, `ipconfig`, etc.

> **Pro tip:** With a 1B model, prompt specificity matters. It knows *how* to route, but it doesn't memorize every OS command. If it gives a wrong command, add more context to the system prompt (e.g., "Use Windows commands, not Linux").

---

## 📋 Demo 3 — Meeting Notes → Action Items (`meeting_notes.py`)

**What happens:** You paste messy meeting notes. The model extracts structured action items — tasks, assignees, deadlines, and priorities — and outputs them as clean tool calls.

```bash
python meeting_notes.py
```

**Example input (already in the script):**
```
Team standup July 8: John said the API migration is behind schedule,
needs to finish by Friday July 11. Maria will review the Q3 budget,
we're over by 15 percent on a 50000 dollar budget so need to find
cuts. Raj is handling the client demo on Monday July 14, high priority.
Sarah needs to update the documentation by end of week, low priority.
```

**Expected output:**
```
=== Meeting Notes → Action Items (MiniCPM5-1B) ===

Input:
Team standup July 8: John said the API migration is behind schedule, ...

Processing...

Found 4 action items:

  [1] API migration
      Assignee: John
      Deadline: Friday July 11
      Priority: high

  [2] Review the Q3 budget
      Assignee: Maria
      Deadline: ...
      Priority: medium

  [3] Client demo
      Assignee: Raj
      Deadline: Monday July 14
      Priority: high

  [4] Update the documentation
      Assignee: Sarah
      Deadline: end of week
      Priority: low
```

**What makes this impressive:**
- **4 separate tool calls in a single response** — from a 1B model running on CPU
- The model reads messy, unstructured text and produces clean, structured output
- Each action item has task, assignee, deadline, and priority correctly extracted
- Your notes never leave your machine — fully local, fully private

> **Known limitation:** The model sometimes confuses which field to put budget info in (e.g., putting budget numbers in the deadline field instead of calling the calculator tool). This is a real limitation of 1B parameters — the routing works, but domain-specific formatting can be hit or miss.

---

## 🧪 The "Without Tools" Test

Try this to see the restraint in action. Open LM Studio's chat interface (no tools attached) and ask:

```
What is 347 * 892?
```

The model will think for about a minute and then respond:

> *"I'm not able to manually solve complex multiplications like this because it involves a very large number of digits and is beyond my current capabilities."*

It doesn't guess. It doesn't hallucinate. It just says "I can't." **That restraint is the feature.** Now give it the calculator tool and watch it route instead.

---

## 🏗 Architecture — How Tool Calling Works Here

```
┌─────────────────┐       ┌──────────────────┐       ┌──────────────┐
│   User Input    │──────▶│  MiniCPM5-1B     │──────▶│  Tool Call   │
│  (plain text)   │       │  (local, CPU)    │       │  (JSON)      │
└─────────────────┘       └──────────────────┘       └──────┬───────┘
                                                              │
                          ┌──────────────────┐       ┌───────▼───────┐
                          │  Final Result    │◀──────│  Python       │
                          │  (real answer)   │       │  executes     │
                          └──────────────────┘       │  tool locally │
                                                    └───────────────┘
```

1. **Define tools** — your Python script tells the model what tools are available using the OpenAI function-calling format
2. **Send question** — user input + tool definitions go to the local model via LM Studio's API
3. **Model decides** — the model chooses whether to answer directly or call a tool (it almost always calls a tool)
4. **Script executes** — Python catches the tool call, runs the actual function locally
5. **Real result** — the answer comes from real computation, not model memory

No cloud. No API costs. No data leaving your machine.

---

## ⚠️ Limitations & Honest Takeaways

This is a 1B model. Here's what that actually means in practice:

| Works Well | Needs Work |
|-----------|-----------|
| Tool routing — picks the right tool | Domain knowledge — doesn't know every OS command |
| Argument formatting — structures JSON correctly | Complex reasoning — can confuse which field holds what |
| Restraint — rarely hallucinates | Multi-step chains — one call at a time works best |
| Structured extraction — pulls entities from text | Edge cases — needs explicit, specific prompts |

**The bottom line:** The intelligence is in the **routing**, not the **knowledge**. You can always fix a knowledge gap with a better prompt or a reference list. But the routing layer — knowing *when* to call a tool and *which* one — that's the hard part. And this 1 GB model can do it.


## 📎 Model Credits

| Component | Source |
|-----------|--------|
| Base Model | [MiniCPM-o 2.6](https://huggingface.co/openbmb/MiniCPM-o-2_6) — OpenBMB |
| Fine-tune | Community `agentic-tool-use` LoRA adapter on HuggingFace |
| Inference | [LM Studio](https://lmstudio.ai/) — local model runner |



