import sys
text = sys.stdin.read()
data = text.split('\n')    
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
    
for i in range(len(adj)):
    arcs_added = 0
    if adj[i][0] == 0:
        break
    for j in range(1, len(adj[i])):
        if 0 in adj[i][j]:
            adj[i][j].append(adj[i][0])
            arcs_added += 1
    adj[i].append(adj[i][1])
    arcs_added += len(adj[i][1])
    adj[i].append(arcs_added)
    adj[i][0] += 1
  
for adj_list in adj:
    print(adj_list[0])
    if adj_list[0] == 0:
        for i in adj_list[1:]:
            print(i)
        break
    for i in adj_list[1:-1]:
        print(' '.join([str(neighbors) for neighbors in i]))
    print(adj_list[-1])
