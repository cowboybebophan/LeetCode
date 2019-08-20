# similar to 503 and 739
class Solution:
    def nextLargerNodes(self, head):
        
        res, stack = [], [] # Be carefule here, do Not initialize like this: res = stack = []
                            # because res and stack points to the same reference and they will change together as [] changes.
        while head:
            while stack and stack[-1][1] < head.val:
                res[stack.pop()[0]] = head.val
            stack.append([len(res), head.val])
            res.append(0)
            head = head.next
        return res
