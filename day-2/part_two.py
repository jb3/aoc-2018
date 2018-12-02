#!/usr/bin/env python

import Levenshtein

with open("input.txt", "r") as f:
    boxes = [r.strip() for r in f.readlines()]
    
for line in boxes:
    for l in boxes:
        if line == l:
            continue
        
        if Levenshtein.distance(line, l) == 1:
            print(line)
            print(l)
            exit()
