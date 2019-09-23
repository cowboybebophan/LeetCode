"""
Idea comes from here:
https://leetcode.com/problems/course-schedule/discuss/162743/JavaC%2B%2BPython-BFS-Topological-Sorting-O(N-%2B-E)

Instead of using a dic, we store the pairs in a list G: index represents the courses, G[i] represents the courses that require
course i as a prerequisite course. For example: G[3] = [2,4] means course 2 and 4 both require course 3.

degree[] represents how many pre courses a course still needs before we take it.
For example: degree[4] = 3 means we need to take 3 more prerequisite courses before we can take course 4.

We maintain a list zeroDegree: it stores the courses(represented by index) that we can already take which means degree[i] == 0

If len(zeroDegree) == n, we know that we can take all the courses.
Otherwise, return False.

"""

class Solution:
    def canFinish(self, n, pairs):
        G = [[] for _ in range(n)]
        degree = [0 for _ in range(n)]
        
        for course, pre in pairs:
            G[pre].append(course)   # the courses in G[pre] are the courses that requires 'pre' as a prerequisite course
            degree[course] += 1     # degree[course] represents how many pre courses do we still need to take a certain course
        
        zeroDegree = [i for i in range(n) if degree[i] == 0]
        
        if len(zeroDegree) == 0: return False
        
        for i in zeroDegree:
            for j in G[i]:
                degree[j] -= 1
                if degree[j] == 0:
                    zeroDegree.append(j)
        return len(zeroDegree) == n

# Topological Sorting + DFS

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        visited = [0 for _ in range(numCourses)]
        
        for x, y in prerequisites:
            graph[x].append(y)
        
        for i in range(numCourses):
            if not self.dfs(graph, visited, i):
                return False
        return True
    
    
    def dfs(self, graph, visited, i):
        if visited[i] == -1:
            return False
        if visited[i] == 1:
            return True
        visited[i] = -1
        
        for j in graph[i]:
            if not self.dfs(graph, visited,j):
                return False
        
        visited[i] = 1
        return True
        
