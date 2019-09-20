"""
Disjoint Set / Union-find
https://www.youtube.com/watch?v=VJnUwsE4fWA
https://zxi.mytechroad.com/blog/data-structure/sp1-union-find-set/
"""
# Union-find based on rank
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)]
        rank = [1 for i in range(len(edges) + 1)]
        
        def find(u):
            if parent[u] == u:
                return u
            parent[u] = find(parent[u])
            return parent[u]
        
        def union(u, v):
            pu, pv = find(u), find(v)
            if pu == pv:
                return False
            if rank[pu] < rank[pv]:
                parent[pu] = pv
            elif rank[pu] > rank[pv]:
                parent[pv] = pu
            else:
                parent[pv] = pu
                rank[pu] += 1
            return True
        
        for u, v in edges:
            if not union(u, v):
                return [u,v]

# Union-find (does not based on rank)
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)]
        
        def find(u):
            if parent[u] == u:
                return u
            parent[u] = find(parent[u])
            return parent[u]
        
        def union(u, v):
            pu, pv = find(u), find(v)
            if pu == pv:
                return False
            parent[pv] = pu
            return True
        
        for u, v in edges:
            if not union(u, v):
                return [u,v]
