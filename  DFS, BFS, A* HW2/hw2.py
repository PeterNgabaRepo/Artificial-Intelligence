import sys
import math
import heapq as hq

def readIn():
	maze = []
	filename = input("Enter filename: ")
	the_file = open(filename)
	for line in the_file:
		line2 = []
		for i in range(len(line)):
			if line[i] != "\n" and line[i] != " ":
				line2.append(line[i])
		maze.append(line2)

	return maze

def displayMaze(maze):
	for i in range(len(maze)):
		print()
		for j in range(len(maze[i])):
			print(maze[i][j], end=" ")

	print()
	print()

def buildVectorList(maze):
	vectList = []
	for i in range(len(maze)):
		for j in range(len(maze[i])):
			if (maze[i][j]) == '0':
				v1 = vertex(j, i)
				vectList.append(v1)
	return vectList

def buildEdgeList(maze):
	edgeList = []

	for i in range(len(maze)):
		for j in range(len(maze[i])):
			if (maze[i][j]) == '0':
				v1 = vertex(j, i)

				if i+1 < len(maze) and maze[i+1][j] == '0' :
					v2 = vertex(j, i+1)
					e1 = edge(v1, v2)
					edgeList.append(e1)

				if i-1 >= 0 and maze[i-1][j] == '0' :
					v2 = vertex(j, i-1)
					e1 = edge(v1, v2)
					edgeList.append(e1)

				if j+1 < len(maze[i]) and maze[i][j+1] == '0':
					v2 = vertex(j+1, i)
					e1 = edge(v1, v2)
					edgeList.append(e1)

				if j-1 >= 0 and maze[i][j-1] == '0':
					v2 = vertex(j-1, i)
					e1 = edge(v1, v2)
					edgeList.append(e1)

	return edgeList

def cost(v1, v2):
	y2 = v2.y
	y1 = v1.y

	x2 = v2.x
	x1 = v1.x

	delta_y = y2 - y1
	delta_x = x2 - x1

	if delta_y < 0:
		delta_y *= -1

	if delta_x < 0:
		delta_x *= -1

	cost = math.sqrt( (delta_y ** 2) + (delta_x ** 2) )
	return cost

class vertex:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.parent = -1
		self.key = sys.maxsize
		self.extracted = 0

class edge:
	def __init__(self, v1, v2):
		self.vert1 = v1
		self.vert2 = v2
		self.cost = cost(v1, v2)

class graph:
	def __init__(self, vertices, edges):
		self.adjList = []
		self.vertices = vertices
		self.edges = edges

		m = len(vertices)
		n = len(edges)


		for i in range(m):
			empty = []
			for j in range(n):
				if vertices[i].x == edges[j].vert1.x and vertices[i].y == edges[j].vert1.y:
					empty.append(edges[j])
			#	if vertices[i].x == edges[j].vert2.x and vertices[i].y == edges[j].vert2.y:
			#		empty.append(edges[j])
			self.adjList.append(empty)

	def getIndex(self, v):
		for i in range(len(self.vertices)):
			if v.x == self.vertices[i].x and v.y == self.vertices[i].y:
				return i

def DFS(graph, v):
	index = graph.getIndex(v)

	for j in range(len(graph.adjList[index])):
		index2 = graph.getIndex(graph.adjList[index][j].vert2)
		if graph.vertices[index2].parent == -1:
			graph.vertices[index2].parent = index
			graph.adjList[index][j].vert2.parent = index

			DFS(graph, graph.adjList[index][j].vert2)
def BFS(graph, s):
	queue = []
	queue.append(s)

	while len(queue) != 0:
		v = queue.pop(0)
		index = graph.getIndex(v)

		for j in range(len(graph.adjList[index])):
			index2 = graph.getIndex(graph.adjList[index][j].vert2)
			if graph.vertices[index2].parent == -1:
				graph.vertices[index2].parent = index
				graph.adjList[index][j].vert2.parent = index
				queue.append(graph.vertices[index2])

def A(graph, s, t):
	queue = []

	index = graph.getIndex(s)
	graph.vertices[index].key = cost(s, t)

	hq.heappush(queue, graph.vertices[index])

	while len(queue) != 0:
		v =  hq.heappop(queue)

		if v.x == t.x and v.y == t.y:
			return

		index = graph.getIndex(v)
		graph.vertices[index].extracted == 1

		for j in range(len(graph.adjList[index])):
			index2 = graph.getIndex(graph.adjList[index][j].vert2)
			if graph.vertices[index2].extracted == 0:
				if (graph.vertices[index].key + graph.adjList[index][j].cost
				+ cost(graph.vertices[index2], t) < graph.vertices[index2].key):

					graph.vertices[index2].key = (graph.vertices[index].key +
					graph.adjList[index][j].cost + cost(graph.vertices[index2], t))

					graph.vertices[index2].parent = index
					graph.adjList[index][j].vert2.parent = index
					hq.heappush(queue, graph.vertices[index2])
					hq.heapify(queue)


def findRoot(maze):
	for i in range(len(maze)):
		for j in range(len(maze[i])):
			if maze[i][j] == "0" and i == 0:
				print(0)
				root = vertex(j, i)
				return root

	root = vertex(j, i)
	return root

def findGoal(maze):
	for i in range(len(maze)):
		for j in range(len(maze[i])):
			if maze[i][j] == "0" and i == len(maze) - 1:
				print(1)
				goal = vertex(j, i)
				return goal
	goal = vertex(j, i)
	return goal

def updateMaze(graph, goal, root):
	if goal.x != root.x or goal.y != root.y:
		x = goal.x
		y = goal.y

		maze[y][x] = "5"
#		print(maze)
		parent = graph.vertices[goal.parent]

		updateMaze(graph, parent, root)
	maze[root.y][root.x] = "5"

if __name__ == '__main__':
	maze = readIn()
	displayMaze(maze)

	vectList = buildVectorList(maze)
	edgeList = buildEdgeList(maze)

	graph = graph(vectList, edgeList)

	print("1 - DFS")
	print("2 - BFS")
	print("3 - A*")

	algorithm = input("Enter the menu option for the algorithm you want to run: ")

	if algorithm == "1":
		DFS(graph,vectList[0])

	elif algorithm == "2":
		BFS(graph, vectList[0])

	elif algorithm == 3:
		goal = findGoal(maze)
		A(graph, vectList[0], goal)

	goal = findGoal(maze)
	root = findRoot(maze)

	goal = graph.vertices[graph.getIndex(goal)]
	root = graph.vertices[graph.getIndex(root)]

	updateMaze(graph, goal, root)

	displayMaze(maze)

#	n = len(graph.adjList)

#	for i in range(n):

#		for j in range(len(graph.adjList[i])):
#			print(graph.adjList[i][j].vert1.x, end = ",")
#			print(graph.adjList[i][j].vert1.y, end = " ")

#			print(graph.adjList[i][j].vert2.x, end = ",")
#			print(graph.adjList[i][j].vert2.y, end = " ")
#		print()


#def updateMaze(graph, goal, root):
#        if goal.x != root.x or goal.x != root.y:
#                x = goal.x
#                y = goal.y
#
#                maze[y][x] = "5"

#                updateMaze(graph, goal.parent, root)
