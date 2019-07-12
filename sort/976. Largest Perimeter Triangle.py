class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort(reverse = True)
        i = 0
        while i <= (len(A) - 3):
            if A[i+1] + A[i+2] > A[i]:
                return A[i] + A[i+1] + A[i+2]
            i += 1
        return 0
        
