'''
Created on Dec 21, 2016

@author: Yuehan
'''
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        a=0
        if x>=0:
            a= int(str(x)[::-1])
        if x<0:
            a= -int(str(-x)[::-1])
        if a>2147483647 or a<-2147483647:
            return 0
        else:
            return a
print(Solution.reverse(1,-3120))
        