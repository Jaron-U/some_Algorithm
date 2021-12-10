graph = {'11': set(['12', '21']),
         '12': set(['11', '13', '22']),
         '13': set(['12', '14']),
         '14': set(['13', '15', '24']),
         '15': set(['14', '25']),
         '21': set(['11', '22', '31']),
         '22': set(['12', '21', '32']),
         '24': set(['14', '25', '34']),
         '25': set(['15', '24', '35']),
         '31': set(['21', '32']),
         '32': set(['22', '31', '33', '42']),
         '33': set(['32', '34']),
         '34': set(['33', '35', '24']),
         '35': set(['25', '34', '45']),
         '42': set(['32']),
         '45': set(['35', '55']),
         '51': set([]),
         '53': set(['54']),
         '54': set(['53', '55']),
         '55': set(['45', '54'])}

def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))


def shortest_path(graph, start, goal):
    try:
        return next(bfs_paths(graph, start, goal))
    except StopIteration:
        return None

result = shortest_path(graph, '11', '55')
for coord in result:
    l = list(coord)
    i =int(l[0])
    j = int(l[1])
    print("(",i,",",j,")", end="")

print("")
