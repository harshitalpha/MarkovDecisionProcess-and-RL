from MDP import MarkovDecisonProcess
from Environment import GridWorld

grid = [[' ',' ',' ',' ',' '],
        ['S',' ',' ',' ',10],
        [-100,-100, -100, -100, -100]]

Grid = GridWorld(grid, 0.01, -1.0)
M = MarkovDecisonProcess(0.9, Grid, 100)
M.ValueIteration()
values = M.getValues()
actions = M.getActions()
qvalues = M.getQValues()
for i in values.keys():
    print(f"{i} : {values[i]}, {actions[i]}")

print('-'*100)

grid = [[' ',' ',' ',' ',' '],
        [8,'S',' ',' ',10],
        [-100,-100, -100, -100, -100]]
Grid = GridWorld(grid, 0.01, -1.0)
M = MarkovDecisonProcess(0.9, Grid, 100)
M.ValueIteration()
values = M.getValues()
actions = M.getActions()
qvalues = M.getQValues()
for i in values.keys():
    print(f"{i} : {values[i]}, {actions[i]}")

print('-'*100)
grid = [[' ',' ',' ',' ',' '],
        [' ','#',' ',' ',' '],
        [' ','#', 1,'#', 10],
        ['S',' ',' ',' ',' '],
        [-10,-10, -10, -10, -10]]
Grid = GridWorld(grid, 0.01, -1.0)
M = MarkovDecisonProcess(0.9, Grid, 100)
M.ValueIteration()
values = M.getValues()
actions = M.getActions()
qvalues = M.getQValues()
for i in values.keys():
    print(f"{i} : {values[i]}, {actions[i]}")

print('-'*100)
grid = [[' ',' ',' ',+1],
        ['#','#',' ','#'],
        [' ','#',' ',' '],
        [' ','#','#',' '],
        ['S',' ',' ',' ']]
Grid = GridWorld(grid, 0.00001, 1.0)
M = MarkovDecisonProcess(0.9, Grid, 100)
M.ValueIteration()
values = M.getValues()
actions = M.getActions()
qvalues = M.getQValues()
for i in values.keys():
    print(f"{i} : {values[i]}, {actions[i]}")

