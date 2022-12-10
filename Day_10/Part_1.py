file = open('Day_10/input.txt', 'r')
lines = file.readlines()
lines = [l.strip("\n") for l in lines]

X = 1
cycle = 0
signal_strength = 0
checkpoints = [20, 60, 100, 140, 180, 220]

for l in lines:
    if l == 'noop':
        cycle += 1
        if cycle in checkpoints:
            signal_strength += cycle * X
            checkpoints.pop(0)
        continue
    value = int(l.replace("addx ", ""))
    for i in [1,1]:
        cycle += i
        if cycle in checkpoints:
            signal_strength += cycle * X
            checkpoints.pop(0)
    X += value

print(signal_strength)