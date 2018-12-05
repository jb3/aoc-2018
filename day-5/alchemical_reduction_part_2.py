#!/usr/bin/env python

import string
import multiprocessing

with open("input.txt", "r") as f:
    polymer = f.read().strip()


def find_reactions(poly: str):
    """
    Find some reacting units (e.g. eE or Ee)
    """
    for character in string.ascii_lowercase:
        lower_upper = character + character.upper()
        upper_lower = character.upper() + character
        if lower_upper in poly:
            return poly.find(lower_upper)
        elif upper_lower in poly:
            return poly.find(upper_lower)
    return None


def react_polymer(poly: str):
    while True:
        found_reaction = find_reactions(poly)
        if found_reaction is None:
            return poly

        poly = poly[:found_reaction] + poly[found_reaction + 2:]


def remove_and_react(letter: str):
    poly = polymer.replace(letter, "").replace(letter.upper(), "")
    poly = react_polymer(poly)

    return letter, len(poly)


if __name__ == "__main__":
    with multiprocessing.Pool(2) as p:
        polys = p.map(remove_and_react, string.ascii_lowercase)

    aoc_2_answer = sorted(polys, key=lambda x: x[1])[0]

    print(f"Part 2 answer: {aoc_2_answer[1]}")
