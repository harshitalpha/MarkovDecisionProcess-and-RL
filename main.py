from MDP import MarkovDecisonProcess
from RL import QLearning
from Environment import GridWorld

# grid = [[' ',' ',' ',' ',' '],
#         ['S',' ',' ',' ',10],
#         [-100,-100, -100, -100, -100]]

# grid = [[' ',' ',' ',' ',' '],
#         [8,'S',' ',' ',10],
#         [-100,-100, -100, -100, -100]]

# grid = [[' ',' ',' ',' ',' '],
#         [' ','#',' ',' ',' '],
#         [' ','#', 1,'#', 10],
#         ['S',' ',' ',' ',' '],
#         [-10,-10, -10, -10, -10]]

# grid = [[' ',' ',' ',+1],
#         ['#','#',' ','#'],
#         [' ','#',' ',' '],
#         [' ','#','#',' '],
#         ['S',' ',' ',' ']]

# grid = [    [  -10,-100 ' ', ' ', ' ', -10, ' ',-10, ' ', ' '],
#             [ ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', -10],
#             [ ' ', ' ', ' ', ' ', ' ', '#', 100 ' ', ' ', ' '],
#             [ -10, ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', -10],
#             [ ' ', ' ', '#', '#', ' ', ' ', ' ', ' ', ' ', ' '],
#             [ ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', '10'],
#             [ -10, ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', -100],
#             [ ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' '],
#             [ ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
#             [ 'S', ' ', ' ', -100, ' ', -10, ' ', -100, ' ', -10]  ]

grid = [[ '#',-100, -100, -100, -100, -100, '#'],
            [   1, 'S',  ' ',  ' ',  ' ',  ' ',  10],
            [ '#',-100, -100, -100, -100, -100, '#']]

Grid = GridWorld(grid, 0.01, -1.0)
M = MarkovDecisonProcess(0.4, Grid, 100)
M.ValueIteration()
values = M.getValues()
actions = M.getActions()
qvalues = M.getQValues()
for i in values.keys():
    print(f"{i} : {values[i]}, {actions[i]}")

RL = QLearning(Grid, 50000, alpha = 0.6, epsilon = 0.2, discount = 0.4)
RL.train()
values = RL.getValues()
actions = RL.getActions()
qvalues = RL.getQValues()
for i in values.keys():
    print(f"{i} : {values[i]}, {actions[i]}")
