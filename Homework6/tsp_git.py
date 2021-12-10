import math
import sys
import time

# Using the nearest neighbor algorithm to solve the TSP
def nn(graph, n, original):
  # graph is an adjacency table
  
  visited = [0]
  node = 0
  total = 0
  
  # Setting all distances from the starting point to the max int value
  for x in range(n):
    graph[x][0] = sys.maxsize
  
  # Going through every edge
  for x in range(n - 1):
    # Finding the node with the minimum distance
    minNode = min(graph[node])
    total += minNode
    deleteNode = graph[node].index(minNode)
    visited.append(deleteNode)
    
    # "Deleteing" instances of that node from the adjacency table
    graph[deleteNode][node] = sys.maxsize
    node = deleteNode

    for i in range(n):
      graph[i][node] = sys.maxsize
  
  # Finding the distance from the last node to the starting node
  total += original[visited[n - 1]]
  visited.append(total)
  
  return visited

fileText = open(sys.argv[1]) # Opening the example file
cities = int(fileText.readline()) # Getting the number of cities
graph = []
points = []
original = []

# Collecting each point
for x in range(cities):
  points.append([])
  temp = fileText.readline().split(" ")
  temp = list(filter(None, temp))
  points[x].append(int(temp[1]))
  points[x].append(int(temp[2]))
  
  # Creating an empty graph
  graph.append([])
  
  for i in range(cities):
    graph[x].append(sys.maxsize)

# Adding values to the adjacency table
for x in range(cities):
  for i in range(x + 1, cities):
    # Calculating the distance between two points
    distance = int(round(math.sqrt(math.pow((points[x][0] - points[i][0]), 2) + math.pow((points[x][1] - points[i][1]), 2))))
    graph[x][i] = distance
    graph[i][x] = distance

# Getting the distances from the starting point
for x in range(cities):
  original.append(graph[x][0])

ans = nn(graph, cities, original) # Getting the solution too the TSP using the nearest neighbor algorithm

# Writing to the file
newFile = sys.argv[1] + ".tour"
tour = open(newFile, 'w')
tour.write(str(ans[cities]) + '\n')

for x in range(cities):
  tour.write(str(ans[x]) + '\n')
  