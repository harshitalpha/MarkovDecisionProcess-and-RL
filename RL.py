from Environment import GridWorld
from tqdm import tqdm
import collections
import random
import os

class QLearning:

    def __init__(self, grid: GridWorld, epochs, alpha, epsilon, discount):
        self.Grid = grid
        self.epochs = epochs
        self.alpha = alpha
        self.epsilon = epsilon
        self.discount = discount
        self.qValues = collections.defaultdict(lambda : 0.0)
        self.values = collections.defaultdict(lambda : 0.0)
        self.finalActions = collections.defaultdict(lambda : None)
        self.states = self.Grid.getStates()
        self.countExit = 0


    def train(self):
        state = self.Grid.getStartState()
        for _ in tqdm(range(self.epochs)):
            action = self.getNextAction(state)
            if action == None:
                state = self.Grid.getStartState()
                continue
            nextState, reward = self.Grid.doAction(state, action)
            if nextState == "TERMINAL_STATE":
                self.countExit += 1
            self.UpdateQValues(state, action, nextState, reward)
            state = nextState

    def UpdateQValues(self, state, action, nextstate, reward):
        sample = reward + self.discount * self.computeValuesFromQValues(nextstate)
        self.qValues[(state, action)] = (1-self.alpha) * self.qValues[(state, action)] + self.alpha * sample

    def computeActionsFromQValues(self, state):
        action = self.Grid.getPossibleActions(state)
        qmax = -float('inf')
        optAct = None
        for act in action:
            if self.qValues[(state, act)] > qmax:
                qmax = self.qValues[(state, act)]
                optAct = act
        return optAct

    def computeValuesFromQValues(self, state):
        qValues = []
        for action in self.Grid.getPossibleActions(state):
            qValues.append(self.qValues[(state, action)])
        if len(qValues) == 0:
            return 0.0
        else:
            return max(qValues)

    def getNextAction(self, state):
        nextPossibleAction = self.Grid.getPossibleActions(state)
        if nextPossibleAction == []:
            return None
        action = None
        if random.random() <= self.epsilon:
            action = random.choice(nextPossibleAction)
        else:
            action = self.computeActionsFromQValues(state)
        return action
    
    def getQValues(self):
        return self.qValues
    
    def getValues(self):
        states = self.Grid.getStates()
        for state in states:
            self.values[state] = self.computeValuesFromQValues(state)
        return self.values
    
    def getActions(self):
        states = self.Grid.getStates()
        for state in states:
            self.finalActions[state] = self.computeActionsFromQValues(state)
        return self.finalActions
    







