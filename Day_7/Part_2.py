class NonBinTree:

    def __init__(self, val, parent):
        self.val = val
        self.nodes = []
        self.parent = parent

    def add_node(self, val):
        self.nodes.append(NonBinTree(val,self))

    def get_node_by_name(self,name):
        for node in self.nodes:
            if node.get_value().get_name() == name:
                return node

    def get_parent(self):
        return self.parent

    def get_value(self):
        return self.val

    @staticmethod
    def part_2_answer(start_node, needed, opt):
        if start_node.get_value().get_type()==1:
                if start_node.get_value().get_size()>=needed:
                    #print(start_node.get_value().get_size())
                    opt.append(start_node.get_value().get_size())
        for node in start_node.nodes:
            NonBinTree.part_2_answer(node, needed,opt)


    def __repr__(self):
        return f"NonBinTree({self.val}): {self.nodes}"


class File:

    def __init__(self, name, size, type):
        self.name = name
        self.size = size
        self.type = type
    
    def get_size(self):
        return self.size

    def get_name(self):
        return self.name

    def set_size(self, size):
        self.size = self.size + int(size)

    def get_type(self):
        return self.type

    def __repr__(self):
        return f"File: {self.name}, size: {self.size}"

file = open('Day_7/input.txt', 'r')
lines = file.readlines()
lines = [l.strip("\n") for l in lines]

cur = NonBinTree(File(lines.pop(0).strip("$ cd"),0,1), None)

for l_ in lines:
    if l_ == "$ ls":
        continue
    if l_[0:4] == "$ cd":
        if l_.strip("$ cd") == "..":
            cur = cur.get_parent()
        else:
            val = l_.replace("$ cd","").strip(" ")
            cur = cur.get_node_by_name(val)
    if l_[0] != "$":
        if l_[0:3] == "dir":
            val = l_.replace("dir","").strip(" ")
            cur.add_node(File(val,0,1))
        else:
            (size, name) = l_.split(".")[0].split(" ")
            cur.add_node(File(name,size,0))
            cur.get_value().set_size(size)
            par = cur.get_parent()
            while(par != None):
                par.get_value().set_size(size)
                par = par.get_parent()


while(cur.get_parent() != None):
    cur = cur.get_parent()

#print(30000000 - (70000000-cur.get_value().get_size()))
test = []
NonBinTree.part_2_answer(cur, 30000000 - (70000000-cur.get_value().get_size()),test)
print(min(test))
#a = NonBinTree(0)
#a.add_node(1)
#a.add_node(3)
#a.add_node(4)
#a.nodes[2].add_node(2)

#print(cur)