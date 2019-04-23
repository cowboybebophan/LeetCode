class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return []
        digit_map = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        results = ['']
        for digit in digits:
            results = [result + d for result in results for d in digit_map[digit]]
        return results
 
 """
 
 Note:
 运用了递归与列表生成式
 例如 digits = '23', 先将results列表初始化为[''], 第一次进入for循环后results = ["a","b","c"](""+"a",""+"b",""+"c"),
 之后进行递归，对当前results中的每个元素和下一个digit:'3'中的字母"d","e","f"分别两两叠加，
 更新results = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
 
 注意：初始化为results = ['']而不是[ ]
 
 """

 
