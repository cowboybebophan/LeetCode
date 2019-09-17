class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        res, L, R = [], 0, len(A) - 1
        while L <= R:
            if abs(A[L]) > abs(A[R]):
                res.append(A[L] ** 2)
                L += 1
            else:
                res.append(A[R] ** 2)
                R -= 1
        return res[::-1]
