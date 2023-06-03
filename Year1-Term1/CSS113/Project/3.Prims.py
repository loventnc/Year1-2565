'''
 สมาชิกกลุ่ม
 65090500435 ณัฐธนิสชา อัมพรชัยรัชต์
 65090500438 ธันยากร เจริญพร
 65090500440 นรุตม์ชัย หมื่นแสน
'''

# Prim's Algorithm in Python

INF = 1e7
# number of vertices in graph
N = 11
# creating graph by adjacency matrix method
G = [[0, 1, 2, 3, 0, 0 ,0 ,0 ,0 ,0 ,0 ],
     [1, 0, 3, 0, 4, 5, 0, 0, 0, 0, 0 ],
     [2, 3, 0, 5, 2, 0, 0, 0, 0, 0, 0 ],
     [3, 0, 5, 0, 0, 4, 5, 0, 0, 0, 0 ],
     [0, 4, 0, 0, 0, 3, 0, 4, 0, 0, 0 ],
     [0, 5, 2, 4, 3, 0, 3, 2, 3, 2, 0 ],
     [0, 0, 0, 5, 0, 3, 0, 0, 0, 4, 0 ],
     [0, 0, 0, 0, 4, 2, 0, 0, 5, 0, 4 ],
     [0, 0, 0, 0, 0, 3, 0, 5, 0, 4, 3 ],
     [0, 0, 0, 0, 0, 2, 0, 0, 4, 0, 4 ],
     [0, 0, 0, 0, 0, 0, 0, 4, 3, 4, 0 ]
     ]

selected_node = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,]

no_edge = 0

selected_node[0] = True
# o = str(input("enter your node "))
# printing for edge and weight
print("Edge : Weight")
while (no_edge < N - 1):

    minimum = INF
    a = 0
    b = 0
    for m in range(N):
        if selected_node[m]:
            for n in range(N):
                if ((not selected_node[n]) and G[m][n]):
                    # not in selected and there is an edge
                    if minimum > G[m][n]:
                        minimum = G[m][n]
                        a = m
                        b = n
    print(str(a) + "-" + str(b) + ":" + str(G[a][b]))
    selected_node[b] = True
    no_edge += 1

# https://favtutor.com/blogs/prims-algorithm-python