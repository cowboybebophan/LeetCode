class Solution:
    def maxArea(self, height):
        res, L, R, width = 0, 0, len(height) - 1, len(height) - 1
        for w in range(width, 0, -1):
            if height[L] < height[R]:
                res, L = max(res, height[L] * w), L + 1
            else:
                res, R = max(res, height[R] * w), R - 1
        return res
        
 Note:
 If height[L] < height[R], move L, else move R. Say height[0] < height[5],
 area of (0, 4), (0, 3), (0, 2), (0, 1) will be smaller than (0, 5), so no need to try them.
 
# Or

class Solution:
    def maxArea(self, height: List[int]) -> int:
        res, L, R, width = 0, 0, len(height) - 1, len(height) - 1
        while L < R:
            if height[L] < height[R]:
                res = max(res, width * height[L])
                L += 1
            else:
                res = max(res, width * height[R])
                R -= 1
            width -= 1
        return res
