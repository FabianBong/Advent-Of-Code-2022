import numpy as np
import matplotlib.pyplot as  plt

file = open('Day_10/input.txt', 'r')
lines = file.readlines()
lines = [l.strip("\n") for l in lines]

X = 1
cycle = 0
drawing = np.full(240, '.')

for l in lines:
    if l == 'noop':
        if cycle%40 >= X-1 and cycle%40 <= X+1:
            drawing[cycle] = "#"
        else:
            drawing[cycle] = "." 
        cycle += 1
        continue
    value = int(l.replace("addx ", ""))
    for i in [1,1]:        
        if cycle%40 >= X-1 and cycle%40 <= X+1:
            drawing[cycle] = "#"
        else:
            drawing[cycle] = "."
        cycle += i
    print(cycle)
    X += value

matrix = drawing.reshape(6, 40)
matrix_imshow = matrix
matrix_imshow[matrix_imshow == "#"] = 1
matrix_imshow[matrix_imshow == "."] = 0
plt.imshow(matrix_imshow.astype('float'))
plt.show()