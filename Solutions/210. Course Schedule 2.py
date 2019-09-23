# Topological Sorting + DFS
# https://www.youtube.com/watch?v=Qqgck2ijUjU

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        order = []
        n = numCourses
        graph = [[] for _ in range(n)]
        visited = [0 for _ in range(n)]
        
        for course, pre in prerequisites:
            graph[pre].append(course)
            
        for i in range(n):
            if not self.dfs(visited, graph, order, i):
                return []
        return order[::-1]
    
    def dfs(self, visited, graph, order, i):
        if visited[i] == -1:
            return False
        if visited[i] == 1:
            return True
        
        visited[i] = -1
        
        for j in graph[i]:
            if not self.dfs(visited, graph, order, j):
                return False
        
        visited[i] = 1
        
        order.append(i)
        return True
