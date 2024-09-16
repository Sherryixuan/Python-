##import sys
##data = sys.stdin.read().strip().split('\n')
data = '''4
1 3
2 3
0

3
1 2

1
0'''
data.strip().split('\n')
def directed_girth(adj):
    n = len(adj)
    min_girth = float('inf')

    for start_node in range(n):
        visited = [False] * n
        distance = [-1] * n
        queue = [(start_node, 0)]
        visited[start_node] = True

        while queue:
            node, dist = queue.pop(0)
            distance[node] = dist

            for neighbor in adj_list[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append((neighbor, dist + 1))
                elif neighbor == start_node:
                    min_girth = min(min_girth, dist + 1)

    return min_girth if min_girth != float('inf') else 0

index = 0
num_digraphs = len(data)
adj = []
d = 0

while index < num_digraphs:
    n = int(data[index])
    if n == 0:
        adj.append([n] + data[index + 1:])
        break
    index += 1
    adj.append([n])
    for i in range(n):
        line = data[index + i]
        neighbors = [int(j) for j in line.split()]
        adj[d].append(neighbors)
    d += 1
    index += n

for graph in graphs:
        print(directed_girth(graph))
