import random
import string

SPECIAL_CHARS = "!@#$%^&*"
CHAR_POOL = string.ascii_letters + string.digits + string.punctuation

STRENGTH_RATINGS = {
    (0, 2): "Weak",
    (3, 4): "Medium",
    (5, 6): "Strong",
    (7, 99): "Very Strong",
}



def get_rating(score: int) -> str:
    for (low, high), label in STRENGTH_RATINGS.items():
        if low <= score <= high:
            return label
    return "Unknown"



def analyze_password(password: str) -> tuple[int, list[str]]:
    """
    Evaluate password strength.
    Returns score, list_of_missing_criteria.
    Max possible score 7.
    """
    score = 0
    missing = []

    #Length scoring
    length = len(password)
    if length >= 16:
        score += 3
    elif length >= 12:
        score += 2
    elif length >= 8:
        score += 1
    else:
        missing.append("too short (need ≥ 8 characters)")

    # Character-type checks using a for loop 
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    for ch in password:          # for loop iterating over each character
        if ch.isupper():
            has_upper = True
        if ch.islower():
            has_lower = True
        if ch.isdigit():
            has_digit = True
        if ch in SPECIAL_CHARS:
            has_special = True

    if has_upper:
        score += 1
    else:
        missing.append("uppercase letter")

    if has_lower:
        score += 1
    else:
        missing.append("lowercase letter")

    if has_digit:
        score += 1
    else:
        missing.append("digit")

    if has_special:
        score += 1
    else:
        missing.append(f"special character ({SPECIAL_CHARS})")

    # No more than 2 repeated consecutive characters 
    has_triple_repeat = False
    for i in range(len(password) - 2):       # for loop with index
        if password[i] == password[i + 1] == password[i + 2]:
            has_triple_repeat = True
            break

    if not has_triple_repeat:
        score += 1
    else:
        missing.append("too many repeated consecutive characters")

    return score, missing


#random password generator
def generate_password(length: int) -> str:
    """Generate a random password of given length using a for loop."""
    password = ""
    for _ in range(length):          # for loop used for generation
        password += random.choice(CHAR_POOL)
    return password



def display_analysis(password: str, label: str = ""):
    score, missing = analyze_password(password)
    max_score = 7
    rating = get_rating(score)

    header = f"  [{label}] " if label else "  "
    print(f"{header}Strength: {score}/{max_score} ({rating})")

    if missing:
        print(f"  Missing : {', '.join(missing)}")
    else:
        print("  All criteria satisfied ✓")

    return score



def main():
    print("=" * 50)
    print("Password Strength Analyzer & Generator")
    print("=" * 50)

        
    print("\n📋 SECTION 1: Analyze Your Password")
    print("-" * 40)
    #Enter a password till strong
    while True:                              
        password = input("\nEnter password: ").strip()

        if not password:
            print("  ⚠  Password cannot be empty. Try again.")
            continue

        score = display_analysis(password)

        if score >= 5:
            print("Password accepted!\n")
            break
        else:
            print("Try again — aim for a score of at least 5.\n")

    #Generate a password
    print("\nSECTION 2: Generate a Secure Password")
    print("-" * 40)

    while True:
        try:
            gen_length = int(input("\nEnter desired password length (min 8): "))
            if gen_length < 8:
                print(" Length must be at least 8. Try again.")
                continue
            break
        except ValueError:
            print("Please enter a valid integer.")

    generated = generate_password(gen_length)
    print(f"\n  Generated Password : {generated}")
    display_analysis(generated, label="Generated")

    print("\n" + "=" * 50)


if __name__ == "__main__":
    main()
