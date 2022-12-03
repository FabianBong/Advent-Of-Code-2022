file = open('Day_3/input.txt', 'r')
lines = file.readlines()

def get_score(letter):
    if letter.isupper():
        return (ord(letter) - 65 + 27)
    else:
        return (ord(letter) - 97 + 1)

score = 0
for l_ in lines:
    l_ = l_.strip('\n')
    l_length = int(len(l_))
    l_1 = [str(c) for c in l_[0:int(l_length/2)]]
    l_2 = [str(c) for c in l_[int(l_length/2):l_length]]
    overlap = [value for value in l_1 if value in l_2]
    score = score + get_score(overlap[0])

print(score)