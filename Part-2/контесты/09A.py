

n, m, s = list(map(int, input().split()))
a = [[] for _ in range(n)]

for i in range(m):
    k, t, w = list(map(int, input().split()))
    a[k].append([t, w])
    #a[t].append([k, w])


d = [float("inf")] * n
d[s] = 0
used = [False] * n

while True:
    u = -1
    for i in range(n):
        if used[i] == False and (u == -1 or d[i] < d[u]):
            u = i
    if u == -1 or d[u] == float("inf"):
        break
    used[u] = True
    for v, w in a[u]:
        d[v] = min(d[v], d[u] + w)
path = d
for e in range(len(path)):
    if path[e] == float('inf'):
        path[e] = 'UDF'

print(*path)