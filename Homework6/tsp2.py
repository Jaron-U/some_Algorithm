# cited CS325-Homework4 mst.py by Jianglong Yu
###############################
## FIle name: tsp.py
## Name: Jianglong Yu
## Date: 7/29
## descripution: This code is read the file, and deal with these data. Using nearest neighbor algorithm to solve TSP 
#################################
import math
import sys
import time
def NearestNeighbor(g, n):
    # get a copy of g
    g_copy = g[:]
    # start from 0
    tourlist = [0]
    # total distance
    total_d = 0
    # set currenty city numebr
    current_city = 0
    for _ in range(n-1):
        # set a list find the nearest line
        compare_list = []
        # find all points connected the current city
        for i in range(len(g)):
            if g[i][0] == current_city:
                compare_list.append(g[i])
        # sort the list by distance
        compare_list.sort(key = lambda x : x[2])
        # get the shortest distance to current city
        u, v, d = compare_list[0]
        tourlist.append(v)
        total_d += d
        # set the current point is v
        current_city = v
        # delete all path to the current city.
        for j in range(len(compare_list)):
            # get each element from this list
            u1, v1, d1 = compare_list[j]
            g.remove((u1, v1, d1))
            g.remove((v1,u1,d1) )
    # get the last city in the tour
    last_c = tourlist[-1]
    # add the distance from the last city to the start city
    for k in range(len(g_copy)):
        if g_copy[k][0] == 0 and g_copy[k][1] == last_c:
            total_d += g_copy[k][2]
    # put the tour list and distance into a list
    tourlist.append(total_d)
    return tourlist

# function that deal with the infomation of point and add them into a graph
def creat_graph(all_points):
    x,y = 0, 0
    g = []
    # Make sure that there are edges at each of the two points
    for i in range(len(all_points)-1):
        y = x+1
        for _ in range(len(all_points)-1-i):
            # count the distance use formula
            distance = round(math.sqrt(pow((all_points[x][1] - all_points[y][1]), 2) + pow((all_points[x][2] - all_points[y][2]), 2)))
            # No directional graph, so they can have the opposite direction
            g.append((x, y, distance))
            g.append((y, x, distance))
            y += 1
        x += 1
    return g

def handlefile(filename):
    # f = open(sys.argv[1], 'r')
    f = open(filename)
    # read each line in to a list
    lines = f.readlines()
    lines_idx = 0
    # get the number of test cases
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
        point = list(filter(None, point))
        point = list(map(int, point))
        # Put the point data into the list 
        all_points.append(point)
        lines_idx += 1
    # get the graph
    
    g = creat_graph(all_points)
    final_tour = NearestNeighbor(g, n_vertex)
    distance = final_tour.pop()
    # Writing to the file
    tsp_example_tour = filename+'.tour'
    ft = open(tsp_example_tour, 'w')
    ft.write(str(distance)+'\n')
    for i in range(len(final_tour)):
        ft.write(str(final_tour[i])+'\n')

handlefile("tsp_example_5.txt")

