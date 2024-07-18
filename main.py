from nltk.corpus import words
from itertools import permutations

dictionary = words.words()

sides = [['o', 'n', 'z'], ['e', 'g', 'r'], ['i', 'j', 'a'], ['d', 'b', 'p']]

substring_to_exclude = set()

for sublist in sides:
    for letter in sublist:
        substring_to_exclude.add(letter + letter)

    for pair in permutations(sublist, 2):
        substring_to_exclude.add(pair[0] + pair[1])

required_letters = [letter for sublist in sides for letter in sublist]

result = [word for word in dictionary if set(word).issubset(required_letters)]
result = [word for word in result if not any(substring in word for substring in substring_to_exclude)]

print(result)
