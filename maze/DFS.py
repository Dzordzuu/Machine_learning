from collections import defaultdict
import matplotlib.pyplot as plt
import time
from numpy import random, array, transpose


class Graph():
    def __init__(self):
        self.graph = defaultdict(list)
        self.vertex_list = []
        self.vertex_num = 0
        self.edge_num = 0

    def addEdge(self, f, t):
        self.graph[f].append(t)
        self.edge_num += 1
        if f not in self.vertex_list:
            self.vertex_list.append(f)
            self.vertex_num += 1
        if t not in self.vertex_list:
            self.vertex_list.append(t)
            self.vertex_num += 1


def printGraph(g):
    print('Graph vertex num: ' + str(g.vertex_num))
    print('Graph edge num: ' + str(g.edge_num))


def plotMaze(maze):
    plt.pcolormesh(maze)
    plt.axes().set_aspect('equal')
    plt.xticks([])
    plt.yticks([])
    plt.axes().invert_yaxis()
    plt.pause(0.01)


def shuffleMaze(mazeGraph):
    for node in mazeGraph.graph:
        random.shuffle(mazeGraph.graph[node])
    return mazeGraph


def checkCell(maze, x, y):
    flag = True
    v = [1] * 9
    v[4] = 0
    if x == 0:
        v[0], v[3], v[6] = 1, 1, 1
        v[5] = maze[x + 1, y]
    else:
        v[3] = maze[x - 1, y]
    if y == 0:
        v[0], v[1], v[2] = 1, 1, 1
        v[7] = maze[x, y + 1]
    else:
        v[1] = maze[x, y - 1]
    if x == len(maze) - 1:
        v[2], v[5], v[8] = 1, 1, 1
        v[3] = maze[x - 1, y]
    else:
        v[5] = maze[x + 1, y]
    if y == len(maze) - 1:
        v[6], v[7], v[8] = 1, 1, 1
        v[1] = maze[x, y - 1]
    else:
        v[7] = maze[x, y + 1]
    if x > 0 and y > 0:
        v[0] = maze[x - 1, y - 1]
    if x > 0 and y < len(maze) - 1:
        v[6] = maze[x - 1, y + 1]
    if x < len(maze) - 1 and y > 0:
        v[2] = maze[x + 1, y - 1]
    if x < len(maze) - 1 and y < len(maze) - 1:
        v[8] = maze[x + 1, y + 1]

    if v[1] == 1:
        if sum(v[3:9]) == 0:
            flag = True
        else:
            flag = False
    if v[3] == 1:
        if sum(v[1:3] + v[4:6] + v[7:9]) == 0:
            flag = True
        else:
            flag = False
    if v[5] == 1:
        if sum(v[0:2] + v[3:5] + v[6:8]) == 0:
            flag = True
        else:
            flag = False
    if v[7] == 1:
        if sum(v[0:6]) == 0:
            flag = True
        else:
            flag = False

    if x == len(maze) - 1 and y == len(maze) - 2:
        flag = True
    return flag


def makeMazeGraph(maze, shuffle=False):
    Size = len(maze)
    mazeGraph = Graph()
    for y in range(Size):
        for x in range(Size):
            coor = 100 * x + y
            if maze[x, y] != 0: continue
            if x + 1 < Size and maze[x + 1, y] == 0:
                mazeGraph.addEdge(coor, coor + 100)
            if x - 1 >= 0 and maze[x - 1, y] == 0:
                mazeGraph.addEdge(coor, coor - 100)
            if y + 1 < Size and maze[x, y + 1] == 0:
                mazeGraph.addEdge(coor, coor + 1)
            if y - 1 >= 0 and maze[x, y - 1] == 0:
                mazeGraph.addEdge(coor, coor - 1)
    if shuffle:
        mazeGraph = shuffleMaze(mazeGraph)
    printGraph(mazeGraph)
    return mazeGraph


