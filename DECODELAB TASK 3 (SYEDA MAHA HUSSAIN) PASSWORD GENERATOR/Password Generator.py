
import secrets
import string
import math

MIN_LENGTH = 8
MAX_LENGTH = 64
AMBIGUOUS_CHARS = "l1IO0"


def get_password_length():
    while True:
        try:
            length = int(input(f"Enter desired password length ({MIN_LENGTH}-{MAX_LENGTH}): "))
            if length < MIN_LENGTH or length > MAX_LENGTH:
                print(f"Length must be between {MIN_LENGTH} and {MAX_LENGTH}. Try again.")
                continue
            return length
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def get_yes_no(prompt):
    """Generic yes/no prompt. Returns True for yes, False for no."""
    while True:
        choice = input(prompt).strip().lower()
        if choice in ("y", "yes"):
            return True
        elif choice in ("n", "no"):
            return False
        else:
            print("Please enter 'y' or 'n'.")


def build_character_pools(exclude_ambiguous):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = "!@#$%^&*()-_=+"

    if exclude_ambiguous:
        lower = ''.join(c for c in lower if c not in AMBIGUOUS_CHARS)
        upper = ''.join(c for c in upper if c not in AMBIGUOUS_CHARS)
        digits = ''.join(c for c in digits if c not in AMBIGUOUS_CHARS)

    return lower, upper, digits, symbols


def generate_password(length, exclude_ambiguous=False):
    lower, upper, digits, symbols = build_character_pools(exclude_ambiguous)
    all_chars = lower + upper + digits + symbols

    # Step 1: guarantee one character from each category
    password_chars = [
        secrets.choice(lower),
        secrets.choice(upper),
        secrets.choice(digits),
        secrets.choice(symbols),
    ]

    # Step 2: fill the rest randomly from the combined pool
    password_chars += [secrets.choice(all_chars) for _ in range(length - 4)]

    # Step 3: shuffle so the guaranteed chars aren't always at the start
    for i in range(len(password_chars) - 1, 0, -1):
        j = secrets.randbelow(i + 1)
        password_chars[i], password_chars[j] = password_chars[j], password_chars[i]

    return ''.join(password_chars), len(all_chars)


def calculate_entropy(length, pool_size):
    """Entropy in bits: E = L * log2(R)"""
    return length * math.log2(pool_size)


def strength_label_and_bar(entropy):
    if entropy < 40:
        label = "Weak"
    elif entropy < 60:
        label = "Moderate"
    elif entropy < 80:
        label = "Strong"
    else:
        label = "Very Strong"

    filled = min(10, int(entropy / 12))  # scale roughly to 10 blocks
    bar = "█" * filled + "░" * (10 - filled)
    return label, bar


def main():
    print("=" * 45)
    print("   DecodeLabs - Secure Password Generator")
    print("=" * 45)

    while True:
        length = get_password_length()
        exclude_ambiguous = get_yes_no("Exclude ambiguous characters like l, 1, I, O, 0? (y/n): ")

        password, pool_size = generate_password(length, exclude_ambiguous)
        entropy = calculate_entropy(length, pool_size)
        label, bar = strength_label_and_bar(entropy)

        print("\nYour generated password is:")
        print(f">>> {password} <<<")
        print(f"Strength: [{bar}] {entropy:.1f} bits — {label}")

        if not get_yes_no("\nGenerate another password? (y/n): "):
            print("\nGoodbye!")
            break


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user. Exiting...")