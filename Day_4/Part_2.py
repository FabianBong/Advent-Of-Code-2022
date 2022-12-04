import numpy as np

file = open('Day_4/input.txt', 'r')
lines = file.readlines()
lines = [l.strip("\n") for l in lines]

score = 0

for l_ in lines:
    (low_1, up_1) = l_.split(",")[0].split("-")
    (low_2, up_2) = l_.split(",")[1].split("-")

    overlap = np.intersect1d(np.arange(int(low_1), int(up_1)+1,1),np.arange(int(low_2), int(up_2)+1,1))

    if len(overlap)>0:
        score = score + 1

print(score)