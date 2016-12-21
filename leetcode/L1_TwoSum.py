'''
Created on Dec 20, 2016

@author: Yuehan

Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        #test 5:26
        """
        ndict = {k: [] for k in nums}
        j=0
        for i in nums:
            ndict[i].append(j)
            if target-i in ndict and len(ndict[target-i])>0:
                if i!=(target/2):
                    return [min(j, ndict[target-i][0]),max(j, ndict[target-i][0])]
                else:
                    if len(ndict[i])>1:
                        return [ndict[target-i][0],ndict[target-i][1]]
            j=j+1
print(Solution.twoSum(0, [0,4,3,0], 0))