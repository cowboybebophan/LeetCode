"""
caikehe大神的答案： https://leetcode.com/problems/single-number/discuss/43000/Python-different-solutions.

Using bitwise XOR:

^ : 按位异或运算符：当两对应的二进位相异时，结果为1
60 ^ 13 = 0011 1100 ^ 0000 1101 = 0011 0001 = 49

又因为a ^ b = b ^ a, (XOR is commutative)
所以按位异或运算符可以交换位置: 4 ^ 1 ^ 2 ^ 1 ^ 2 = ( 4 ) ^ (1 ^ 1) ^ (2 ^ 2) = 4 ^ 0 ^ 0 = 4

"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res ^= num
        return res
