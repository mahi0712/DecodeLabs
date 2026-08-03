"""
Python Programming - Industrial Training Kit
Project 4: The General Knowledge Quiz
DecodeLabs | Batch 2026

Goal:
- Ask multiple general knowledge questions
- Keep a score counter (+1 for every correct answer)
- Print the final score at the end

Key Skill: If-Else logic & Variables (Control Flow)
Handles the "Case-Sensitivity Trap" -> user input is sanitized
(stripped + lowercased) before comparison, so "Paris", " paris ",
and "PARIS" are all treated as correct.
"""

import time

score = 0
total_questions = 8

print("=" * 50)
print("🧠  WELCOME TO THE ULTIMATE GENERAL KNOWLEDGE QUIZ  🧠")
print("=" * 50)
name = input("\nEnter your name to begin: ").strip().title()
print(f"\nGood luck, {name}! Let's see how sharp you are. 🚀\n")
time.sleep(1)

answer = input("Q1. What is the capital of France? ").strip().lower()
if answer == "paris":
    print("Correct! ✅ Paris it is, the City of Light.")
    score += 1
else:
    print("Wrong! ❌ The correct answer was Paris.")

answer = input("\nQ2. Which planet is known as the Red Planet? ").strip().lower()
if answer == "mars":
    print("Correct! ✅ Mars, named after the Roman god of war.")
    score += 1
else:
    print("Wrong! ❌ The correct answer was Mars.")

answer = input("\nQ3. Who wrote the play 'Romeo and Juliet'? ").strip().lower()
if answer in ("shakespeare", "william shakespeare"):
    print("Correct! ✅ William Shakespeare, the Bard himself.")
    score += 1
else:
    print("Wrong! ❌ The correct answer was William Shakespeare.")

answer = input("\nQ4. What is the largest ocean on Earth? ").strip().lower()
if answer in ("pacific", "pacific ocean"):
    print("Correct! ✅ The Pacific Ocean covers about a third of the Earth.")
    score += 1
else:
    print("Wrong! ❌ The correct answer was the Pacific Ocean.")

answer = input("\nQ5. How many continents are there on Earth? ").strip().lower()
if answer == "7" or answer == "seven":
    print("Correct! ✅ There are 7 continents.")
    score += 1
else:
    print("Wrong! ❌ The correct answer was 7 (seven).")


answer = input("\nQ6. Which gas do humans need to breathe to survive? ").strip().lower()
if answer in ("oxygen", "o2"):
    print("Correct! ✅ Oxygen keeps us alive.")
    score += 1
else:
    print("Wrong! ❌ The correct answer was Oxygen.")

answer = input("\nQ7. What is the national language of Pakistan? ").strip().lower()
if answer == "urdu":
    print("Correct! ✅ Urdu it is.")
    score += 1
else:
    print("Wrong! ❌ The correct answer was Urdu.")

answer = input("\nQ8. In Python, which keyword is used to define a function? ").strip().lower()
if answer == "def":
    print("Correct! ✅ 'def' defines a function in Python.")
    score += 1
else:
    print("Wrong! ❌ The correct answer was 'def'.")

time.sleep(1)
print("\n" + "=" * 50)
print("🏁  QUIZ FINISHED  🏁")
print("=" * 50)
percentage = (score / total_questions) * 100
print(f"\n{name}, your final score is: {score}/{total_questions} ({percentage:.0f}%)")

if score == total_questions:
    print("Perfect score! You're a certified genius. 🏆🎉")
elif score >= total_questions * 0.7:
    print("Excellent work! Almost flawless. 🌟")
elif score >= total_questions * 0.4:
    print("Not bad! A little more trivia reading and you'll ace it. 👍")
else:
    print("Better luck next time — go brush up on your facts! 📚")

print("\nThanks for playing, see you next round! 👋")