import re
import math
import getpass

# Common weak passwords
common_passwords = [
    "password",
    "123456",
    "12345678",
    "123456789",
    "qwerty",
    "admin",
    "letmein",
    "welcome",
    "password123",
    "abc123"
]

print("=" * 45)
print("       PASSWORD SECURITY CHECKER")
print("=" * 45)

# Hide password while typing
password = getpass.getpass("Enter your password: ")

score = 0
suggestions = []

# -------------------------------
# 1. Length Check
# -------------------------------

length = len(password)

if length >= 16:
    score += 25
    length_status = "Excellent"
elif length >= 12:
    score += 20
    length_status = "Good"
elif length >= 8:
    score += 10
    length_status = "Okay"
else:
    length_status = "Too Short"
    suggestions.append("Use at least 8 characters.")

# -------------------------------
# 2. Uppercase Check
# -------------------------------

if re.search(r"[A-Z]", password):
    score += 15
    uppercase = "Yes"
else:
    uppercase = "No"
    suggestions.append("Add uppercase letters (A-Z).")

# -------------------------------
# 3. Lowercase Check
# -------------------------------

if re.search(r"[a-z]", password):
    score += 15
    lowercase = "Yes"
else:
    lowercase = "No"
    suggestions.append("Add lowercase letters (a-z).")

# -------------------------------
# 4. Number Check
# -------------------------------

if re.search(r"[0-9]", password):
    score += 15
    number = "Yes"
else:
    number = "No"
    suggestions.append("Add numbers (0-9).")

# -------------------------------
# 5. Special Character Check
# -------------------------------

if re.search(r"[^A-Za-z0-9]", password):
    score += 20
    special = "Yes"
else:
    special = "No"
    suggestions.append("Add special characters such as @, #, $, !.")

# -------------------------------
# 6. Common Password Check
# -------------------------------

if password.lower() in common_passwords:
    score = min(score, 20)
    common = "YES - Very Risky"
    suggestions.append("Avoid common passwords.")
else:
    common = "No"

# -------------------------------
# 7. Repeated Character Check
# -------------------------------

if re.search(r"(.)\1\1", password):
    score -= 10
    suggestions.append("Avoid repeating the same character many times.")

# -------------------------------
# 8. Sequential Characters Check
# -------------------------------

sequences = [
    "1234",
    "2345",
    "3456",
    "4567",
    "5678",
    "6789",
    "abcd",
    "bcde",
    "cdef",
    "qwer",
    "asdf"
]

if any(seq in password.lower() for seq in sequences):
    score -= 10
    suggestions.append("Avoid predictable sequences like 1234 or abcde.")

# Keep score between 0 and 100
score = max(0, min(score, 100))

# -------------------------------
# 9. Entropy Estimation
# -------------------------------

character_set = 0

if re.search(r"[a-z]", password):
    character_set += 26

if re.search(r"[A-Z]", password):
    character_set += 26

if re.search(r"[0-9]", password):
    character_set += 10

if re.search(r"[^A-Za-z0-9]", password):
    character_set += 32

if character_set > 0:
    entropy = length * math.log2(character_set)
else:
    entropy = 0

# -------------------------------
# 10. Strength Level
# -------------------------------

if score < 30:
    strength = "VERY WEAK"
elif score < 50:
    strength = "WEAK"
elif score < 70:
    strength = "MEDIUM"
elif score < 90:
    strength = "STRONG"
else:
    strength = "VERY STRONG"

# -------------------------------
# Results
# -------------------------------

print("\n" + "=" * 45)
print("             SECURITY REPORT")
print("=" * 45)

print(f"\nPassword Length : {length}")
print(f"Length Status   : {length_status}")
print(f"Uppercase       : {uppercase}")
print(f"Lowercase       : {lowercase}")
print(f"Numbers         : {number}")
print(f"Special Chars   : {special}")
print(f"Common Password : {common}")

print(f"\nSecurity Score  : {score}/100")
print(f"Strength        : {strength}")
print(f"Estimated Entropy: {entropy:.2f} bits")

# -------------------------------
# Suggestions
# -------------------------------

print("\n" + "-" * 45)
print("SECURITY SUGGESTIONS")
print("-" * 45)

if suggestions:
    for suggestion in suggestions:
        print("• " + suggestion)
else:
    print("✓ Excellent! No major weaknesses detected.")

print("\n" + "=" * 45)
print("        PASSWORD CHECK COMPLETE")
print("=" * 45)