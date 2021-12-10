# cited CS325-Homework4 mst.py by Jianglong Yu
###############################
## FIle name: tsp.py
## Name: Jianglong Yu
## Date: 8/12
## descripution: This code is read the file, and deal with these data. Using nearest neighbor algorithm to solve TSP 
#################################
import math
import sys

maxnumber = 999999
# by using tuple list graph---time out
# def NearestNeighbor(g, n):
#     # get a copy of g
#     g_copy = g[:]
#     # start from 0
#     tourlist = [0]
#     # total distance
#     total_d = 0
#     # set currenty city numebr
#     current_city = 0
#     for _ in range(n-1):
#         # set a list find the nearest line
#         compare_list = []
#         # find all points connected the current city
#         for i in range(len(g)):
#             if g[i][0] == current_city:
#                 compare_list.append(g[i])
#         # sort the list by distance
#         compare_list.sort(key = lambda x : x[2])
#         # get the shortest distance to current city
#         u, v, d = compare_list[0]
#         tourlist.append(v)
#         total_d += d
#         # set the current point is v
#         current_city = v
#         # delete all path to the current city.
#         for j in range(len(compare_list)):
#             # get each element from this list
#             u1, v1, d1 = compare_list[j]
#             g.remove((u1, v1, d1))
#             g.remove((v1, u1, d1))
#     # get the last city in the tour
#     last_c = tourlist[-1]
#     # add the distance from the last city to the start city
#     for k in range(len(g_copy)):
#         if g_copy[k][0] == 0 and g_copy[k][1] == last_c:
#             total_d += g_copy[k][2]
#     # put the tour list and distance into a list
#     tourlist.append(total_d)
#     return tourlist

# # function that deal with the infomation of point and add them into a graph use tuple list
# def creat_graph(all_points):
#     x,y = 0, 0
#     g = []
#     # Make sure that there are edges at each of the two points
#     for i in range(len(all_points)-1):
#         y = x+1
#         for _ in range(len(all_points)-1-i):
#             # count the distance use formula
#             distance = round(math.sqrt(pow((all_points[x][1] - all_points[y][1]), 2) + pow((all_points[x][2] - all_points[y][2]), 2)))
#             # No directional graph, so they can have the opposite direction
#             g.append((x, y, distance))
#             g.append((y, x, distance))
#             y += 1
#         x += 1
#     return g

# function that deal with the infomation of point and add them into a graph using matrix 
def creat_graph(all_points):
    x,y = 0, 0
    # created a matrix
    g = []
    for i in range(len(all_points)):
        g.append([maxnumber]*len(all_points))
    # Make sure that there are edges at each of the two points
    for i in range(len(all_points)-1):
        y = x+1
        for _ in range(len(all_points)-1-i):
            # count the distance use formula
            distance = round(math.sqrt(pow((all_points[x][1] - all_points[y][1]), 2) + pow((all_points[x][2] - all_points[y][2]), 2)))
            # No directional graph, so they can have the opposite direction
            g[x][y] = distance
            g[y][x] = distance
            y += 1
        x += 1
    return g

# by using matrix graph
def NearestNeighbor(g, n):
    # get copy of the g
    g_copy = g[:]
    # the a list store the tour point. start from city 0
    tourlist = [0]
    # total distance
    total_d = 0
    # current city
    current_city = 0
    for _ in range(n-1):
        # get the distance of nearest city to the current city
        nearest_city_d = min(g[current_city])
        total_d += nearest_city_d
        # get th nearest city to the current city
        nearest_city = g[current_city].index(nearest_city_d)
        # add this city to the tour list
        tourlist.append(nearest_city)
        # set the distance of all other cities to current city is max. which mean delete the path of the all other cities to current city
        for i in range(n):
            g[i][current_city] = maxnumber
        # set the nearest_city to the current city
        current_city = nearest_city
    
    # get the last city
    last_city = tourlist[-1]
    # get the distance of last city to the start city and add them to the total distance
    total_d += g_copy[0][last_city]
    # put the total distance to the tour list
    tourlist.append(total_d)
    return tourlist

def handlefile(filename):
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

handlefile(sys.argv[1])

