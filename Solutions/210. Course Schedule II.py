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
        
