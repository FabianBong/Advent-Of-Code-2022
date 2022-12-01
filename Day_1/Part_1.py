file = open('Day_1/input.txt', 'r')
lines = file.readlines()

elves_cal = []
cur_cal = 0

for l_ in lines:
    if l_ == "\n":
        elves_cal.append(cur_cal)
        cur_cal = 0
        continue
    cur_cal = cur_cal + int(l_)
    
print(max(elves_cal))