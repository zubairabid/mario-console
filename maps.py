from random import random
from random import randrange

maps = [
[
[32, 0, 4, 500, 6],
[4, 80, 2, 4, 6],
[4, 40, 4, 8, 1],
[32, 20, 4, 5, 0],
[23, 40, 2, 4, 6],
[23, 45, 2, 4, 6],
[23, 50, 2, 4, 6],
[23, 55, 2, 4, 6],
[23, 60, 2, 4, 6],
[23, 65, 2, 4, 6],
[23, 80, 2, 4, 6],
[23, 10, 2, 4, 8],
# [(4, j, 4, 8, 1) for j in range(10,1000,10)]
],

[

[32, 0, 4, 30, 6],
[32, 35, 4, 20, 6],
[29, 38, 4, 5, 6]

],

]

def genlevel(num):
    map = []

    map.append([32, 0, 4, 500, 6]) # a floor

    # Adding pipe
    for j in range(30, 490):
        if random() < 0.03:
            map.append([28, j-4, 4, 4, 6])

    # Adding staircase
    for j in range(30, 420):
        if random() < 0.001 or j == 419 or j == 40:
            map.append([31, j, 1, 16, 6])
            map.append([30, j+4, 1, 12, 6])
            map.append([29, j+8, 1, 8, 6])
            map.append([28, j+12, 1, 4, 6])

    # Adding gaps
    for j in range(20, 490):
        if random() < 0.01:
            map.append([24, j, 12, 5, 0])

            # Adding column before gap
            if random() < 0.4:
                map.append([28, j-4, 4, 4, 6])

            # Adding a staircase

    # Adding clouds
    for j in range(490):
        if random() < 0.08:
            map.append([2, j, 4, 4, 1])
            map.append([4, j-1, 2, 6, 1])

    # Adding platform 1
    for j in range(490):
        if random() < 0.02:
            map.append([23, j, 2, 4, 6])
            map.append([23, j+5, 2, 4, 6])
            map.append([23, j+10, 2, 4, 6])

            if random() < 0.2:
                map.append([23, j, 2, 4, 8])

            # Adding platform 2:
            if random() < 0.5:
                map.append([12, j, 2, 4, 6])
                map.append([12, j+5, 2, 4, 6])
                map.append([12, j+10, 2, 4, 6])

                if random() < 0.2:
                    map.append([12, j+5, 2, 4, 8])


    return map