def makeMaze(Size, animate=False, bfs_prob=0.3):
    maze = array([[0.0] * Size] * Size)
    mazeGraph = makeMazeGraph(maze, shuffle=True)

    x = 0
    y = 1
    coor = 100 * x + y
    stack = []
    stack.append(coor)
    # plt.axes().set_aspect('equal')
    # plt.xticks([])
    # plt.yticks([])
    # plt.imshow(maze,interpolation='nearest')

    while stack:
        if random.rand() < bfs_prob * random.rand():  # Set probability for BFS
            coor = stack.pop(0)  # BFS
        else:
            coor = stack.pop()  # DFS
        x = int(coor / 100)
        y = coor % 100
        if checkCell(maze, x, y):  # check if a cell can be filled
            maze[x, y] = 1
            if animate:
                print(len(stack))
                p = plt.imshow(maze, interpolation='nearest', cmap='cubehelix')
                plt.pause(0.000001)
                p.remove()
            for child in mazeGraph.graph[coor]:  # Append child to stack
                childx = int(child / 100)
                childy = child % 100
                if maze[childx, childy] == 0:
                    stack.append(child)

    maze[len(maze) - 2, len(maze) - 2] = 1
    maze[len(maze) - 1, len(maze) - 2] = 1
    # plt.imshow(maze,interpolation='nearest',cmap='cubehelix')
    # plt.show()
    return maze


def solveMaze(maze, animate=False):
    invertedMaze = 1 - maze
    footprint = invertedMaze
    mazeGraph = makeMazeGraph(invertedMaze, shuffle=True)
    Size = len(maze)

    x = 0
    y = 1
    coor = 100 * x + y
    stack = []
    step = 0
    stack.append(coor)
    # plt.axes().set_aspect('equal')
    # plt.xticks([])
    # plt.yticks([])
    plt.imshow(maze,interpolation='nearest')

    while stack:
        coor = stack.pop()
        x = int(coor / 100)
        y = coor % 100
        step += 1
        childNum = 0
        for child in mazeGraph.graph[coor]:
            childx = int(child / 100)
            childy = child % 100
            if invertedMaze[childx, childy] == 0:
                childNum += 1
                stack.append(child)
        if childNum == 0:
            invertedMaze[x, y] = 0.8
            for child in mazeGraph.graph[coor]:
                childx = int(child / 100)
                childy = child % 100
                if invertedMaze[childx, childy] <= 0.5:
                    childNum += 1
                    stack.append(child)
        else:
            invertedMaze[x, y] = 0.5
        if animate:
            print(len(stack))
            p = plt.imshow(1 - invertedMaze, interpolation='nearest', cmap='cubehelix')
            plt.pause(0.001)
            p.remove()
        if [x, y] == [Size - 1, Size - 2]:
            invertedMaze[x, y] = 0.5
            print("Found a path in {:d} steps.".format(step))
            break

    # plt.imshow(1-invertedMaze,interpolation='nearest',cmap='cubehelix')
    # plt.show()
    solvedMaze = 1 - invertedMaze
    return solvedMaze


def main():
    Size = 30
    print('\nMaze size: {:d}x{:d}'.format(Size, Size))
    print('\nCreating graph:')
    tic = time.time()
    maze = makeMaze(Size, animate=True, bfs_prob=0.3)
    # Switch animate to True to view animation
    toc1 = time.time()
    print("Created in: {:.3f} s.".format(toc1 - tic))
    print('\nSolving graph:')
    return toc1-tic

def main2():
    Size = 10
    print('\nMaze size: {:d}x{:d}'.format(Size, Size))
    print('\nCreating graph:')
    tic = time.time()
    maze = makeMaze(Size, animate=True, bfs_prob=0.3)
    toc1 = time.time()
    toc2=time.time()
    solveMaze(maze, animate=True)
    toc3 = time.time()
    print(toc3-toc2)
    return toc3 - toc2
if __name__ == '__main__':
    main()
