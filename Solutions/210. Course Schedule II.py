"""
This problem is a follow-up of problem 207.

The difference is that we are asked to return the ordering of the courses.

Here we can just return the list we are maintaining: zeroDegree. 

We append a course number to zeroDegree everytime a course doesn't require any prerequisite course anymore.
Therefore, zeroDegree stores the ordering of the courses we take.

"""

class Solution:
    def findOrder(self, n, pairs):
        G = [[] for _ in range(n)]
        degree = [0 for _ in range(n)]
        
        for course, pre in pairs:
            G[pre].append(course)   # the courses in G[pre] are the courses that requires pre as a prerequisite
            degree[course] += 1
        
        zeroDegree = [i for i in range(n) if degree[i] == 0]
        
        if len(zeroDegree) == 0: return []
        
        for i in zeroDegree:
            for j in G[i]:
                degree[j] -= 1
                if degree[j] == 0:
                    zeroDegree.append(j)
        
        if len(zeroDegree) == n:
            return zeroDegree
        else:
            return []
        
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
