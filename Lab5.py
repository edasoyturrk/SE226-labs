import random
import string
passwords = []
for _ in range(5):
    password = ''.join(random.choices(string.ascii_lowercase, k=15))
    passwords.append(password)


mapping = {}
selectedChars = set()


while len(selectedChars) < 5:
    char = input("Enter a lowercase character: ")
    if char in selectedChars or char not in string.ascii_lowercase:
        print("Invalid or duplicate character, try again.")
        continue
    
    selectedChars.add(char)
    replacements = set()
    while len(replacements) < 3:
        replacement = input(f"Enter a replacement for '{char}': ")
        if len(replacement) != 1 or replacement in replacements:
            print("Invalid or duplicate replacement, try again.")
            continue
        replacements.add(replacement)
    
    mapping[char] = list(replacements)

categorizedPasswords = {"strong": [], "weak": []}

for password in passwords:
    updatedPassword = ""
    replacedCount = 0
    
    for char in password:
        if char in mapping:
            updatedPassword += random.choice(mapping[char])
            replacedCount += 1
        else:
            updatedPassword += char
    
    if replacedCount > 4:
        categorizedPasswords["strong"].append(updatedPassword)
    else:
        categorizedPasswords["weak"].append(updatedPassword)

print("\nGenerated Passwords:")
print("\nSTRONG PASSWORDS:")
for password in categorizedPasswords["strong"]:
    print(password)

print("\nWEAK PASSWORDS:")
for password in categorizedPasswords["weak"]:
    print(password)
