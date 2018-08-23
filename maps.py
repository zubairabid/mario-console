from random import random
from random import randrange

def genlevel(num):
    map = []



    map.append([32, 0, 4, 500, 6]) # a floor

    # Adding pipe
    for j in range(30, 400):
        if random() < 0.03:
            map.append([28, j-4, 4, 4, 6])

    # Adding staircase
    for j in range(30, 400):
        if random() < 0.001 or j == 380 or j == 40:
            map.append([31, j, 1, 16, 6])
            map.append([30, j+4, 1, 12, 6])
            map.append([29, j+8, 1, 8, 6])
            map.append([28, j+12, 1, 4, 6])

    # Adding gaps
    for j in range(20, 400):
        if random() < 0.01:
            map.append([24, j, 12, 5, 0])

            # Adding column before gap
            if random() < 0.4:
                map.append([28, j-4, 4, 4, 6])

            # Adding a staircase

    # Adding clouds
    for j in range(400):
        if random() < 0.08:
            map.append([2, j, 4, 4, 1])
            map.append([4, j-1, 2, 6, 1])

    # Adding platform 1
    for j in range(400):
        if random() < 0.02:
            map.append([23, j, 2, 4, 6])
            map.append([23, j+5, 2, 4, 6])
            map.append([23, j+10, 2, 4, 6])

            if random() < 0.2:
                map.append([23, j, 2, 4, 8])

            if random() < 0.7:
                map.append([17, j, 2, 2, 9])
                map.append([17, j+3, 2, 2, 9])
                map.append([17, j+6, 2, 2, 9])
                map.append([17, j+9, 2, 2, 9])

            # Adding platform 2:
            if random() < 0.5:
                map.append([12, j, 2, 4, 6])
                map.append([12, j+5, 2, 4, 6])
                map.append([12, j+10, 2, 4, 6])

                if random() < 0.2:
                    map.append([12, j+5, 2, 4, 8])


    map.append([0, 402, 35, 1, 6])

    return map
