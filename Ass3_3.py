import sys
text = sys.stdin.read()
##text = """4
##1 3
##2 3
##0
##
##3
##1 2
##
##1
##3
##
##
##
##0"""
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
    
def main(adj):
    for adj_list in adj:
        if adj_list[0] == 0:
            break
        girth = BFS(adj_list[1:])
        if girth != []:
            print(min(girth))
        else:
            print(0)
    
def BFS(adj):
    g = []
    for i in range(len(adj)):
        queue = [i]
        color = ['white'] * len(adj)
        d = [len(adj)] * len(adj)
        color[i] = 'grey'
        d[i] = 0
        while queue != []:
            node = queue.pop(0)
            neighbors = adj[node]
            for neighbor in neighbors:
                if color[neighbor] == 'white':
                    color[neighbor] = 'grey'
                    d[neighbor] = d[node] + 1
                    queue.append(neighbor)
                if neighbor == i:
                    g.append(d[node] + 1)
            color[node] = 'black'
    return g

main(adj)
