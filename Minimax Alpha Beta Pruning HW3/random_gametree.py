# Paul Burkhardt, Ph.D.
# November 08, 2021
#
# CMSC 471: Introduction to Artificial Intelligence
#
# Random two-player game tree generator.
#
# Nodes at each tree level represent a game state and each level is a ply,
# i.e. player turn.
#
# Each node in the tree has an ID from {0, 1} where 0 is for even levels
# starting with the zeroth level and 1 for odd levels. Thus all nodes in a level
# have the same node ID.
#
# Each leaf node is initialized by a random final game score:
#
#  1 : win
# -1 : lose
#  0 : draw
import random
from random import *
class node:
    def __init__(self, key):
        self.key = key
        self.neighbor = []
        self.id = None

    def insert(self, key):
        self.neighbor.append(node(key))

class gametree:
    def __init__(self, branching_factor, depth):
        self.bf = branching_factor
        self.depth = depth
        self.root = node(None)
        self.root.id = 0

    def _random_insert(self, node):
        for i in range(randint(0, self.bf)):
            node.insert(None)

    def _build(self, node, k):
        if (k == self.depth):
            node.key = randint(-1, 1)
            return
        self._random_insert(node)
        if (len(node.neighbor) == 0):
            node.key = randint(-1, 1)
        for u in node.neighbor:
            u.id = (k+1) % 2
            self._build(u, k+1)
            
    def get_root(self):
        return self.root

    def generate(self):
        while (len(self.root.neighbor) == 0):
            self._build(self.root, 0)

    def print(self, node):
        for u in node.neighbor:
            self.print(u)
        print(f"key = {node.key}, id = {node.id}")
