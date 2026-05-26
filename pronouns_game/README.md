# 🌍 Pronoun Master

### A Knowledge Graph–Powered Game for Learning Social Pronouns in Honorific Languages

**Pronoun Master** is an adaptive sociolinguistic learning game designed to help **heritage language learners** master pronoun usage in socially hierarchical languages.

Instead of teaching pronouns through simple one-to-one translations, Pronoun Master models **human relationships and social context** using a **multilayer knowledge graph**. The system dynamically evaluates cultural appropriateness and adapts exercise difficulty based on learner performance.

Currently supported languages include **Vietnamese**, **Urdu**, and **Nepali**.

---

## 🎯 Motivation

### The Problem: Pronouns Are Social, Not Fixed

For many **heritage Vietnamese learners**, pronoun usage is one of the most difficult aspects of language learning.

Unlike English pronouns (*I, you, he, she*), Vietnamese pronouns are **socially negotiated** rather than fixed. Speakers must choose pronouns according to:

* **Age hierarchy**
* **Generation level**
* **Gender**
* **Social context**
* **Relationship between speakers**

The same person may be addressed differently depending on the situation.

For example, one person could be called:

* *anh* (older brother / older male peer)
* *chú* (younger uncle)
* *bác* (older uncle)
* *ông* (grandfather / elderly man)

—all depending on **relative age and social context**.

This complexity often creates anxiety and uncertainty for heritage learners, even when they understand vocabulary and grammar.

### Our Goal

Pronoun Master helps learners:

✅ Recognize social hierarchies
✅ Select culturally appropriate **pronoun pairs** (*speaker ↔ addressee*)
✅ Practice pronouns in realistic social situations
✅ Build confidence through adaptive feedback

The ultimate goal is to help learners navigate **everyday social interactions** more naturally.

---

## 🧠 How It Works

Pronoun Master models pronoun selection as a **knowledge graph problem**.

Rather than memorizing isolated vocabulary, learners interact with a system that evaluates **social distance** between speakers.

The engine represents social relationships across **five semantic layers**:

1. **Broad Age Category**
   (Child, Peer, Parent, Grandparent)

2. **Specific Generation**
   (Older sibling, younger aunt, uncle, etc.)

3. **Target Gender**

4. **Social Context**
   (Formal, casual, family, workplace)

5. **Speaker Gender**

These layers form a **semantic web of cultural relationships**, enabling the system to dynamically generate exercises and evaluate mistakes based on their social severity.

---

## ✨ Core Features

### 🧠 5-Layer Knowledge Graph

Models pronoun interactions across:

* Broad age
* Specific generation
* Gender
* Social setting
* Speaker identity

This allows the system to reason about **cultural appropriateness**, not just grammatical correctness.

### ⚡ Dynamic Exercise Generation

The game generates **thousands of possible exercises automatically**.

Adding a new language or social scenario requires **no code changes** — simply add rows to the linguistic database.

### 🎯 Adaptive Difficulty Progression

The learning engine gradually scaffolds complexity:

#### Easy

Focuses on **broad age distinctions**

> child ↔ adult

#### Medium

Introduces **generational nuance and gender**

> older cousin ↔ younger aunt

#### Hard

Tests **social register and contextual appropriateness**

> formal vs. casual interactions among peers

### 💰 Cultural Bounty Scoring

Pronoun mistakes are treated as **graded cultural mismatches**, not binary failures.

Each question begins with **20 points**, and penalties are deducted according to the social severity of the error.

### 🖼️ Visual Social Profiles

Instead of long textual descriptions, Pronoun Master uses **dynamic visual cues**.

Example:

**👴🏽 → 🏢**
*A grandparent in a formal setting*

This reduces reading load and encourages intuitive sociolinguistic reasoning.

---

## 🏗️ System Architecture

The project is divided into two major components:

### 1. Python Knowledge Graph Compiler

A Python pipeline reads the linguistic database from:

`db_pronouns_social-adressing_v1.xlsx`

The compiler:

* Cleans and normalizes linguistic data
* Builds a **Directed Acyclic Graph (DAG)** using `NetworkX`
* Collapses redundant nodes into a semantic star schema
* Projects them into concrete **pronoun instances**

### 2. Interactive Learning Engine

The frontend game is built with vanilla JavaScript and consumes the generated graph assets.

After compilation, the system exports production-ready files into `graph_export/`.

### Generated Artifacts

| File                     | Purpose                                  |
| ------------------------ | ---------------------------------------- |
| `graph_data.js`          | Compiled semantic graph for the frontend |
| `nodes.csv`              | Node export for analysis                 |
| `edges.csv`              | Edge export for analysis                 |
| `confusion.csv`          | Penalty-rule metadata                    |
| `semantic_graph.png`     | Static graph visualization               |
| `interactive_graph.html` | Interactive graph explorer               |

---

## 📊 Cultural Distance Scoring

When a learner chooses an incorrect pronoun, the system calculates the **Cultural Distance** between the selected answer and the correct answer.

Errors are weighted according to sociolinguistic severity:

| Mismatch Layer      | Penalty | Severity                      |
| ------------------- | ------: | ----------------------------- |
| Broad Age           | -10 pts | 🚨 Critical cultural error    |
| Specific Generation |  -8 pts | 🔴 Major generational mistake |
| Addressee Gender    |  -6 pts | 🔴 Major grammatical mismatch |
| Social Context      |  -4 pts | 🟠 Register misalignment      |
| Speaker Gender      |  -2 pts | 🟡 Minor awkwardness          |

**Scoring Formula**

```text
Bounty = 20 − (Sum of Mismatched Layer Weights × 2)
```

This system rewards learners for being **socially close**, even when imperfect.

---

## 🚀 Installation & Usage

### Prerequisites

* Python **3.8+**
* A modern web browser

(Chrome, Firefox, Safari, Edge)

### Step 1 — Build the Knowledge Graph

Install dependencies:

```bash
pip install pandas networkx matplotlib openpyxl
```

Run the graph compiler:

```bash
python build_graph.py
```

> Ensure `db_pronouns_social-adressing_v1.xlsx` is located in the project root.

---

### Step 2 — Launch the Game

After compilation, open:

```text
index.html
```

in your browser.

No local web server is required.

---

### Step 3 — Explore the Graph

Open:

```text
interactive_graph.html
```

to visualize the semantic network through an interactive graph interface.

---

## 📂 Repository Structure

```text
├── db_pronouns_social-adressing_v1.xlsx
├── build_graph.py
├── index.html
├── interactive_graph.html
├── semantic_graph.png
└── graph_export/
    ├── graph_data.js
    └── artifacts/
        ├── nodes.csv
        ├── edges.csv
        └── confusion.csv
```

---

## 🔮 Roadmap

### Syntactic Hooks

Extend graph nodes with grammatical constraints such as:

* Urdu verb agreement
* Honorific verb morphology
* Pronoun-dependent conjugation systems

### Personalized Remediation

Track historical learner errors and model them as **negative graph edges** to generate personalized review exercises.

### Cloud Knowledge Graph

Migrate from static JSON exports to a graph database (e.g., Neo4j) to enable collaborative linguistic contributions and live updates.