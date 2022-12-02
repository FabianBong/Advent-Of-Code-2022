file = open('Day_2/input.txt', 'r')
lines = file.readlines()

points_for_choice = {"X":1, "Y":2, "Z":3}
outcome = {"X,A":3, "X,B":0, "X,C":6,
            "Y,A":6, "Y,B":3, "Y,C":0,
            "Z,A":0, "Z,B":6, "Z,C":3}

score = 0
for l_ in lines:
    if l_ == "\n":
        continue
    (other,me) = l_.split(' ')
    me = me.strip('\n')
    score = score + points_for_choice[me]
    score = score + outcome[me + "," + other]

print(score)