import sys
text = sys.stdin.read()
##text = '''4
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
##0'''
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
    
def dfs(adj_list):
    color = ["white"] * len(adj_list)
    seen = [None] * len(adj_list)
    done = [None] * len(adj_list)
    pred = [None] * len(adj_list)
    time = 0
    for s in range(len(adj_list)):
        if color[s] == "white":
            color[s] = "grey"
            seen[s] = time
            time += 1
            stack = [s]
            while stack != []:
                u = stack[-1]
                neighbours_color = [color[neighbour] for neighbour in adj_list[u]]
                if "white" in neighbours_color:
                    v = adj_list[u][neighbours_color.index("white")]
                    color[v] = "grey"
                    pred[v] = u
                    seen[v] = time
                    time += 1
                    stack.append(v)
                else:
                    stack.pop()
                    color[u] = "black"
                    done[u] = time
                    time += 1
    return seen, done, pred

for adj_list in adj:
    if adj_list[0] == 0:
        break
    seen, done, pred = dfs(adj_list[1:])
    tree_arc = len(pred) - pred.count(None)
    cross_arc = 0
    for neighbors in range(len(adj_list[1:])):
        for neighbor in adj_list[1 + neighbors]:
            if seen[neighbor] < done[neighbor] < seen[neighbors] < done[neighbors]:
                cross_arc += 1
    print(f"{tree_arc} {cross_arc}")
