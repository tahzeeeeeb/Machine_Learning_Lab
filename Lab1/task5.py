text = "Hello World 123"

vowels = 0
consonants = 0
digits = 0
spaces = 0

for character in text:
    if character == " ":
        spaces = spaces + 1
    elif character.isdigit():
        digits = digits + 1
    elif character.lower() in "aeiou":
        vowels = vowels + 1
    elif character.isalpha():
        consonants = consonants + 1

print("String:", text)
print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Spaces:", spaces)
