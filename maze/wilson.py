# WILSON

import numpy as np
import random as rd
import matplotlib.pyplot as plt
import time
from numpy import random, array, transpose
import numpy as np


def wilson(grid: np.ndarray, size: int) -> np.ndarray:
    output_grid = np.empty([size * 3, size * 3], dtype=int)
    output_grid[:] = 0
    c = size * size  # number of cells to be visited

    # choose random cell
    y = rd.randrange(size)
    x = rd.randrange(size)
    grid[y, x] = 1

    visited = [[y, x]]
    visited_from = [0]

    while np.count_nonzero(grid) < c:

        if grid[y, x] == 1:
            print('closing loop...')
            print(visited)

            # already visited, close the loop (carve + empty visited)
            for i in range(len(visited)):
                ve = visited[i]
                vy = ve[0]
                vx = ve[1]
                print('actually visiting '+str(vy)+" "+str(vx))
                print('visited from: '+ str(visited_from[i]))
                grid[vy, vx] = 1
                w = vy * 3 + 1
                k = vx * 3 + 1
                output_grid[w, k] = 1

                vf = visited_from[i]

                if vf == 1:
                    output_grid[w - 1, k] = 1
                    output_grid[w - 2, k] = 1
                if vf == 2:
                    output_grid[w, k + 1] = 1
                    output_grid[w, k + 2] = 1
                if vf == 3:
                    output_grid[w + 1, k] = 1
                    output_grid[w + 2, k] = 1
                if vf == 4:
                    output_grid[w, k - 1] = 1
                    output_grid[w, k - 2] = 1
                p = plt.imshow(output_grid, interpolation='nearest', cmap='cubehelix')
                plt.pause(0.01)
                p.remove()

            visited.clear()
            visited_from.clear()
            y = rd.randrange(size)
            x = rd.randrange(size)
            print('randomly jumped '+str(y)+","+str(x))
            visited.append([y, x])
            visited_from.append(0)
            # we just random-jumped there

        else:
            if [y, x] in visited:
                # print(str(i)+","+str(j)+' - erasing loop...')
                # print(visited)
                # erase the loops
                visited.clear()
                visited_from.clear()

            # visit a random cell

            visited.append([y, x])

            print(grid)

            can_go = [1, 1, 1, 1]

            if y == 0:
                can_go[0] = 0
            if y == size - 1:
                can_go[2] = 0
            if x == 0:
                can_go[3] = 0
            if x == size - 1:
                can_go[1] = 0

            neighbour_idx = np.random.choice(np.nonzero(can_go)[0])  # n,e,s,w

            if neighbour_idx == 0:
                # going there from s
                visited_from.append(1)
                y -= 1

            if neighbour_idx == 1:
                visited_from.append(2)
                x += 1

            if neighbour_idx == 2:
                visited_from.append(3)
                y += 1

            if neighbour_idx == 3:
                visited_from.append(4)
                x -= 1

    return output_grid

def main ():
    size = 10

    # np.random.seed(42)
    grid = np.zeros(shape=(size, size))
    tic = time.time()
    console_grid = wilson(grid, size)
    tic2 = time.time()
    return (tic2-tic)


    time.sleep(100)