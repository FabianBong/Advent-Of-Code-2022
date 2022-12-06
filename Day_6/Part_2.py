file = open('Day_6/input.txt', 'r')
lines = file.readlines()
lines = [l.strip("\n") for l in lines]
line = lines[0]

for i in range(14,len(line)):
    if len(set(line[i-14:i])) == 14:
        print(i)
        break
