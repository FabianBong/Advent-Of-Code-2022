import re

file = open('Day_5/input.txt', 'r')
lines = file.readlines()
lines = [l.strip("\n") for l in lines]
lines = [l.replace("[","") for l in lines]
lines = [l.replace("]","") for l in lines]

space_count = 0
stacks = []
for c_ in lines[0]:
    if c_ == ' ':
        space_count += 1
        if space_count == 4:
            space_count = 0
            stacks.append([])
    else:
        space_count = 0
        stacks.append([])

print(stacks)

for l_ in lines: 
    if '1' in l_:
        break

    stack_count = 0
    for c_ in l_:
        if c_ == ' ':
            space_count += 1
            if space_count == 4:
                space_count = 0
                stack_count += 1
        else:
            space_count = 0
            stacks[stack_count].append(c_)
            stack_count += 1

print(stacks)
command_num_move = []
command_move_from = []
command_move_to = []

read = False
for l_ in lines:

    if read == True:
        nums = re.findall(r'\d+', l_)
        command_num_move.append(int(nums[0]))
        command_move_from.append(int(nums[1]))
        command_move_to.append(int(nums[2]))

    if l_ == "":
        read = True

print(command_move_to)

for num,fr,to in zip(command_num_move,command_move_from,command_move_to):
    for i in range(num-1,0-1,-1): 
        stacks[to-1].insert(0,stacks[fr-1].pop(i))
        

solution = ""
for stack in stacks:
    solution += stack[0]

print(solution)