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

def comparelist(tuple1, tuple2):
    resultlist = []
    for i in range(len(tuple1)):
        for j in range(len(tuple2)):
            if (tuple1[i][0] == tuple2[j][0]):
                if (tuple1[i][1] < tuple2[j][1]):
                    resultlist.append(tuple1[i])
                else:
                    resultlist.append(tuple2[j])
    return resultlist

def creatlist(n):
    list1 = []
    for i in range(n):
        list1.append(i)
    return list1

def findpoints(matrix):
    alldis_list = []
    x,y = 0, 0
    for i in range(len(matrix)-1):
        y = x+1
        for _ in range(len(matrix)-1-i):
            val_listx = creatlist(len(matrix))
            del val_listx[y]
            listx = dijkstra(matrix, x)
            del listx[y]
            tuplex = list(zip(val_listx,listx))


            val_listy = creatlist(len(matrix))
            del val_listy[x]
            listy = dijkstra(matrix, y)
            del listy[x]
            tupley = list(zip(val_listy,listy))


            finallist = comparelist(tuplex, tupley)
            finallist.sort(key = lambda x : x[1])
            maxd = finallist[5][1]
            alldis_list.append((chr(x+65), chr(y+65), maxd))
            y += 1
        x += 1
    alldis_list.sort(key= lambda x : x[2])
    return alldis_list

print(findpoints(matrix))



# # list1 = []
# for i in range(8):
#     result = dijkstra(matrix,i)
#     #   result.sort()
#     #   list1.append((chr(65+i), result[7]))
#     print(result)
