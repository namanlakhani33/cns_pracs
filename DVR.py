n = int(input("Enter the number of nodes: "))
graph = [
    [0, 1, 9999, 9999, 9999],
    [1, 0, 6, 9999, 3],
    [9999, 6, 0, 2, 9999],
    [9999, 9999, 2, 0, 4],
    [9999, 3, 9999, 4, 0]
]

for intermediate in range(n):
    for source in range(n):
        for destination in range(n):
            if source != destination and source != intermediate and destination != intermediate:
                if graph[source][destination] > graph[source][intermediate] + graph[intermediate][destination]:
                    graph[source][destination] = graph[source][intermediate] + graph[intermediate][destination]

print("Graph after distance vector routing:")
for row in graph:
    print(row)