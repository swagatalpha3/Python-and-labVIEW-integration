# Author : Swagat panda (Hochschule Darmstadt)

from argparse import ArgumentParser
import numpy as np
from sudoku_solver import collect
from sudoku_solver import solve
from sudoku_solver import clear
import pandas as pd


def parser():
    parser = ArgumentParser()
    parser.add_argument('--input', help='optional input from cmd')
    return parser


def end_session():
    exit()


parser = parser()
options = parser.parse_args()


def main():
    # my_arr = np.array([1, 2, 3, 4])
    Name = options.input
    # Name1 = float(Name) + 10
    # print(Name)
    if Name == 'solve':    # Solve sudoku
        # print(f'{Name1}')
        print("Solving......\n")
        collect()
        solve()
        print("Solved....")
        return
    elif Name == 'clear':    # clear the output array
        clear()
        return
    elif Name == 'exit':
        print('session stopped')
        end_session()
    else:                    # Do nothing
        print("Not a valid input\n")
        print("solve = solve the puzze")
        print("clear = clear teh output array")
        return
    # print(my_arr * 2)


if __name__ == '__main__':
    main()
    # out = np.zeros((9, 9))

    # print(type(out.tolist()))
    # df = pd.DataFrame(out.tolist())
    # print(df.values)
