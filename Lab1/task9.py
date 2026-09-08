text = "A man a plan a canal Panama"

cleanedText = ""
for character in text:
    if character != " ":
        cleanedText = cleanedText + character.lower()

reversedText = cleanedText[::-1]

print("String:", text)
if cleanedText == reversedText:
    print("Palindrome")
else:
    print("Not a palindrome")
