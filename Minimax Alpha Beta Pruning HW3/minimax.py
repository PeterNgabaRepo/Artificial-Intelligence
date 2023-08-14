import sys
from random_gametree import *

def minimax(v): #max player starts
	global count
	count = 0
	alpha = -1 * sys.maxsize
	beta = sys.maxsize
	v.key = maxi(v, alpha, beta)
	return count

def maxi(v, alpha, beta):
	global count
	count += 1
	if (len(v.neighbor) == 0):
		return v.key

	v.key = -1 * sys.maxsize

	for u in v.neighbor:
		x = mini(u, alpha, beta)
		alpha = max(alpha, x)
		if(beta <= alpha):
#			print(1)
			return alpha

	return alpha

def mini(v, alpha, beta):
	global count
	count +=1
	if (len(v.neighbor) == 0):
		return v.key

	v.key = sys.maxsize

	for u in v.neighbor:
#		print(1);
		x = maxi(u, alpha, beta)
		beta = min(beta, x)
		if(beta <= alpha):
			return beta

	return beta

