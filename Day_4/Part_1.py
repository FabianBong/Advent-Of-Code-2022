file = open('Day_4/input.txt', 'r')
lines = file.readlines()
lines = [l.strip("\n") for l in lines]

score = 0

for l_ in lines:
    (low_1, up_1) = l_.split(",")[0].split("-")
    (low_2, up_2) = l_.split(",")[1].split("-")

    if int(low_1) >= int(low_2) and int(up_1) <= int(up_2):
        score = score + 1
    elif int(low_2) >= int(low_1) and int(up_2) <= int(up_1):
        score = score + 1

print(score)