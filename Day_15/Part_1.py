import re

file = open('Day_15/input.txt', 'r')
lines = file.readlines()
lines = [l.strip("\n") for l in lines]

sensor_beacons = [re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", l) for l in lines]
sensor_beacons = [[(int(l[0]),int(l[1])),(int(l[2]),int(l[3]))] for l in sensor_beacons]

beacon_in_line_set = set()
ranges = []
line_of_interest = 2000000
for sensor,beacon in sensor_beacons:
    abs_diff_x = abs(sensor[0] - beacon[0])
    abs_diff_y = abs(sensor[1] - beacon[1])
    if beacon[1] == line_of_interest:
        beacon_in_line_set.add(beacon)
    max_diff = abs_diff_x if abs_diff_x > abs_diff_y else abs_diff_y
    if sensor[1] - max_diff <= line_of_interest <= sensor[1]:
        dist = sensor[1] - line_of_interest
        if dist == 0:
            ranges.append((sensor[0]-abs_diff_x,sensor[0]+abs_diff_x))
        else:
            ranges.append((sensor[0]-(abs_diff_x+(abs_diff_y)-dist),sensor[0]+(abs_diff_x+(abs_diff_y)-dist)))
    if sensor[1] + max_diff >= line_of_interest >= sensor[1]:
        dist = line_of_interest - sensor[1]
        if dist == 0:
            ranges.append((sensor[0]-abs_diff_x,sensor[0]+abs_diff_x))
        else:
            ranges.append((sensor[0]-((abs_diff_x+(abs_diff_y))-dist),sensor[0]+(abs_diff_x+(abs_diff_y)-dist)))

print(ranges)
checked = set()
for r in ranges:
    for i in range(r[0],r[1]+1):
        checked.add(i)

print(len(checked)-len(beacon_in_line_set))
print(len(beacon_in_line_set))