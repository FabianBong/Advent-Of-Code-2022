file = open('Day_2/input.txt', 'r')
lines = file.readlines()

points_for_choice = {"X":1, "Y":2, "Z":3}
outcome = {"A,X":3, "A,Y":4, "A,Z":8,
            "B,X":1, "B,Y":5, "B,Z":9,
            "C,X":2, "C,Y":6, "C,Z":7}

score = 0
for l_ in lines:
    if l_ == "\n":
        continue
    (other,out) = l_.split(' ')
    out = out.strip('\n')
    score = score + outcome[other + "," + out]

print(score)