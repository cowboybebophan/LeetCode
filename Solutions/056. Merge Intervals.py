"""
Sort the list first, then compare the start i[0] in each interval with the end of the last interval in res: res[-1][1];
If i[0] <= res[-1][1], it means there is overlapping so we merge them into one.
If i[0] > res[-1][1], it means there is no overlapping so we append the interval into res.

"""
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res=[]
        for i in sorted(intervals):
            if res and i[0] <= res[-1][1]:
                res[-1][1] = max(res[-1][1], i[1])
            else:
                res.append(i)
        return res
        
