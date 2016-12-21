'''
Created on Dec 18, 2016

@author: Yuehan
'''
class Solution(object):
    def rob(self, nums):
        
        last, now = 0, 0
        for i in nums: 
            last, now = now, max(last + i, now)
        return now
    
print(Solution.rob(0, [2,4,1,2,1]))