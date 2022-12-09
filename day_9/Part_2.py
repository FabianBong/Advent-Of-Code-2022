import numpy as np
import matplotlib.pyplot as plt

file = open('Day_9/input_test.txt', 'r')
lines = file.readlines()
lines = [l.strip("\n") for l in lines]

step_type = [l_.split(" ")[0] for l_ in lines]
step_length = [int(l_.split(" ")[1]) for l_ in lines]

pos_visited = set()
pos_h = (0,0)
pos_knots = [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),
            (0,0),(0,0)]

for i in range(1,9):
    print(i)

for ty,le in zip(step_type, step_length):
    for i in range(le):
        if ty == "R":
            pos_h = tuple(np.add(pos_h, (1,0)))
            if(tuple(np.subtract(pos_h ,pos_knots[0])) == (2,0)):
                pos_knots[0] = tuple(np.add(pos_knots[0], (1,0)))
            if(tuple(np.subtract(pos_h ,pos_knots[0])) == (2,-1)):
                pos_knots[0] = tuple(np.add(pos_knots[0], (1,-1)))
            if(tuple(np.subtract(pos_h ,pos_knots[0])) == (2,1)):
                pos_knots[0] = tuple(np.add(pos_knots[0], (1,1)))
                
        elif ty == "L":
            pos_h = tuple(np.add(pos_h, (-1,0)))
            if(tuple(np.subtract(pos_h ,pos_knots[0])) == (-2,0)):
                pos_knots[0] = tuple(np.add(pos_knots[0], (-1,0)))
            if(tuple(np.subtract(pos_h ,pos_knots[0])) == (-2,-1)):
                pos_knots[0] = tuple(np.add(pos_knots[0], (-1,-1)))
            if(tuple(np.subtract(pos_h ,pos_knots[0])) == (-2,1)):
                pos_knots[0] = tuple(np.add(pos_knots[0], (-1,1)))
                
        elif ty == "U":
            pos_h = tuple(np.add(pos_h, (0,1)))
            if(tuple(np.subtract(pos_h ,pos_knots[0])) == (0,2)):
                pos_knots[0] = tuple(np.add(pos_knots[0], (0,1)))
            if(tuple(np.subtract(pos_h ,pos_knots[0])) == (1,2)):
                pos_knots[0] = tuple(np.add(pos_knots[0], (1,1)))
            if(tuple(np.subtract(pos_h ,pos_knots[0])) == (-1,2)):
                pos_knots[0] = tuple(np.add(pos_knots[0], (-1,1)))

            #plt.clf()
            #plt.scatter(pos_h[0],pos_h[1])
            #[plt.scatter(v[0],v[1]) for v in pos_knots]
            #plt.ylim([-1, 10])
            #plt.xlim([-1, 8])
            #plt.show()


        elif ty == "D":
            pos_h = tuple(np.add(pos_h, (0,-1)))
            if(tuple(np.subtract(pos_h ,pos_knots[0])) == (0,-2)):
                pos_knots[0] = tuple(np.add(pos_knots[0], (0,-1)))
            if(tuple(np.subtract(pos_h ,pos_knots[0])) == (1,-2)):
                pos_knots[0] = tuple(np.add(pos_knots[0], (1,-1)))
            if(tuple(np.subtract(pos_h ,pos_knots[0])) == (-1,-2)):
                pos_knots[0] = tuple(np.add(pos_knots[0], (-1,-1)))
                
        for j in range(1,9):
            if(tuple(np.subtract(pos_knots[j-1] ,pos_knots[j])) == (0,-2)):
                pos_knots[j] = tuple(np.add(pos_knots[j], (0,-1)))
            elif(tuple(np.subtract(pos_knots[j-1] ,pos_knots[j])) == (1,-2)):
                pos_knots[j] = tuple(np.add(pos_knots[j], (1,-1)))
            elif(tuple(np.subtract(pos_knots[j-1] ,pos_knots[j])) == (-1,-2)):
                pos_knots[j] = tuple(np.add(pos_knots[j], (-1,-1)))
            elif(tuple(np.subtract(pos_knots[j-1] ,pos_knots[j])) == (0,2)):
                pos_knots[j] = tuple(np.add(pos_knots[j], (0,1)))
            elif(tuple(np.subtract(pos_knots[j-1] ,pos_knots[j])) == (1,2)):
                pos_knots[j] = tuple(np.add(pos_knots[j], (1,1)))
            elif(tuple(np.subtract(pos_knots[j-1] ,pos_knots[j])) == (-1,2)):
                pos_knots[j] = tuple(np.add(pos_knots[j], (-1,1)))
            elif(tuple(np.subtract(pos_knots[j-1] ,pos_knots[j])) == (-2,0)):
                pos_knots[j] = tuple(np.add(pos_knots[j], (-1,0)))
            elif(tuple(np.subtract(pos_knots[j-1] ,pos_knots[j])) == (-2,-1)):
                pos_knots[j] = tuple(np.add(pos_knots[j], (-1,-1)))
            elif(tuple(np.subtract(pos_knots[j-1] ,pos_knots[j])) == (-2,1)):
                pos_knots[j] = tuple(np.add(pos_knots[j], (-1,1)))
            elif(tuple(np.subtract(pos_knots[j-1] ,pos_knots[j])) == (2,0)):
                pos_knots[j] = tuple(np.add(pos_knots[j], (1,0)))
            elif(tuple(np.subtract(pos_knots[j-1] ,pos_knots[j])) == (2,-1)):
                pos_knots[j] = tuple(np.add(pos_knots[j], (1,-1)))
            elif(tuple(np.subtract(pos_knots[j-1] ,pos_knots[j])) == (2,1)):
                pos_knots[j] = tuple(np.add(pos_knots[j], (1,1)))
            elif(tuple(np.subtract(pos_knots[j-1] ,pos_knots[j])) == (2,2)):
                pos_knots[j] = tuple(np.add(pos_knots[j], (1,1)))
            elif(tuple(np.subtract(pos_knots[j-1] ,pos_knots[j])) == (-2,2)):
                pos_knots[j] = tuple(np.add(pos_knots[j], (-1,1)))
            elif(tuple(np.subtract(pos_knots[j-1] ,pos_knots[j])) == (-2,-2)):
                pos_knots[j] = tuple(np.add(pos_knots[j], (-1,-1)))
            elif(tuple(np.subtract(pos_knots[j-1] ,pos_knots[j])) == (2,-2)):
                pos_knots[j] = tuple(np.add(pos_knots[j], (1,-1)))
            #plt.clf()
            #plt.scatter(pos_h[0],pos_h[1])
            #[plt.scatter(v[0],v[1]) for v in pos_knots]
            #plt.ylim([-1, 10])
            #plt.xlim([-1, 8])
            #plt.show()

        plt.clf()
        plt.scatter(pos_h[0],pos_h[1])
        [plt.scatter(v[0],v[1]) for v in pos_knots]
        plt.ylim([-100, 100])
        plt.xlim([-100, 100])
        plt.show()
        print(pos_knots)
        pos_visited.add(pos_knots[8])

print(len(pos_visited))