def print_situation(used, s_x,s_y,e_x,e_y):
    for i in range(s_y,e_y):
        p_string = ""
        for j in range(s_x, e_x):
            if(j,i) in used:
                p_string += " # "
            else:
                p_string += " . "
        print(p_string)

file = open('Day_14/input.txt', 'r')
lines = file.readlines()
lines = [l.strip("\n") for l in lines]

rock = set()

min = -1;

for l_ in lines:
    coords = l_.split(" -> ")
    for i in range(len(coords)-1):
        cur = coords[i].split(",")
        cur_plus = coords[i+1].split(",")
        if int(cur[1]) > min:
            min = int(cur[1])
        if int(cur_plus[1]) > min:
            min = int(cur_plus[1])
        dif_x = int(cur[0]) - int(cur_plus[0])
        dif_y = int(cur[1]) - int(cur_plus[1])
        if dif_x < 0:
            for j in range(int(cur[0]), int(cur_plus[0])+1,1):
                rock.add((j,int(cur_plus[1])))
        elif dif_x > 0:
            for j in range(int(cur_plus[0]), int(cur[0])+1,1):
                rock.add((j,int(cur_plus[1])))
        if dif_y < 0:
            for j in range(int(cur[1]), int(cur_plus[1])+1,1):
                rock.add((int(cur_plus[0]),j))
        if dif_y > 0:
            for j in range(int(cur_plus[1]), int(cur[1])+1,1):
                rock.add((int(cur_plus[0]),j))


for i in range(0,1000):
    rock.add((i,min+2))

count_sand = 0
notDone = True
while notDone:
    cur_corn = (500,0)
    while True:

        if (cur_corn[0], cur_corn[1]+1) not in rock:
             cur_corn = (cur_corn[0], cur_corn[1]+1)
        elif (cur_corn[0]-1, cur_corn[1]+1) not in rock:
            cur_corn = (cur_corn[0]-1, cur_corn[1]+1)
        elif (cur_corn[0]+1, cur_corn[1]+1) not in rock:
            cur_corn = (cur_corn[0]+1, cur_corn[1]+1)
        else:
            if cur_corn == (500,0):
                notDone = False
            rock.add(cur_corn)
            break

    count_sand += 1
    #print_situation(rock,494,0,510,15)

print(count_sand)