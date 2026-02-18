import re
import math

# ANSI color codes for CLI output
COLORS = {
    "red": "\033[91m",
    "yellow": "\033[93m",
    "green": "\033[92m",
    "cyan": "\033[96m",
    "magenta": "\033[95m",
    "reset": "\033[0m"
}

# Function to calculate entropy based on character set size and password length
def calculate_entropy(password):
    charset_size = 0
    if re.search(r"[a-z]", password):  # lowercase letters
        charset_size += 26
    if re.search(r"[A-Z]", password):  # uppercase letters
        charset_size += 26
    if re.search(r"[0-9]", password):  # digits
        charset_size += 10
    if re.search(r"[^a-zA-Z0-9]", password):  # special characters
        charset_size += 32  # rough estimate of symbols

    # Entropy formula: length * log2(charset_size)
    entropy = len(password) * math.log2(charset_size) if charset_size > 0 else 0
    return entropy

# Function to evaluate password strength using regex rules + entropy
def evaluate_password(password):
    entropy = calculate_entropy(password)

    # Basic regex checks
    length_ok = len(password) >= 8
    has_upper = bool(re.search(r"[A-Z]", password))
    has_lower = bool(re.search(r"[a-z]", password))
    has_digit = bool(re.search(r"[0-9]", password))
    has_symbol = bool(re.search(r"[^a-zA-Z0-9]", password))

    # Score system (Revlink-style)
    score = 0
    if length_ok: score += 2
    if has_upper: score += 1
    if has_lower: score += 1
    if has_digit: score += 2
    if has_symbol: score += 2
    if entropy > 50: score += 2
    if entropy > 75: score += 3

    # Gamified meter
    if score <= 3:
        level, color = "Weak", COLORS["red"]
    elif score <= 6:
        level, color = "Decent", COLORS["yellow"]
    elif score <= 9:
        level, color = "Strong", COLORS["cyan"]
    elif score <= 12:
        level, color = "Epic", COLORS["magenta"]
    else:
        level, color = "Legendary", COLORS["green"]

    return entropy, score, level, color

# Function to display progress bar
def display_meter(score, max_score=15):
    filled = int((score / max_score) * 20)  # 20 blocks total
    bar = "[" + "#" * filled + "-" * (20 - filled) + "]"
    return bar

# CLI entry point
if __name__ == "__main__":
    print("\nWelcome to PassQuest 🔐")
    password = input("Enter a password to check: ")
    entropy, score, level, color = evaluate_password(password)

    print("\n--- Password Strength Report ---")
    print(f"Entropy: {entropy:.2f} bits")
    print(f"Score: {score}")
    print(f"Strength Level: {color}{level}{COLORS['reset']}")
    print(display_meter(score))
