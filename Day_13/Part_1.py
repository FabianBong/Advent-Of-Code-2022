import itertools  

file = open('Day_13/input.txt', 'r')
lines = file.readlines()
lines = [l.strip("\n") for l in lines]

def compare_lists(l1, l2):

    ## if l1 runs out first
    if l1 is None:
        return -1
    ## if l2 runs out first
    if l2 is None:
        return 1

    print(isinstance(l1, list))

    ## if both are integers
    if isinstance(l1, int) and isinstance(l2, int):
        if l1 < l2:
            return -1
        elif l1 > l2:
            return 1
        else:
            return 0

        
    ## if they are both lists
    elif isinstance(l1, list) and isinstance(l2, list):
        for l2, r2 in itertools.zip_longest(l1,l2):
            if (result := compare_lists(l2,r2)) != 0:
                return result
        return 0

    else:
        return compare_lists([l1] if isinstance(l1, int) else l1,
        [l2] if isinstance(l2, int) else l2)


def part_1(packets):
    score = 0
    cur = 1
    for i in range(0,len(packets),3):
        if compare_lists(eval(packets[i]), eval(packets[i + 1])) == -1:
            score += cur
        cur += 1
    return score


print(part_1(lines))