#!/usr/bin/python3

# Implement Ford Fulkerson, where weighted graphs are represented by arrays.

# Import useful packages
import numpy as np
from copy import deepcopy

# Given a graph represented as a matrix ary, find a path between two nodes at indices i and j. subpath gives the part of the potential path found by previous calls. 
def GetPath(ary,i,j,subpath=[]):
	if len(subpath)==0:
		subpath = [i]
	if not ary[subpath[-1],j]==0:
		subpath.append(j)
		return subpath
	N = ary.shape[1]
	k = 0
	ret = -1
	while k < N and ret == -1:

		while k < N and (ary[subpath[-1],k] == 0 or k in subpath):
			k = k + 1
		if k >= N:
			return -1;

		subpath2 = deepcopy(subpath)
		subpath2.append(k)
		ret = GetPath(ary,i,j,subpath2)
	return ret

# Takes as input a symmetric N by N matrix Cap, such that the Cap[i,j] represents the total capacity between nodes i and j in a graph. We will assume that the source node is at the first index, and the sink node is at the last index. 
def FordFulkerson(Cap):
	
	# CapEff will store the unused capacity in the graph. 
	CapEff = np.array(deepcopy(Cap))
	# Number of vertices
	N = CapEff.shape[0]
	# Flow is an antisymmetric matrix
	Flow = np.zeros((N,N))
	path = GetPath(CapEff,0,N-1)

	while not path == -1:
		path_capacities = [0 for n in path[:-1]]
		for i in range(0,len(path_capacities)):
			path_capacities[i] = CapEff[path[i],path[i+1]]
		lowest_cap = min(path_capacities)
		for i in range(0,len(path)-1):
			Flow[path[i],path[i+1]] += lowest_cap
			Flow[path[i+1],path[i]] += -lowest_cap
		for i in range(0,N):
			for j in range(0,N):
				CapEff[i,j] = Cap[i,j] - abs(Flow[i,j])
		path = GetPath(CapEff,0,N-1)

	ret = 0
	for i in range(1,N):
		ret += Flow[0,i]
	return ret
	
def main():

	ary = np.zeros((25,25))
	for i in range(0,24):
		ary[i,i+1] = 1
		ary[i+1,i] = 1
	#print(ary)
	print()
	print(FordFulkerson(ary))

if __name__ == '__main__':
	main()
