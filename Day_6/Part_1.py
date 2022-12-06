file = open('Day_6/input.txt', 'r')
lines = file.readlines()
lines = [l.strip("\n") for l in lines]
line = lines[0]

for i in range(4,len(line)):
    if len(set(line[i-4:i])) == 4:
        print(i)
        break
