import collections
from Environment import GridWorld

class MarkovDecisonProcess:

    def __init__(self, discount, Grid: GridWorld, iteration):
        self.Grid = Grid
        self.discount = discount
        self.iteration = iteration
        self.values = collections.defaultdict(lambda : 0)
        self.QValues = collections.defaultdict(lambda : 0.0)
        self.finalActions = collections.defaultdict(lambda : None)
        self.states = self.Grid.getStates()

    
    def ValueIteration(self):
        k = 0
        while k < self.iteration:
            nextValues = self.values.copy()
            nextQValues = self.QValues.copy()
            for state in self.states:
                if self.Grid.isTerminal(state):
                    nextValues[state] = 0.0
                else:
                    qvalues = []
                    for action in self.Grid.getPossibleActions(state):
                        qvalue = self.computeQValues(state, action)
                        qvalues.append(qvalue)
                        nextQValues[(state, action)] = qvalue

                    nextValues[state] = max(qvalues)
            self.values = nextValues
            self.QValues = nextQValues
            for state in self.states:
                self.finalActions[state] = self.computeActionFromValues(state)
            
            k += 1

    def computeQValues(self, state, action):
        transactionProbs = self.Grid.getNextStateAndProbs(state, action)
        qvalue = 0.0
        for nextState, prob in transactionProbs:
            qvalue += prob * (self.Grid.getReward(state, action, nextState) + (self.discount * self.values[nextState]))
        return qvalue

    def computeActionFromValues(self, state):
        action = self.Grid.getPossibleActions(state)
        qmax = -float('inf')
        optAct = None
        for act in action:
            if self.QValues[(state, act)] > qmax:
                qmax = self.QValues[(state, act)]
                optAct = act
        return optAct
    
    def getValues(self):
        return self.values

    def getQValues(self):
        return self.QValues

    def getActions(self):
        return self.finalActions
    


