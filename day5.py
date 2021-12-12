#!/usr/local/bin/python3

import re
import sys

input = open("day5_input.txt").readlines()
max_coordinate = 0

lines = []

def is_horizontal_or_vertical(x1, y1, x2, y2):
    return x1 == x2 or y1 == y2

def is_45_degree_diagonal(x1, y1, x2, y2):
    return abs(x1 - x2) == abs(y1 - y2)

for line in input:
    p = re.compile(r'(\d+),(\d+) -> (\d+),(\d+)')
    m = p.match(line)
    x1 = int(m.group(1))
    y1 = int(m.group(2))
    x2 = int(m.group(3))
    y2 = int(m.group(4))
    if not (is_horizontal_or_vertical(x1, y1, x2, y2)):
    # if not (is_horizontal_or_vertical(x1, y1, x2, y2) or is_45_degree_diagonal(x1, y1, x2, y2)):
        continue

    lines.append([x1,y1, x2,y2])
    max_c = max(x1,x2,y1,y2)
    if max_c > max_coordinate:
        max_coordinate = max_c
    # print(f"{x1},{y1} {x2},{y2} {max_coordinate}")


field = [[0 for x in range(max_coordinate+1)] for y in range(max_coordinate+1)]

def print_field(field):
    for line in field:
        for num in line:
            if num == 0:
                print(".", end="")
            else:
                print(num, end="")
        print()

for line in lines:
    x1, y1, x2, y2 = line
    if x1 == x2:
        for y in range(min(y1,y2), max(y1,y2)+1):
            field[y][x1] += 1
    if y1 == y2:
        for x in range(min(x1,x2), max(x1,x2)+1):
            field[y1][x] += 1
    if is_45_degree_diagonal(x1, y1, x2, y2):
        for y in range(min(y1,y2), max(y1,y2)+1):
            for x in range(min(x1,x2), max(x1,x2)+1):
                field[y][x] += 1

count2 = 0
for line in field:
    for c in line:
        if c > 1:
            count2 += 1
print(f"count2: {count2}")