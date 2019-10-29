# Python 2.x
from collections import defaultdict

class Solution:
    def criticalConnections(self, n, connections):
        g = defaultdict(list)
        res = []
        [root_seq, parent] = [[n] * n for _ in range(2)]
        visited = [False] * n
        self.seq = 0

        for u, v in connections:
            g[u].append(v)
            g[v].append(u)

        def dfs(u):
            visited[u] = True
            curr_seq = root_seq[u] = self.seq
            self.seq += 1

            for v in g[u]:
                if not visited[v]:
                    parent[v] = u
                    dfs(v)

                    if root_seq[v] > curr_seq:
                        res.append([u, v])

                if parent[u] != v:
                    root_seq[u] = min(root_seq[u], root_seq[v])

        dfs(0)
        return res  
        
# Python 3.x
from collections import defaultdict

class Solution:
    def criticalConnections(self, n, connections):
        g = defaultdict(list)
        res = []
        [root_seq, parent] = [[n] * n for _ in range(2)]
        visited = [False] * n
        seq = 0

        for u, v in connections:
            g[u].append(v)
            g[v].append(u)

        def dfs(u):
            nonlocal seq
            visited[u] = True
            curr_seq = root_seq[u] = seq
            seq += 1

            for v in g[u]:
                if not visited[v]:
                    parent[v] = u
                    dfs(v)

                    if root_seq[v] > curr_seq:
                        res.append([u, v])

                if parent[u] != v:
                    root_seq[u] = min(root_seq[u], root_seq[v])

        dfs(0)
        return res 
