#!/usr/bin/env python

import itertools

with open("input.txt", "r") as f:
    inputs = f.readlines()
    inputs = [int(inp.strip()) for inp in inputs]

frequency = 0

seen_freqs = set()

for number in inputs:
    frequency += number
    seen_freqs.add(frequency)

print(f"AoC part 1 answer: {frequency}")

for number in itertools.cycle(inputs):
    frequency += number
    if frequency in seen_freqs:
        break

print(f"AoC part 2 answer: {frequency}")
