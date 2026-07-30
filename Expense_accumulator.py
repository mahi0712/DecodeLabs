def expense_tracker():
    total = 0.0  # State initialized OUTSIDE the loop (accumulator)
    count = 0

    print("Expense Tracker - DecodeLabs")
    print("Enter expense amounts one by one. Type 'quit' to stop.\n")

    while True:
        entry = input("Enter expense (or 'quit' to finish): ").strip()

        # Sentinel value check - kill switch
        if entry.lower() == 'quit':
            break

        # Defensive coding - digital poka-yoke
        try:
            expense = float(entry)
            if expense < 0:
                print("Invalid Data: Expense cannot be negative.\n")
                continue
        except ValueError:
            print("Invalid Data: Please enter a valid number.\n")
            continue

        total += expense  # Accumulator pattern: State(new) = State(old) + Input
        count += 1
        print(f"Added: {expense:.2f} | Running Total: {total:.2f}\n")

    # Phase 3: Output - decoupled from logic
    print("-" * 30)
    print(f"Transactions recorded: {count}")
    print(f"FINAL TOTAL SPENT: {total:.2f}")


if __name__ == "__main__":
    expense_tracker()