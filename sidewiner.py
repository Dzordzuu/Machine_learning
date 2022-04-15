# SIDE WINDER

import numpy as np
import random as rd
import matplotlib.pyplot as plt
import time
from numpy import random, array, transpose
import numpy as np


def carve_maze(grid: np.ndarray, size: int) -> np.ndarray:
    output_grid = np.empty([size * 3, size * 3], dtype=int)
    output_grid[:] = 0

    i = 0
    j = 0

    while i < size:
        w = i * 3 + 1
        previous_l = []
        while j < size:
            k = j * 3 + 1
            toss = grid[i, j]
            output_grid[w, k] = 1
            if toss == 0 and k + 2 < size * 3:
                output_grid[w, k + 1] = 1
                output_grid[w, k + 2] = 1
                previous_l.append(j)
            if toss == 1:
                # look back, choose a random cell
                if grid[i, j - 1] == 0:
                    # reaching from 0

                    r = rd.choice(previous_l)
                    k = r * 3 + 1

                # this just carve north if this is the first element of the row (1 element loop)
                output_grid[w - 1, k] = 1
                output_grid[w - 2, k] = 1
                previous_l = []

            j += 1

        i += 1
        j = 0
        p = plt.imshow(output_grid, interpolation='nearest', cmap='cubehelix')
        plt.pause(0.01)
        p.remove()

    return output_grid


def preprocess_grid(grid: np.ndarray, size: int) -> np.ndarray:
    # fix first row and last column to avoid digging outside the maze external borders
    first_row = grid[0]
    first_row[first_row == 1] = 0
    grid[0] = first_row
    for i in range(1, size):
        grid[i, size - 1] = 1
    return grid


def maze_to_string(output_grid: np.ndarray) -> str:
    s = ""

    return s


def main():
    n = 5
    p = 0.5
    size = 10

    # 1 (head) N, 0 (tail) E
    # np.random.seed(42)
    grid = np.random.binomial(n, p, size=(size, size))
    processed_grid = preprocess_grid(grid, size)
    output = carve_maze(processed_grid, size)
    output_string = maze_to_string(output)
    print(output_string)

    time.sleep(100)
if __name__ == '__main__':
    main()