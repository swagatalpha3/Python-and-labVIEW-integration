import numpy as np
import csv
import pandas as pd
# grid = [[5, 3, 0, 0, 7, 0, 0, 0, 0, ],
#          [6, 0, 0, 1, 9, 5, 0, 0, 0, ],
#          [0, 9, 8, 0, 0, 0, 0, 6, 0, ],
#          [8, 0, 0, 0, 6, 0, 0, 0, 3, ],
#          [4, 0, 0, 8, 0, 3, 0, 0, 1, ],
#          [7, 0, 0, 0, 2, 0, 0, 0, 6, ],
#          [0, 6, 0, 0, 0, 0, 2, 8, 0, ],
#          [0, 0, 0, 4, 1, 9, 0, 0, 5, ],
#          [0, 0, 0, 0, 8, 0, 0, 7, 9, ]]

# def ret(arr):
#     return arr


# print(np.matrix(grid))
# with open('data.csv', newline='') as data_in:
#     grid = list(csv.reader(data_in))
def collect():   # take data from LABVIEW
    global grid
    df = pd.read_csv('data_in.csv', header=None, index_col=None)
    grid = (df.values.tolist())
    return


def clear():  # Put data to LABVIEW
    out = np.zeros((9, 9))
    df = pd.DataFrame(out.tolist())
    df.to_csv('data_out', index=False, header=None)


def possible(y, x, n):
    global grid
    for i in range(0, 9):
        if grid[y][i] == n:
            return False
    for i in range(0, 9):
        if grid[i][x] == n:
            return False
    x0 = (x // 3) * 3
    y0 = (y // 3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if grid[y0 + i][x0 + j] == n:
                return False
    return True


def solve():
    global grid
    global out
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1, 10):
                    if possible(y, x, n):
                        grid[y][x] = n
                        solve()
                        grid[y][x] = 0
                return
    # print(grid)
    out = np.array(grid)
    df = pd.DataFrame(out.tolist())
    df.to_csv('data_out', index=False, header=None)
    return 0


if __name__ == '__main__':
    # print(possible(4, 4, 3))
    # print(grid.tolist())
    # print(solve.out)
    collect()
    solve()
    print((out))
    # print(ret(grid1))
    # print(type(grid[0][3]))
    # print((df.values))
    # print(df)
