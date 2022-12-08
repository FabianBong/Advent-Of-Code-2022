file = open('Day_8/input.txt', 'r')
lines = file.readlines()
lines = [l.strip("\n") for l in lines]

visible_trees = (len(lines[0])-2)*2 + len(lines)*2

max_view = -1 

for j in range(1, len(lines)-1):
    for i in range(1,len(lines[0])-1):

        cur = int(lines[j][i])

        ## for left
        left_view_fac = 1
        offset = 1
        while i-offset >= 0 and cur > int(lines[j][i-offset]):
            if i-offset == 0:
                left_view_fac -= 1
            left_view_fac += 1
            offset += 1
        
        ## for right
        right_view_fac = 1
        offset = 1
        while i+offset < len(lines[0]) and cur > int(lines[j][i+offset]):
            if i+offset == len(lines[0])-1:
                right_view_fac -=1
            right_view_fac += 1
            offset += 1

        ## for up
        offset = 1
        up_view_fac = 1
        while j-offset >= 0 and cur > int(lines[j-offset][i]):
            if j-offset == 0:
                up_view_fac -= 1
            up_view_fac += 1
            offset += 1

        ## for down
        offset = 1
        down_view_fac = 1
        while j+offset < len(lines) and cur > int(lines[j+offset][i]):
            if j+offset == len(lines)-1:
                down_view_fac -=1
            down_view_fac += 1
            offset += 1

        view_score = left_view_fac * right_view_fac * up_view_fac * down_view_fac
        if view_score > max_view:
            max_view = view_score


print(max_view)