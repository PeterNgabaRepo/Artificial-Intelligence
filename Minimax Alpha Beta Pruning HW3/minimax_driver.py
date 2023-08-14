# Paul Burkhardt, Ph.D.
# November 20, 2021
#
# CMSC 471: Introduction to Artificial Intelligence
#
# Homework: Run minimax on the generated random game tree and return the final
# game score of the max player (root of the tree).
#
# Use the provided random two-player game tree generator.
#
# The max player starts the game.
#
# The max and min players alternate turns with the even levels being the max ply
# and odd levels the min ply.
from random_gametree import *
from minimax import *

def node_count(node):
    n = len(node.neighbor)
    for u in node.neighbor:
        n += node_count(u)
    return n

# Do not modify.
#
# Generate random game tree.
seed(5)
branching_factor = 10
depth = 6
tree = gametree(branching_factor, depth)
root = tree.get_root()
tree.generate()

# Compute minimax and return the max playe score.
size = node_count(root) + 1
n = minimax(root)
print(f"minimax alpha-beta processed {n} of {size} nodes: pruned {size-n}")

# Final game score for the max player.
print(f"The max player final score: {root.key}")
