import sys
import math

def read_input():
    return sys.stdin.read().strip().split('\n')

def build_graph(v1):
    n = len(v1) // 2
    graph = [[] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if i != j:
                distance = math.sqrt((v1[2 * j] - v1[2 * i]) ** 2 + (v1[2 * j + 1] - v1[2 * i + 1]) ** 2)
                if distance <= 100:
                    graph[i].append((j, distance))
    return graph, n

def dijkstra(graph, n):
    distances = [float('inf')] * n
    distances[0] = 0
    unvisited = set(range(n))
    
    while unvisited:
        current_node = min(unvisited, key=lambda node: distances[node])
        if distances[current_node] == float('inf'):
            break
        unvisited.remove(current_node)
        
        for neighbor, weight in graph[current_node]:
            if neighbor in unvisited and distances[current_node] + weight < distances[neighbor]:
                distances[neighbor] = distances[current_node] + weight
    
    return distances[-1]

def main():
    data = read_input()
    
    for line in data:
        if line:
            values = [float(x) for x in line.split(',')[1:]]
            graph, n = build_graph(values)
            shortest_path = dijkstra(graph, n)
            
            if shortest_path != float('inf'):
                print(f'{shortest_path:.2f}')
            else:
                print(-1)

if __name__ == "__main__":
    main()
