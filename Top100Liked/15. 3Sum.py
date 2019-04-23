class Solution:
    def threeSum(self, nums):
        res = []
        nums.sort()
        length = len(nums)
        for i in range(length - 2):
            if nums[i] > 0: break
            if i > 0 and nums[i] == nums[i-1]:continue
            
            L, R = i + 1, length - 1
            while L < R:    
                total = nums[i] + nums[L] + nums[R]
                if total > 0:
                    R -= 1
                elif total < 0:
                    L += 1
                else:
                    res.append([nums[i], nums[L], nums[R]])
                    while L < R and nums[L] == nums[L+1]:
                        L += 1
                    while L < R and nums[R] == nums[R-1]:
                        R -= 1
                    L += 1; R -= 1
        return res
        
  """
  # This note comes from christopherwu0529 on LeetCode (https://github.com/wuduhren/leetcode-python)
  
  The main idea is to iterate every number in nums.
	We use the number as a target to find two other numbers which make total zero.
	For those two other numbers, we move pointers, l and r, to try them.
	
  l start from left to right
	r start from right to left
	
  First, we sort the array, so we can easily move i around and know how to adjust l and r.
	If the number is the same as the number before, we have used it as target already, continue. [1]
	We always start the left pointer from i+1 because the combination of 0~i has already been tried. [2]
	
  Now we calculate the total:
	If the total is less than zero, we need it to be larger, so we move the left pointer. [3]
	If the total is greater than zero, we need it to be smaller, so we move the right pointer. [4]
	If the total is zero, bingo! [5]
	We need to move the left and right pointers to the next different numbers, so we do not get repeating result. [6]
	
  We do not need to consider i after nums[i]>0, since sum of 3 positive will be always greater than zero. [7]
	We do not need to try the last two, since there are no rooms for l and r pointers.
	You can think of it as The last two have been tried by all others. [8]
	
  For time complexity
	Sorting takes O(NlogN)
	Now, we need to think as if the 'nums' is really really big
	We iterate through the 'nums' once, and each time we iterate the whole array again by a while loop
	So it is O(NlogN+N^2)~=O(N^2)
	
  For space complexity
	We didn't use extra space except the 'res'
	Since we may store the whole 'nums' in it
	So it is O(N)
	N is the length of 'nums'
  """
