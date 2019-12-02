from collections import defaultdict
import threading, sys

sys.setrecursionlimit(10**8)

visited = [False] * 200010
graph = defaultdict(set)


def read():
    return sys.stdin.readline().split()
 
def dfs(start):
    visited[start] = True
    ret = start
    for v in graph[start]:
        if not visited[v]:
            ret = max(dfs(v), ret)
    return ret
 
def main():
    n, m = map(int, read())

    for _ in range(m):
        u, v = map(int, read())
        u, v = u-1, v-1

        graph[u].add(v)
        graph[v].add(u)

    max_r = 0
    ans = 0
    for l in range(n):
        if not visited[l]:
            r = dfs(l)
            if l < max_r:
                ans += 1
            max_r = max(r, max_r)
 
    print(ans)
 
 
if __name__ == "__main__":
    threading.stack_size(1024 * 100000)

    thread = threading.Thread(target=main)
    thread.start()
    thread.join()
