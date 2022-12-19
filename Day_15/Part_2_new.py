import re

def in_range(point,sensor,beacon):
    abs_diff_x = abs(sensor[0] - beacon[0])
    abs_diff_y = abs(sensor[1] - beacon[1])
    point_abs_diff_x = abs(sensor[0] - point[0])
    point_abs_diff_y = abs(sensor[1] - point[1])
    total_diff = abs_diff_x + abs_diff_y
    point_total_diff = point_abs_diff_x + point_abs_diff_y
    if point_total_diff > total_diff:
        return -1
    else:
        return 1

file = open('Day_15/input.txt', 'r')
lines = file.readlines()
lines = [l.strip("\n") for l in lines]

sensor_beacons = [re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", l) for l in lines]
sensor_beacons = [[(int(l[0]),int(l[1])),(int(l[2]),int(l[3]))] for l in sensor_beacons]

range_size = 4000000
for sensor,beacon in sensor_beacons:
        abs_diff_x = abs(sensor[0] - beacon[0])
        abs_diff_y = abs(sensor[1] - beacon[1])
        total_diff = abs_diff_x + abs_diff_y + 1
        for direction in [1,-1]:
            for i in range(-total_diff,1,1):
                p = (sensor[0] + i,sensor[1] + direction*(total_diff+i))
                if p[0] >= 0 and p[0] <= range_size and p[1] >= 0 and p[1] <= range_size:
                    poss = True
                    for sen,beac in sensor_beacons:
                        if sen == sensor:
                            continue
                        if in_range(p,sen,beac)==1 or p == beac or p == sen:
                            poss = False
                            break
                    if poss:
                        print(p[0]*4000000 + p[1])
                        exit()
        for direction in [1,-1]:
            for i in range(0,total_diff+1,1):
                p = (sensor[0] + i,sensor[1] + direction*(total_diff-i))
                if p[0] >= 0 and p[0] <= range_size and p[1] >= 0 and p[1] <= range_size:
                    poss = True
                    for sen,beac in sensor_beacons:
                        if sen == sensor:
                            continue
                        if in_range(p,sen,beac)==1 or p == beac or p == sen:
                            poss = False
                            break
                    if poss:
                        print(p[0]*4000000 + p[1])
                        exit()
