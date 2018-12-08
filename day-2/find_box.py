#!/usr/bin/env python

with open("input.txt", "r") as f:
    boxes = [r.strip() for r in f.readlines()]

three_times = 0
two_times = 0

for box in boxes:
    found_three = False
    found_two = False
    for letter in box:
        if box.count(letter) == 3 and not found_three:
            three_times += 1
            found_three = True
            continue

        if box.count(letter) == 2 and not found_two:
            found_two = True
            two_times += 1

print(f"AoC part 1 answer: {three_times * two_times}")
