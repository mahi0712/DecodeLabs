# Expense Tracker — Project 2 (DecodeLabs Industrial Training Kit)

A simple command-line Python script that lets a user enter multiple expense amounts and displays the running total, using the **accumulator pattern**.

## 📌 Overview

| | |
|---|---|
| **Project** | 2 — Expense Tracker |
| **Track** | Python Programming (Industrial Training Kit) |
| **Batch** | 2026 |
| **Key Skill** | Math operations & Accumulators |
| **Concept** | `total = total + new_expense` (State accumulation) |

## 🎯 Goal

Build a script where the user enters expense amounts one at a time (e.g. `100`, `50`, `20`). The program keeps adding them up and displays the **Total Spent** once the user is done.

## ⚙️ How It Works

1. **Initialize state outside the loop** — `total = 0.0` is set once, before the loop starts, so it isn't reset on every iteration.
2. **Loop continuously** — `while True:` keeps asking for new expenses.
3. **Accumulate** — every valid entry updates the state: `total += expense`.
4. **Defensive coding** — invalid (non-numeric) input is caught with `try/except ValueError` instead of crashing the program.
5. **Sentinel value exit** — typing `quit` breaks the loop (the "kill switch").
6. **Output phase** — once the loop ends, the final total and transaction count are printed.

## ▶️ How to Run

```bash
python expense_tracker.py
```

## 💻 Sample Run

```
Expense Tracker - DecodeLabs
Enter expense amounts one by one. Type 'quit' to stop.

Enter expense (or 'quit' to finish): 100
Added: 100.00 | Running Total: 100.00

Enter expense (or 'quit' to finish): 50
Added: 50.00 | Running Total: 150.00

Enter expense (or 'quit' to finish): 20
Added: 20.00 | Running Total: 170.00

Enter expense (or 'quit' to finish): quit
------------------------------
Transactions recorded: 3
FINAL TOTAL SPENT: 170.00
```

## ✅ Quality Checklist (per project guidelines)

- [x] Stability: handles 5+ transactions without breaking
- [x] State: `total` initialized **outside** the loop
- [x] Defense: catches `ValueError` on invalid input
- [x] Control: sentinel value (`quit`) cleanly exits and prints the final total

## 📂 Files

- `expense_tracker.py` — main script
- `README.md` — this file

## 🏢 Credits

Built as part of the **DecodeLabs Industrial Training Kit — Python Programming, Batch 2026**.

- 🌎 www.decodelabs.tech
- ✉️ decodelabs.tech@gmail.com
