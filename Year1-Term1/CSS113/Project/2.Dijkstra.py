'''
 สมาชิกกลุ่ม
 65090500435 ณัฐธนิสชา อัมพรชัยรัชต์
 65090500438 ธันยากร เจริญพร
 65090500440 นรุตม์ชัย หมื่นแสน
'''

class Graph:
    def __init__(self, verticies_num):
        self.v = verticies_num
        self.edges = [[0 for i in range(verticies_num)] for j in range(verticies_num)]
        self.visited = []
        
    def add_edge(self, u, v, weight):
        self.edges[u][v] = weight

def get_lowest_dist(list):
    lowest = (float('inf'), )
    for i in list:
        temp_dist = i[0]
        if temp_dist < lowest[0]:
            lowest = i
    return lowest

def dijkstra(graph, start_v, dest_v):
    data = {v:(float('inf'),) for v in range(graph.v)}
    data[start_v] = (0, 0)

    queue = []
    queue.append((0, start_v))

    while len(queue) > 0:
        (dist, current_v) = get_lowest_dist(queue)
        queue.remove((dist, current_v))
        graph.visited.append(current_v)

        for neighbor in range(graph.v):
            cost = graph.edges[current_v][neighbor]
            if cost == 0:
                continue
            if neighbor in graph.visited:
                continue

            old_cost = data[neighbor][0]
            new_cost = data[current_v][0] + cost
            if new_cost < old_cost:
                queue.append((new_cost, neighbor))
                data[neighbor] = (new_cost, current_v)
                        
    return data


g = Graph(8)
g.add_edge(0, 1, 2)
g.add_edge(0, 2, 5)
g.add_edge(0, 3, 3)
g.add_edge(1, 2, 2)
g.add_edge(1, 4, 6)
g.add_edge(2, 4, 3)
g.add_edge(2, 6, 6)
g.add_edge(3, 2, 2)
g.add_edge(3, 6, 7)
g.add_edge(4, 5, 3)
g.add_edge(4, 7, 6)
g.add_edge(5, 7, 2)
g.add_edge(6, 5, 3)
g.add_edge(6, 7, 4)


def answer(data, start_v, end_v):
    result = []
    distance = data[end_v][0]
    while start_v != end_v:
        result.append(end_v)
        end_v = data[end_v][1]
    result.append(start_v)
    return data, result[::-1], distance

print(*answer(dijkstra(g, 0, 7), 0, 7), sep="\n")