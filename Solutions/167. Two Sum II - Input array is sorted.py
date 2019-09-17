class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res, L, R = [], 1, len(numbers)
        
        while L < R:
            if numbers[L - 1] + numbers[R - 1] == target:
                res = [L, R]
                return res
            elif numbers[L - 1] + numbers[R - 1] > target:
                R -= 1
            else:
                L += 1
