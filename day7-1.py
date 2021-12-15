#!/usr/local/bin/python3

input = open("day7_input.txt").read().split(",")
h_positions = [int(pos) for pos in input]

# h_position_avg = round(sum(h_positions) / len(h_positions))
# print(h_position_avg)

# h_position_avg = 2
best = (None, None)
max_h_pos = max(h_positions) + 1
for pos_target in range(max_h_pos):
    fuel = sum([abs(pos - pos_target) for pos in h_positions])
    if best[1]:
        if fuel < best[1]:
            best = pos_target, fuel
    else:
        best = pos_target, fuel
    print(f"{pos_target}: {fuel}")
print(best)