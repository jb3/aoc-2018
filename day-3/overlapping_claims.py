#!/usr/bin/env python

import re

CLAIM_RE = re.compile(r"#(\d+) @ (\d+),(\d+): (\d+)x(\d+)")


class Claim:
    def __init__(self, claim_id, left, top, width, height):
        self.claim_id = claim_id
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.covered_squares = set()

        for row in range(width):
            for column in range(height):
                self.covered_squares.add((row + left, column + top))

    @classmethod
    def from_text(cls, data):
        match = CLAIM_RE.match(data)
        if match is None:
            raise Exception("Invalid claim string specified")

        groups = [int(x) for x in match.groups()]

        return cls(*groups)

    def __repr__(self):
        return (
            f"Claim(claim_id={self.claim_id}, "
            f"left={self.left}, "
            f"top={self.top}, "
            f"width={self.width}, "
            f"height={self.height})"
        )


with open("input.txt", "r") as f:
    claims = [line.strip() for line in f.readlines()]

claim_list = []

claimed_squares = set()

for claim in claims:
    clm = Claim.from_text(claim)
    claim_list.append(clm)

overlapping_inches = 0
overlapping_squares = set()

for clm in claim_list:
    for square in clm.covered_squares:
        if square in claimed_squares and square not in overlapping_squares:
            overlapping_inches += 1
            overlapping_squares.add(square)

        claimed_squares.add(square)

print(overlapping_inches)

for clm in claim_list:
    for square in clm.covered_squares:
        if square in overlapping_squares:
            break
    else:
            print(clm)
