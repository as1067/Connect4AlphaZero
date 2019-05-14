import Arena
from MCTS import MCTS
from connect4_Hawk.Connect4Game import Connect4Game, display
from connect4_Hawk.Connect4Players import *
#from othello.pytorch.NNet import NNetWrapper as NNet
from connect4_Hawk.NNet import NNetWrapper as NNet

import numpy as np
from utils import *

"""
use this script to play any two agents against each other, or play manually with
any agent.
"""

g = Connect4Game(6,7)

# all players
# rp = RandomPlayer(g).play
# gp = GreedyOthelloPlayer(g).play
hp = HumanConnect4Player(g).play
hp2 = HumanConnect4Player(g).play

#nnet players
# n1 = NNet(g)
# n1.load_checkpoint('./temp','temp.pth.tar')
# args1 = dotdict({'numMCTSSims': 50, 'cpuct':1.0})
# mcts1 = MCTS(g, n1, args1)
# n1p = lambda x: np.argmax(mcts1.getActionProb(x, temp=0))


# n2 = NNet(g)
# n2.load_checkpoint('./tempOriginal','temp.pth.tar')
# args2 = dotdict({'numMCTSSims': 25, 'cpuct':1.0})
# mcts2 = MCTS(g, n2, args2)
# n2p = lambda x: np.argmax(mcts2.getActionProb(x, temp=0))

arena = Arena.Arena(hp, hp2, g, display=display)
print(arena.playGames(10, verbose=True))
