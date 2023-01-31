from math import inf
import heapq


V, m = map(int, input().split())

graph = [[] for _ in range(V + 1)]
revgraph = [[] for _ in range(V + 1)]
edges = []

def addConnection(x, y, w, g):
    g[x].append((w, y))  # Connection represented by (node, weight) in adjacency list

for i in range(m):
    x, y, w = map(int, input().split())
    edges.append([x, y, w])
    addConnection(x, y, w, graph)
    addConnection(y, x, w, revgraph)


s = 1  # Starting node

distorg = [0 for _ in range(V + 1)]
vis = [0 for _ in range(V + 1)]
pq = []


for i in range(V + 1):
    distorg[i] = inf
distorg[s] = 0

heapq.heappush(pq, (0, s))
while len(pq):
    d, n = heapq.heappop(pq)
    if vis[n]:
        continue
    else:
        vis[n] = 1
    for edge in graph[n]:
        w, v = edge
        if d + w < distorg[v]:
            distorg[v] = d + w
            heapq.heappush(pq, (distorg[v], v))

s = V
distend = [0 for _ in range(V + 1)]
vis = [0 for _ in range(V + 1)]
pq = []

for i in range(V + 1):
    distend[i] = inf
distend[s] = 0

heapq.heappush(pq, (0, s))
while len(pq):
    d, n = heapq.heappop(pq)
    if vis[n]:
        continue
    else:
        vis[n] = 1
    for edge in revgraph[n]:
        w, v = edge
        if d + w < distend[v]:
            distend[v] = d + w
            heapq.heappush(pq, (distend[v], v))

shortest = distorg[-1]
mini = inf
for x, y, w in edges:
    path = distorg[x] + w + distend[y]
    if path > shortest:
        mini = min(path, mini)
if mini == inf:
    print(-1)
else:
    print(mini)
