#!/usr/local/bin/python3

input = open("day6_input.txt").read().split(",")
fish = dict((int(days), 0) for days in range(9))
for days in input:
    if int(days) in fish:
        fish[int(days)] += 1
    else:
        fish[int(days)] = 1

print(fish)

def simulate(fish, num_days):
    for d in range(num_days):
        print(f"day {d}")
        fish2 = dict((int(days), 0) for days in range(9))
        for d in range(8):
            fish2[d] = fish[d+1]
        fish2[8] += fish[0]
        fish2[6] += fish[0]
        fish = fish2
        print(fish)
    print(sum(fish.values()))

# simulate(fish, 18)
# simulate(fish, 80)
simulate(fish, 256)