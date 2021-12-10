# import sys

# # Providing the graph
# vertices = [[0, 0, 1, 0, 0, 1, 0, 0],
#             [0, 0, 0, 0, 1, 0, 0, 1],
#             [1, 0, 0, 1, 0, 1, 1, 0],
#             [0, 0, 1, 0, 1, 0, 1, 0],
#             [0, 1, 0, 1, 0, 0, 1, 1],
#             [1, 0, 1, 0, 0, 0, 1, 0],
#             [0, 0, 1, 1, 1, 1, 0, 1],
#             [0, 1, 0, 0, 1, 0, 1, 0]]

# edges = [[0, 0, 4, 0, 0, 7, 0, 0],
#          [0, 0, 0, 0, 9, 0, 0, 3],
#          [4, 0, 0, 3, 0, 2, 9, 0],
#          [0, 0, 3, 0, 3, 0, 7, 0],
#          [0, 9, 0, 3, 0, 0, 2, 7],
#          [7, 0, 2, 0, 0, 0, 8, 0],
#          [0, 0, 9, 7, 2, 8, 0, 3],
#          [0, 3, 0, 0, 7, 0, 3, 0]]

# # Find which vertex is to be visited next
# def to_be_visited():
#     global visited_and_distance
#     v = -10
#     for index in range(num_of_vertices):
#         if visited_and_distance[index][0] == 0 \
#             and (v < 0 or visited_and_distance[index][1] <=
#                  visited_and_distance[v][1]):
#             v = index
#     return v


# num_of_vertices = len(vertices[0])

# visited_and_distance = [[0, 0]]
# for i in range(num_of_vertices-1):
#     visited_and_distance.append([0, sys.MAXsize])

# for vertex in range(num_of_vertices):

#     # Find next vertex to be visited
#     to_visit = to_be_visited()
#     for neighbor_index in range(num_of_vertices):

#         # Updating new distances
#         if vertices[to_visit][neighbor_index] == 1 and \
#                 visited_and_distance[neighbor_index][0] == 0:
#             new_distance = visited_and_distance[to_visit][1] \
#                 + edges[to_visit][neighbor_index]
#             if visited_and_distance[neighbor_index][1] > new_distance:
#                 visited_and_distance[neighbor_index][1] = new_distance
        
#         visited_and_distance[to_visit][0] = 1

# i = 0
# sum = 0
# # Printing the distance
# for distance in visited_and_distance:
#     print("Distance of ", chr(ord('a') + i),
#           " from source vertex: ", distance[1])
#     i = i + 1
#     sum += distance[1]

# print("Sum: ", sum)



MAX= float('inf')
matrix = [[MAX, MAX, 4, MAX, MAX, 7, MAX, MAX],
         [MAX, MAX, MAX, MAX, 9, MAX, MAX, 3],
         [4, MAX, MAX, 3, MAX, 2, 9, MAX],
         [MAX, MAX, 3, MAX, 3, MAX, 7, MAX],
         [MAX, 9, MAX, 3, MAX, MAX, 2, 7],
         [7, MAX, 2, MAX, MAX, MAX, 8, MAX],
         [MAX, MAX, 9, 7, 2, 8, MAX, 3],
         [MAX, 3, MAX, MAX, 7, MAX, 3, MAX]]

def dijkstra(matrix, start_node):
    matrix_length = len(matrix)
    used_node = [False] * matrix_length
    distance = [MAX] * matrix_length
    distance[start_node] = 0
    while used_node.count(False):
        min_value = float('inf')
        min_value_index = 999
        for index in range(matrix_length):
            if not used_node[index] and distance[index] < min_value:
                min_value = distance[index]
                min_value_index = index

        used_node[min_value_index] = True
        for index in range(matrix_length):
            distance[index] = min(distance[index], distance[min_value_index] + matrix[min_value_index][index])

    return distance

list1 = []
for i in range(8):
    result = dijkstra(matrix,i)
    result.sort()
    list1.append((chr(65+i), result[7]))
    # print(result)

list1.sort(key = lambda x : x[1])
print(list1)
print(list1[0])




# start_node = int(input('please input start point:'))
# result = dijkstra(matrix,start_node)
# print('distance to other each point: %s' % result)