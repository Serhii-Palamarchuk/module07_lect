from collections import defaultdict

text = "missisipi"

letters = defaultdict(int)

for letter in text:
    letters[letter] += 1

print(letters)
