# MarkovDecisionProcess-and-RL

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