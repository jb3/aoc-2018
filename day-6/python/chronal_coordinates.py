#!/usr/bin/env python

import itertools
from collections import namedtuple

Point2DBase = namedtuple("Point2D", ["x", "y"])


class Point2D(Point2DBase):
    infinite = False

    @classmethod
    def from_text(cls, data: str):
        x, y = data.split(",")
        y = int(y.strip())
        x = int(x)

        return cls(x, y)

    def distance_from(self, point):
        return abs(self.x - point.x) + abs(self.y - point.y)


with open("input.txt", "r") as f:
    coordinates = [l.strip() for l in f.readlines()]

points = []

for coordinate in coordinates:
    points.append(Point2D.from_text(coordinate))

sorted_y = sorted(points, key=lambda point: point.y)

min_y = sorted_y[0].y
max_y = sorted_y[::-1][0].y

sorted_x = sorted(points, key=lambda point: point.x)

min_x = sorted_x[0].x
max_x = sorted_x[::-1][0].x

grid_points = {point: 0 for point in points}


for x, y in itertools.product(range(min_x, max_x + 1), range(min_y, max_y + 1)):
    point = Point2D(x, y)

    closest_point = map(lambda p: (p, p.distance_from(point)), points)

    sorted_points = sorted(closest_point, key=lambda x: x[1])

    if point.x in {min_x, max_x} or point.y in {min_y, max_y}:
        points[points.index(sorted_points[0][0])].infinite = True
        continue

    if sorted_points[0][0].infinite:
        continue

    if sorted_points[0][1] == sorted_points[1][1]:
        continue

    grid_points[sorted_points[0][0]] += 1

aoc_part_1_answer = sorted(
    grid_points.items(), key=lambda point: point[1], reverse=True
)[0][1]

print(f"AoC part 1 answer: {aoc_part_1_answer}")

safe_locations = 0

for x, y in itertools.product(range(min_x, max_x), range(min_y, max_y)):
    p = Point2D(x, y)
    distance = 0
    for point in points:
        distance += point.distance_from(p)

    if distance < 10000:
        safe_locations += 1

print(f"AoC part 2 answer: {safe_locations}")
