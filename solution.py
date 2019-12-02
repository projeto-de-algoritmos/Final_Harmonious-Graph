n, m = map(int, input().split())
graph = [list() for i in range(n+1)]
visited = [False for i in range(n+1)]

for i in range(m):
    u, v = map(int, input().split())
    graph[v].append(u)
    graph[u].append(v)
 
ans = 0
count = m = 1
stack = [count]

while count <= n:
    while (len(stack) > 0):
        v = stack.pop()
        visited[v] = True
        m = max(v, m)
        for e in graph[v]:
            if not visited[e]:
                stack.append(e)
                visited[e] = True
    while count <= n and visited[count]:
        count += 1
    if count <= m:
        ans += 1
    stack.append(count)
print(ans)
