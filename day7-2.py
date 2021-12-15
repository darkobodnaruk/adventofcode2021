#!/usr/local/bin/python3

input = open("day7_input.txt").read().split(",")
h_positions = [int(pos) for pos in input]

def calc_fuel(pos, pos_target):
    d = abs(pos - pos_target)
    return int((d + 1) * d / 2)

# h_position_avg = 2
best = (None, None)
max_h_pos = max(h_positions) + 1
for pos_target in range(max_h_pos):
    fuel = sum([calc_fuel(pos, pos_target) for pos in h_positions])
    if best[1]:
        if fuel < best[1]:
            best = pos_target, fuel
    else:
        best = pos_target, fuel
    # print(f"{pos_target}: {fuel}")
print(best)