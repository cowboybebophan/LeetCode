class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        i, j, sz = 0, 1, len(A)
        
        while i < sz and j < sz:
            if A[i] % 2 == 0:
                i += 2
            elif A[j] % 2 == 1:
                j += 2
            else:   # A[i] % 2 == 1 and A[j] % 2 == 0
                A[i], A[j] = A[j], A[i]
                i += 2
                j += 2
        
        return A
