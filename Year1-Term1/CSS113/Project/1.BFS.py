'''
 สมาชิกกลุ่ม
 65090500435 ณัฐธนิสชา อัมพรชัยรัชต์
 65090500438 ธันยากร เจริญพร
 65090500440 นรุตม์ชัย หมื่นแสน
'''

graph = {
    'A' : ['B','C','F'],
    'B' : ['A','D','J'],
    'C' : ['A','F'],
    'D' : ['B','E','G','H'],
    'E' : ['D','G'],
    'F' : ['H','K'],
    'G' : ['D','E','I','J'],
    'H' : ['D','F','I'],
    'I' : ['G','H','J'],
    'J' : ['B','I','K'],
    'K' : ['F','J']
    }

visited = []  # List for visited nodes.
queue = []  # Initialize a queue


def bfs(visited, graph, node):  # function for BFS
    visited.append(node)
    queue.append(node)

    while queue:          # Creating loop to visit each node
        m = queue.pop(0)
        print(m, end=" ")

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


# Driver Code
# node = str(input("enter your node:"))
print("Following is the Breadth-First Search")
bfs(visited, graph, 'A')    # function calling


# https://favtutor.com/blogs/breadth-first-search-python
