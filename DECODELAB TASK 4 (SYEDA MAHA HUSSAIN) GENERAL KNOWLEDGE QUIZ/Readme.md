# 🧠 General Knowledge Quiz

**DecodeLabs Industrial Training Kit — Python Programming, Project 4**
Batch: 2026 | Author: Syeda Maha Hussain

A terminal-based quiz game built in Python that tests general knowledge
across geography, science, literature, and more — while demonstrating
core **Control Flow** concepts: variables, if-else logic, loops, and
input sanitization.

## 📋 Overview

This project simulates the role of a Python Developer building a small
**decision engine**: a program that reacts to human input in real time,
tracks state (score), and produces a final evaluated output.

- Asks **8 general knowledge questions**
- Tracks your score with a running counter
- Shares a fun fact after every answer
- Gives a final percentage + performance grade
- Handles messy human input (extra spaces, random capitalization)

## 🎯 Key Skills Demonstrated

| Concept | Where it's used |
|---|---|
| Variables & State Management | `score` counter persists across the quiz |
| If-Else / Control Flow | Checking each answer, grading the final result |
| Loops | Iterating through the question list |
| Input Sanitization | `.strip().lower()` defeats the "Case-Sensitivity Trap" |
| Data Structures | Questions stored as a list of dictionaries |

## 🛠️ Requirements

- Python 3.7 or higher (no external libraries needed)

## ▶️ How to Run

**Windows (PowerShell):**
```powershell
python main.py
```
or, if `python` isn't recognized:
```powershell
py main.py
```

**macOS / Linux:**
```bash
python3 main.py
```

## 🕹️ Sample Gameplay

```
==================================================
🧠  WELCOME TO THE GENERAL KNOWLEDGE QUIZ  🧠
==================================================
You will be asked 8 questions.
Type your answer and hit Enter. Let's go!

Q1. What is the capital of France? paris
Correct! ✅
💡 Fun fact: Paris is nicknamed 'The City of Light' 💡

...

==================================================
🏁  QUIZ FINISHED  🏁
==================================================
Your final score is: 7/8 (88%)
Excellent work! 🌟
```

## ➕ Adding Your Own Questions

Questions live in the `questions` list at the top of `main.py`. Add a
new dictionary to the list to add a question:

```python
{
    "question": "Your question here?",
    "answers": ["accepted answer", "another accepted spelling"],
    "fact": "A fun fact shown after answering.",
},
```

The `answers` list lets you accept multiple correct phrasings (e.g.
`"shakespeare"` and `"william shakespeare"`).

## 📁 Files

| File | Description |
|---|---|
| `main.py` | The quiz program |
| `README.md` | This file |

---
*Built as part of the DecodeLabs Python Programming Industrial Training Kit.*