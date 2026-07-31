# 🔐 Password Generator — Project 3

**DecodeLabs Python Programming — Industrial Training Kit**
Author: Syeda Maha Hussain
Batch: 2026

## 📌 Overview

This is a command-line password generator built in Python. It asks the
user for a desired password length and generates a random, secure
password using letters, digits, and symbols.

This project was built to practice two core Python skills:
- **Importing Modules** — using Python's built-in `secrets`, `string`,
  and `math` modules instead of writing custom logic
- **String Manipulation** — building, combining, and shuffling character
  sets to construct a password

## ✨ Features

| Feature | Description |
|---|---|
| Secure randomness | Uses the `secrets` module instead of `random`, since `secrets` is cryptographically secure and not predictable |
| Guaranteed complexity | Every password is guaranteed to contain at least 1 uppercase letter, 1 lowercase letter, 1 digit, and 1 symbol |
| Entropy calculation | Displays password strength in bits using `E = L × log2(R)` |
| Visual strength meter | Shows a strength bar (`Weak` → `Very Strong`) next to every password |
| Ambiguous character exclusion | Optionally removes confusing characters like `l`, `1`, `I`, `O`, `0` |
| Input validation | Rejects invalid or out-of-range lengths instead of crashing |
| Loop mode | Generate as many passwords as you want in a single run |
| Graceful exit | Handles `Ctrl+C` cleanly instead of showing an error traceback |

## 🛠️ Requirements

- Python 3.6 or higher (uses the `secrets` module, introduced in 3.6)
- No external libraries needed — only Python's standard library

## ▶️ How to Run

```bash
python "Password Generator.py"
```

You will be asked:
1. **Password length** (between 8 and 64 characters)
2. **Whether to exclude ambiguous characters** (y/n)

The program will then print your password along with its strength,
and ask if you'd like to generate another one.

## 📋 Example Output

```
=============================================
   DecodeLabs - Secure Password Generator
=============================================
Enter desired password length (8-64): 16
Exclude ambiguous characters like l, 1, I, O, 0? (y/n): n

Your generated password is:
>>> Dn#4r*6V4h5FpQ2w <<<
Strength: [████████░░] 95.3 bits — Very Strong

Generate another password? (y/n): n

Goodbye!
```

## 🧠 How It Works

1. **Input phase** — the user enters a password length; the program
   validates it's a whole number within the allowed range (8–64).
2. **Generation phase** — four character pools (lowercase, uppercase,
   digits, symbols) are built. One character is picked from each pool
   to guarantee complexity, then the rest of the password is filled
   randomly and the whole string is shuffled using `secrets`.
3. **Output phase** — the password's entropy is calculated and shown
   as a strength label and visual bar, so the user knows exactly how
   secure their password is.

## 📚 Concepts Practiced

- `import` statements and using standard library modules
- String concatenation and manipulation
- List comprehensions
- Functions and program structure (separation of concerns)
- Basic error handling (`try`/`except`)
- Input validation loops

## 📞 Contact

DecodeLabs:
✉️ decodelabs.tech@gmail.com
🌎 www.decodelabs.tech
