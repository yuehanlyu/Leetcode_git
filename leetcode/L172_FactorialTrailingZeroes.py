'''
Created on Dec 18, 2016

@author: Yuehan
'''
import math
class Solution(object):
    def trailingZeroes(self, n):
        '''return 0 if n == 0 else int(n / 5 + Solution.trailingZeroes(self,n / 5))'''
        
        if (n==0):
            return 0
        digts=math.floor(math.log(n)/math.log(5))
        a=0;
        result=0;
        while (digts):
            a=math.floor(n/(5**digts))-math.floor(n/(5**(digts+1)))
            result=result+a*digts
            digts=digts-1
        return int(result)
       

print(Solution.trailingZeroes(0,200))
