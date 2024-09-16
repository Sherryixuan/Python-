from collections import defaultdict, deque
import sys
#v = sys.stdin.read().split('\n')
v = """3
7 6
Easy Easy Medium Medium Hard Hard
Graphs Brute AdHoc Brute Geometry Math
SexyLife Brute Medium
BottomFeeder Graphs Hard
BadCase AdHoc Easy
Dominos Graphs Medium
Elephant Brute Hard
Flash Geometry Medium
Geography Math Easy
2 2
Easy Medium
Graph AdHoc
Funny AdHoc Medium
NotSoFun Graph Hard
3 2
E H
A B G
a B E
b B E
c G E""".split("\n")


    
def bfs(source, sink, parent, graph, capacity):
    visited = set()
    queue = deque([source])
    visited.add(source)
        
    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if v not in visited and capacity[(u, v)] > 0:
                parent[v] = u
                if v == sink:
                    return True
                queue.append(v)
                visited.add(v)
    return False
    
def edmonds_karp(source, sink, graph, capacity):
    parent = {}
    max_flow = 0
        
    while bfs(source, sink, parent, graph, capacity):
        path_flow = float('Inf')
        s = sink
            
        while s != source:
            path_flow = min(path_flow, capacity[(parent[s], s)])
            s = parent[s]
            
        max_flow += path_flow
            
        v = sink
        while v != source:
            u = parent[v]
            capacity[(u, v)] -= path_flow
            capacity[(v, u)] += path_flow
            v = parent[v]
        
    return max_flow, capacity


test_cases = int(v[0])
v = v[1:]
for _ in range(test_cases):
    n, m = map(int, v[0].split())
    required_difficulties = v[1].split()
    required_topics = v[2].split()
    questions = [v[3 + i].split() for i in range(n)]

    graph = defaultdict(list)
    capacity = defaultdict(int)
    
    difficulties = list(set(required_difficulties))
    topics = list(set(required_topics))
    graph_size = 2 + len(difficulties) + len(topics)
    
    source = 0
    sink = graph_size - 1
    
    # Map difficulties and topics to unique indices
    difficulty_to_index = {difficulty: i + 1 for i, difficulty in enumerate(difficulties)}
    topic_to_index = {topic: i + 1 + len(difficulties) for i, topic in enumerate(topics)}
    
    # Add edges from source to each unique difficulty node
    for difficulty in required_difficulties:
        graph[source].append(difficulty_to_index[difficulty])
        graph[difficulty_to_index[difficulty]].append(source)
        capacity[(source, difficulty_to_index[difficulty])] += 1
    
    # Add edges from each unique topic node to sink
    for topic in required_topics:
        graph[topic_to_index[topic]].append(sink)
        graph[sink].append(topic_to_index[topic])
        capacity[(topic_to_index[topic], sink)] += 1
    
    # Add edges between difficulty nodes and topic nodes based on the questions
    for name, topic, difficulty in questions:
        if difficulty in difficulty_to_index and topic in topic_to_index:
            graph[difficulty_to_index[difficulty]].append(topic_to_index[topic])
            graph[topic_to_index[topic]].append(difficulty_to_index[difficulty])
            capacity[(difficulty_to_index[difficulty], topic_to_index[topic])] += 1
    r, capacity = edmonds_karp(source, sink, graph, capacity)
    if r == m:
        sys.stdout.write("Yes\n")
    else:
        sys.stdout.write("No\n")
    v = v[3 + n:]


