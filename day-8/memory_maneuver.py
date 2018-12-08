#!/usr/bin/env python

import sys
from collections import deque
from dataclasses import dataclass

# fuck you stack traces
sys.setrecursionlimit(100_000_000)


@dataclass
class Node:
    children: list
    metadata: list
    value: int


with open("input.txt", "r") as f:
    tree_data = deque([int(f) for f in f.read().split(" ")])

metadata = deque()


def parse_node(data):
    child_count, metadata_count = tree_data.popleft(), tree_data.popleft()

    children = []
    if child_count > 0:
        for i in range(child_count):
            children.append(parse_node(data))

    meta = []
    value = 0
    for i in range(metadata_count):
        m = data.popleft()
        meta.append(m)
        metadata.append(m)

        if len(children) >= m:
            value += children[m - 1].value

    if len(children) == 0:
        value = sum(meta)

    return Node(children=children, metadata=meta, value=value)


if __name__ == "__main__":
    root_node = parse_node(tree_data)
    print(f"AoC part 1 answer: {sum(metadata)}")
    print(f"AoC part 2 answer: {root_node.value}")
