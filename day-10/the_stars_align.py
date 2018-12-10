#!/usr/bin/env python

####################
# This is HORRIBLE #
####################

# Several flaws with my implementation:
#     - can't tell if stars are moving apart again
#     - user must be watching the logs to see the message appear
#     - pretty slow
#     - help

from sky import Sky, Star

with open("input.txt", "r") as f:
    star_text = [l.strip() for l in f.readlines()]


stars = []

for star in star_text:
    stars.append(Star.from_text(star))

sky = Sky(stars)

seconds = -1

while True:
    seconds += 1
    if sky.contains_negative_values(seconds):
        if seconds % 1000 == 0:
            print(f"Second {seconds} contained negative values, not printing.")
        continue

    print(f"Message at {seconds}")
    sky.print(seconds)
    