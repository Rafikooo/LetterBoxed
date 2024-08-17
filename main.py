import json
import requests
import re
from itertools import permutations


def get_game_data():
    url = "https://www.nytimes.com/puzzles/letter-boxed"
    response = requests.get(url)

    start = "window.gameData = "
    stop = "</script>"
    pattern = rf"\{start}(.*?)\{stop}"
    match = re.search(pattern, response.text)

    return json.loads(match.group(1))


def get_sides():
    new_sides = []
    for i in get_game_data()["sides"]:
        new_sides.append(list(i.lower()))
    return new_sides


def get_dictionary():
    return [i.lower() for i in get_game_data()["dictionary"]]


def filter_words():
    substring_to_exclude = set()
    sides = get_sides()
    dictionary = get_dictionary()

    for sublist in sides:
        for letter in sublist:
            substring_to_exclude.add(letter + letter)

        for pair in permutations(sublist, 2):
            substring_to_exclude.add(pair[0] + pair[1])

    required_letters = [letter for sublist in sides for letter in sublist]

    result = [word for word in dictionary if set(word).issubset(required_letters)]
    result = [word for word in result if not any(substring in word for substring in substring_to_exclude)]
    result.sort(key=lambda x: len(x), reverse=True)

    return result


def main():
    search_partial = ''

    while search_partial != 'exit':
        search_partial = input()
        current_result = [word for word in filter_words() if word.startswith(search_partial)]
        print(current_result)


main()
