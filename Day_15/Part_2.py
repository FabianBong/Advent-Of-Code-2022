import re

file = open('Day_15/input.txt', 'r')
lines = file.readlines()
lines = [l.strip("\n") for l in lines]

sensor_beacons = [re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", l) for l in lines]
sensor_beacons = [[(int(l[0]),int(l[1])),(int(l[2]),int(l[3]))] for l in sensor_beacons]

range_size = 10000
for j in range(0,range_size):
    if j % 100:
        print(j)
    beacon_in_line_set = set()
    sensor_in_line_set = set()
    ranges = []
    line_of_interest = j
    for sensor,beacon in sensor_beacons:
        abs_diff_x = abs(sensor[0] - beacon[0])
        abs_diff_y = abs(sensor[1] - beacon[1])
        max_diff = abs_diff_x if abs_diff_x > abs_diff_y else abs_diff_y
        other_diff = abs_diff_x + abs_diff_y
        if sensor[1] - other_diff <= line_of_interest <= sensor[1]:
            dist = sensor[1] - line_of_interest
            if dist == 0:
                ranges.append((sensor[0]-other_diff,sensor[0]+other_diff))
            else:
                ranges.append((sensor[0]-(other_diff-dist),sensor[0]+(other_diff-dist)))
        if sensor[1] + other_diff >= line_of_interest >= sensor[1]:
            dist = line_of_interest - sensor[1]
            if dist == 0:
                ranges.append((sensor[0]-other_diff,sensor[0]+other_diff))
            else:
                ranges.append((sensor[0]-((other_diff)-dist),sensor[0]+(other_diff-dist)))
    checked = set()
    for r in ranges:
        for i in range(r[0],r[1]+1):
            if i >= 0 and i <= range_size:
                checked.add(i)
    if(len(checked) != range_size+1):
        break

for i in range(range_size+1):
    if i not in checked:
        print(i)
        print(j)
