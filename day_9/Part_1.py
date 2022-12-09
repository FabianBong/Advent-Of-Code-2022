import numpy as np

file = open('Day_9/input.txt', 'r')
lines = file.readlines()
lines = [l.strip("\n") for l in lines]

step_type = [l_.split(" ")[0] for l_ in lines]
step_length = [int(l_.split(" ")[1]) for l_ in lines]

pos_visited = set()
pos_h = (0,0)
pos_t = (0,0)

for ty,le in zip(step_type, step_length):
    for i in range(le):
        if ty == "R":
            pos_h = tuple(np.add(pos_h, (1,0)))
            if(tuple(np.subtract(pos_h ,pos_t)) == (2,0)):
                pos_t = np.add(pos_t, (1,0))
            if(tuple(np.subtract(pos_h ,pos_t)) == (2,-1)):
                pos_t = np.add(pos_t, (1,-1))
            if(tuple(np.subtract(pos_h ,pos_t)) == (2,1)):
                pos_t = np.add(pos_t, (1,1))
        elif ty == "L":
            pos_h = tuple(np.add(pos_h, (-1,0)))
            if(tuple(np.subtract(pos_h ,pos_t)) == (-2,0)):
                pos_t = np.add(pos_t, (-1,0))
            if(tuple(np.subtract(pos_h ,pos_t)) == (-2,-1)):
                pos_t = np.add(pos_t, (-1,-1))
            if(tuple(np.subtract(pos_h ,pos_t)) == (-2,1)):
                pos_t = np.add(pos_t, (-1,1))
        elif ty == "U":
            pos_h = tuple(np.add(pos_h, (0,1)))
            if(tuple(np.subtract(pos_h ,pos_t)) == (0,2)):
                pos_t = np.add(pos_t, (0,1))
            if(tuple(np.subtract(pos_h ,pos_t)) == (1,2)):
                pos_t = np.add(pos_t, (1,1))
            if(tuple(np.subtract(pos_h ,pos_t)) == (-1,2)):
                pos_t = np.add(pos_t, (-1,1))
        elif ty == "D":
            pos_h = tuple(np.add(pos_h, (0,-1)))
            if(tuple(np.subtract(pos_h ,pos_t)) == (0,-2)):
                pos_t = np.add(pos_t, (0,-1))
            if(tuple(np.subtract(pos_h ,pos_t)) == (1,-2)):
                pos_t = np.add(pos_t, (1,-1))
            if(tuple(np.subtract(pos_h ,pos_t)) == (-1,-2)):
                pos_t = np.add(pos_t, (-1,-1))

        pos_t = tuple(pos_t)
        pos_visited.add(pos_t)

print(len(pos_visited))