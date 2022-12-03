import numpy as np 

file = open('Day_3/input.txt', 'r')
lines = file.readlines()
lines = [l.strip("\n") for l in lines]

def get_score(letter):
    if letter.isupper():
        return (ord(letter) - 65 + 27)
    else:
        return (ord(letter) - 97 + 1)

score = 0
for i in np.arange(3,len(lines)+3,3):
    common = np.intersect1d(np.intersect1d(list(lines[i-1]),list(lines[i-2])), list(lines[i-3]))
    score = score + get_score(common[0])

print(score)