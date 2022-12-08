file = open('Day_8/input.txt', 'r')
lines = file.readlines()
lines = [l.strip("\n") for l in lines]

visible_trees = (len(lines[0])-2)*2 + len(lines)*2


for j in range(1, len(lines)-1):
    for i in range(1,len(lines[0])-1):
        next = 0
        cur = int(lines[j][i])

        ## for left
        offset = 1
        while i >= 0 and cur > int(lines[j][i-offset]):
            if i-offset == 0:
                visible_trees += 1
                next = 1
                break
            offset += 1
        
        ## for right
        offset = 1
        while i < len(lines[0]) and cur > int(lines[j][i+offset]) and next != 1:
            if i+offset == len(lines[0])-1:
                visible_trees += 1
                next = 1
                break
            offset += 1

        ## for up
        offset = 1
        while i >= 0 and cur > int(lines[j-offset][i]) and next != 1:
            if j-offset == 0:
                visible_trees += 1
                next = 1
                break
            offset += 1

        ## for up
        offset = 1
        while i < len(lines) and cur > int(lines[j+offset][i]) and next != 1:
            if j+offset == len(lines)-1:
                visible_trees += 1
                next = 1
                break
            offset += 1


print(visible_trees)