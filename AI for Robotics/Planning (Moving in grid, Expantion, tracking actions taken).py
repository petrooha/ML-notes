# ----------
# User Instructions:
# 
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

import random
import numpy as np

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']



# SOLUTION:

def search(grid,init,goal,cost):
    # define the array of the same size as grid
    closed = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    # check off the init location
    closed[init[0]][init[1]] = 1

    # grid to memorize the order of expansions
    expand = [[-1 for row in range(len(grid[0]))] for col in range(len(grid))]

    # grid to memorize action to get there
    action = [[-1 for row in range(len(grid[0]))] for col in range(len(grid))]

    count = 0
    # create a list of particles
    x = init[0]
    y = init[1]
    g = 0
    open = [[x,y,g]]

    # Set the search flags
    found = False
    resign = False

    #print('initial open list:')
    #for i in range(len(open)):
        #print('   ', open[i])
    #print('---')

    while found is False and resign is False:

        # check if we still have elements in the open
        if len(open) ==0:
            resign = True
            print('fail')

        else:
            # remove node from list with smallest g value
            open.sort()
            open.reverse()
            next = open.pop()
            x = next[1]
            y = next[2]
            g = next[0]
            expand[x][y] = count
            count +=1
            #print(open)
            #print(next)
            #print('---')

            
            # check if we are done

            if x == goal[0] and y == goal[1]:
                found = True

            else:
                # expand winning element and add to new open list
                for i in range(len(delta)):
                    x2 = x + delta[i][0]
                    y2 = y + delta[i][1]
                    if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]):
                        if closed[x2][y2] == 0 and grid[x2][y2] ==0:
                            g2 = g + cost
                            open.append([g2, x2, y2])
                            closed[x2][y2] = 1
                            action[x2][y2] = i
                            
    X = x
    Y = y
    
    policy = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]
    x = goal[0]
    y = goal[1]
    policy[x][y] = '*'
    while x != init[0] and y != init[1]:
        x2 = x -delta[action[x][y]][0]
        y2 = y - delta[action[x][y]][1]
        policy[x2][y2] = delta_name[action[x][y]]
        x = x2
        y = y2
    x2 = x -delta[action[x][y]][0]
    y2 = y - delta[action[x][y]][1]
    policy[x2][y2] = delta_name[action[x][y]]
    x = x2
    y = y2
                                    
    return g, X, Y, np.array(expand), np.array(policy)
"""
def search(grid,init,goal,cost):
    # ----------------------------------------
    # insert code here
    # ----------------------------------------
    paths = []
    car = init
    moves = 0
    cell = grid[car[0]][car[1]]
    while car!=goal:
        move = 0
        attempt = 0
        while move==0 and attempt < 5:
            attempt +=1
            d = delta[random.randint(0,3)]
            card = car+d
            if grid[card[0]][card[1]]!=1 and card[0]>=0 and card[1]>=0 and grid[card[0]][card[1]] not in paths:
                car = card
                paths.append(card)
                move+=1
                moves+=1
                if car == goal:
                    return [moves, car[0], car[1]]
        if move == 0:
            paths = []
            moves = 0
            car = init
            print('Move failed', moves, car)
    
"""


