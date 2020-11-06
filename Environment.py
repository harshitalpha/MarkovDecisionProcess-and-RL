'''
Our Project: Given a network with vertices and edges. Design the MDP to nevigate through the network. 
                Solve this through Reinforcement learning

Team:
Harshit Singhal- 18UCC159
Arpit Dangi- 18UCC003
Prerak Mathur- 18UCC149

Explanation:
    First of all we need to design an Stocastic Graph network. 
    
    Next we need to run Markov Decision Process Algorithms like Value Iteration and Policy Iteration. 
    To run MDP our algorithm know the probabilities of transition and reward it get for every tansition.

    Next we need to use Basic Reinforcement Learning algorithms like Q-Learning
    For Reinforcement learning, our algorithm dont know where to get the reward, and neither transition probabilities.
    Main task is to get the Q values for each state-transition pair.

Graph Network we should use:
    We should use a graph network that is neither so complicated nor so easy.
    I think we should use the version of Grid World (discussed in the Lectures), since it is prrtty easy to design and nevigate

    # # # & # # *
    # # # & # # @'
    # # # # # # @'
    # # @ @ @ # *

    Here # are the normal state from which we can move to North, South, East, West
    & are the walls our agent can not step on them 
    * are good exit with reward of +50
    @ are bad exit with reward of -50
    @' are very bad exit with reward of -100
    each transition has reward of -2 
    Start state can be Bottom Left #

    Our Agent need to find the best policy to nevigate through the network
'''
import collections
import random

class GridWorld:
    def __init__(self, grid, noise, livingReward):
        self.grid = grid
        self.width = len(grid)
        self.height = len(grid[0])
        self.noise = noise
        self.livingReward = livingReward
        self.terminalState = "TERMINAL_STATE"
        self.state = self.getStartState()
        
    
    def printGrid(self):
        print(self.grid)

    def getPossibleActions(self, state):
        if state == self.terminalState:
            return []
        x,y = state
        if type(self.grid[x][y]) == int:
            return ('exit',)
        return ('north','west','south','east')
    
    def getStartState(self):
        for x in range(self.width):
            for y in range(self.height):
                if self.grid[x][y] == 'S':
                    return (x, y)
        raise 'Grid has no start state'

    def getCurrentState(self):
        return self.state
    
    def getStates(self):
        # The true terminal state.
        states = [self.terminalState]
        for x in range(self.width):
            for y in range(self.height):
                if self.grid[x][y] != '#':
                    state = (x,y)
                    states.append(state)
        return states
    
    def isTerminal(self, state):
        if state == self.terminalState:
            return True
        return False

    def getReward(self, state, action, nextState):
        if state == self.terminalState:
            return 0.0
        x, y = state
        cell = self.grid[x][y]
        if type(cell) == int or type(cell) == float:
            return cell
        return self.livingReward

    def getNextStateAndProbs(self, state, action):
        if action not in self.getPossibleActions(state):
            return "Illegal Action"
        
        if state == self.terminalState:
            return []
        
        x, y = state

        if type(self.grid[x][y]) == int or type(self.grid[x][y]) == float:
            return [("TERMINAL_STATE", 1.0)]
        
        nextStates = []
        northState = (self.__isAllowed(y,x-1) and (x-1,y)) or state
        westState = (self.__isAllowed(y-1,x) and (x,y-1)) or state
        southState = (self.__isAllowed(y,x+1) and (x+1,y)) or state
        eastState = (self.__isAllowed(y+1,x) and (x,y+1)) or state

        if action == 'north' or action == 'south':
            if action == 'north':
                nextStates.append([northState, 1 - self.noise])
            if action == 'south':
                nextStates.append([southState, 1 - self.noise])
            
            nextStates.append([eastState, self.noise/2])
            nextStates.append([westState, self.noise/2])
        
        if action == 'east' or action == 'west':
            if action == 'east':
                nextStates.append([eastState, 1 - self.noise])
            if action == 'west':
                nextStates.append([westState, 1 - self.noise])
            
            nextStates.append([northState, self.noise/2])
            nextStates.append([southState, self.noise/2])
        
        return self.__aggregate(nextStates)
    
    def __aggregate(self, statesAndProbs):
        counter = collections.defaultdict(lambda : 0.0)
        for state, prob in statesAndProbs:
            counter[state] += prob
        newStatesAndProbs = []
        for state, prob in counter.items():
            newStatesAndProbs.append((state, prob))
        return newStatesAndProbs

    def __isAllowed(self, y, x):
        if y < 0 or y >= self.height: return False
        if x < 0 or x >= self.width: return False
        return self.grid[x][y] != '#'
    

    def getRandomState(self, state, action):
        nextStates = self.getNextStateAndProbs(state, action)
        if nextStates != 'Illegal Action':
            possibleState = [row[0] for row in nextStates]
            stateProbs = [row[1] for row in nextStates]
            nextState = random.choices(possibleState, weights=stateProbs, k = 1)[0]
            reward = self.getReward(state, action, nextState)
            return (nextState, reward) 
        else:
            return "Illegal Action"
    
    def doAction(self, state, action):
        nextStateAction = self.getRandomState(state, action)
        if nextStateAction != "Illegal Action":
            nextState, reward = nextStateAction[0], nextStateAction[1]
            self.state = nextState
            return (nextState, reward)
        else:
            return "Illegal Action"


# if __name__ == '__main__':
#     grid = [[' ',' ',' ',' ',' '],
#             ['S',' ',' ',' ',10],
#             [-100,-100, -100, -100, -100]]
    
#     G = GridWorld(grid, 0.2, -1.0)
#     state = (1,4)
#     print(state)
#     print(G.getPossibleActions(state))
#     print(G.getRandomState(state, 'east'))
#     print(G.getNextStateAndProbs(state, 'east'))
#     print(G.getReward(state, 'east', 'TERMINAL_STATE'))
#     print(G.doAction('east'))

    
    


