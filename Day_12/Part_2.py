import sys

class Cell:
    def __init__(self, x, y, dist, prev, value) :
        self.x = x
        self.y = y
        self.dist = dist; 
        self.prev = prev;
        self.value = value;
    def __str__(self):
        return "("+ str(self.x) + "," + str(self.y) + ")" 

class ShortestPathBetweenCellsBFS:

    def shortestPath(self, matrix, start):
        sx = start[0]
        sy = start[1]

        m = len(matrix)
        n = len(matrix[0])
        
        cells = []
        for i in range(0,m):
            row = []
            for j in range(0,n):
                if(matrix[i][j] == "S"):
                    row.append(Cell(i, j, sys.maxsize,None, "a"))
                elif matrix[i][j] == "E":
                    row.append(Cell(i, j, sys.maxsize,None, "z"))
                else:
                    row.append(Cell(i, j, sys.maxsize,None, matrix[i][j]))
            cells.append(row)

        queue = []
        src = cells[sx][sy]
        src.dist = 0
        queue.append(src)
        dest = None
        p = queue.pop(0)
        while p != None:
            if matrix[p.x][p.y] == "E":
                dest = p
                break

            self.visit(cells, queue, p.x-1, p.y, p)    
            self.visit(cells, queue, p.x, p.y-1, p)     
            self.visit(cells, queue, p.x+1, p.y, p)             
            self.visit(cells, queue, p.x, p.y+1, p)
            if len(queue) > 0:
                p = queue.pop(0)
            else:
                p = None     
        path = []
        p = dest
        while p != None :
            path.insert(0, p)	      
            p = p.prev	       
        return len(path)-1
             


    def visit(self, cells, queue, x, y, parent):
        if x < 0 or x>= len(cells) or y < 0 or y>= len(cells[0]):
            return
        
        if (ord(cells[x][y].value)) - ord(parent.value) <= 1:
            dist = parent.dist + 1
            p = cells[x][y]
            if dist < p.dist:
                p.dist = dist
                p.prev = parent
                queue.append(p)


file = open('Day_12/input.txt', 'r')
lines = file.readlines()
lines = [l.strip("\n") for l in lines]

all_a = []

for i in range(len(lines)):
    for j in range(len(lines[0])):
        if lines[i][j] in ["a","S"]:
            all_a.append((i,j))

dist = []
for flat in all_a:
    shortest = ShortestPathBetweenCellsBFS()
    start= [flat[0],flat[1]]

    dist_opt = shortest.shortestPath(lines,start)
    if dist_opt != -1:
        dist.append(dist_opt)

print(sorted(dist)[0])
