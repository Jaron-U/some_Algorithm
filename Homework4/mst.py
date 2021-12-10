# cited from https://www.programiz.com/dsa/kruskal-algorithm
###############################
## FIle name: mst.py
## Name: Jianglong Yu
## Date: 7/29
## descripution: This code is read the file, and deal with these data. Use kruskal algorithm to find the minimum distance.
#################################
import math
# find parent node of a node
def findParent(parent, n):
    # if the value of the index number in parents list equal to the value index,
    # which mean we find the parent of n
    if parent[n] == n:
        return n
    #keep looking for the parent node
    return findParent(parent, parent[n])

# point the parent of one node to another
def union(parent, x, y):
    parent[findParent(parent,x)] = findParent(parent,y)

# Kruskal algorithm 
def kruskal_algo(g, n):
    # store the node has been selected
    result = 0
    # set a edge flag
    edge = 0
    # sort the tuple list according to the distance
    g.sort(key = lambda x : x[2])
    # set the parent list
    parent = []
    for node in range(n):
        # put the date into the parent list
        parent.append(node)
    # use for loop to connecent the node one by one
    for i in range(len(g)):
        # get the info of each edge
        u, v, w = g[i]
        # find the parent node of each side
        x = findParent(parent, u)
        y = findParent(parent, v)
        # if they have different parent node, mean is we can select this edge
        if (x != y):
            # add the distence
            result += w
            # edge flag increaing
            edge += 1
            # use the union function put them into one parent node
            union(parent, x, y)
        # the condition out of loop, if the number of edge we selected is equal to the vertex - 1
        if (edge == n-1):
            # just return the result
            return result

# function that deal with the infomation of point and add them into a graph
def creat_graph(all_points):
    x,y = 0, 0
    g = []
    # Make sure that there are edges at each of the two points
    for i in range(len(all_points)-1):
        y = x+1
        for _ in range(len(all_points)-1-i):
            # count the distance use formula
            distance = round(math.sqrt(pow((all_points[x][0] - all_points[y][0]), 2) + pow((all_points[x][1] - all_points[y][1]), 2)))
            # No directional graph, so they can have the opposite direction
            g.append((x, y, distance))
            g.append((y, x, distance))
            y += 1
        x += 1
    return g

def handlefile(filename):
    f = open(filename)
    # read each line in to a list
    lines = f.readlines()
    # get the number of test cases
    test_cases = int(lines[0])
    # set a line flag
    lines_idx = 1
    # use for loop to handle each graph
    for i in range(test_cases):
        # get the number of vertex
        n_vertex = int(lines[lines_idx])
        lines_idx += 1
        # set a all_point
        all_points = []
        for _ in range(n_vertex):
            # for loop get the 
            point = []
            # get these number in this line, put them into a list
            point.extend(lines[lines_idx].strip().split(' '))
            # convert the string list into int list
            point = list(map(int, point))
            # Put the point data into the list 
            all_points.append(point)
            lines_idx += 1
        # get the graph
        g = creat_graph(all_points)
        print("Test case {0}: MST weight {1}".format(i+1, kruskal_algo(g, n_vertex)))
        print("")

handlefile("graph.txt")