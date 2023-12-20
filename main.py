'''
Sudoku Problem Solver
Created by Nathan Sivalingam
13/12/2023

Inspired/Adapted from:
https://www.youtube.com/watch?v=PZJ5mjQyxR8
'''

import numpy as np

# example my_grid
my_grid = [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,0,0]]

def possible(row, col, num):
        global my_grid
        # given row
        for i in range(0,9):
            if my_grid[row][i] == num:
                return False
 
        # given column
        for i in range(0,9):
            if my_grid[i][col] == num:
                return False
        
        # given square
        x0 = (col // 3) * 3
        y0 = (row // 3) * 3

        for i in range(0,3):
            for j in range(0,3):
                if my_grid[y0+i][x0+j] == num:
                    return False

        return True

def main():
    global my_grid
    for row in range(0,9):
        for col in range(0,9):
            if my_grid[row][col] == 0:
                for num in range(1,10):
                    if possible(row, col, num):
                        my_grid[row][col] = num
                        main()
                        my_grid[row][col] = 0
                
                return
    
    print(np.matrix(my_grid))
    input("Another solution...")

main()
