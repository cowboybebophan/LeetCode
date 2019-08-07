class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}
        for item in s:
            dic[item] = dic.get(item, 0) + 1
        for item in t:
            if item not in dic:
                return False
            dic[item] -= 1
        for k in dic:
            if dic[k] != 0:
                return False
        return True
