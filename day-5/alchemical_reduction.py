#!/usr/bin/env python

import string

with open("input.txt", "r") as f:
    polymer = f.read().strip()

##########
# Part 1 #
##########


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


while True:
    found_reaction = find_reactions(polymer)
    if found_reaction is None:
        break

    polymer = polymer[:found_reaction] + polymer[found_reaction + 2:]

print(f"AoC Part 1 answer: {len(polymer)}")
