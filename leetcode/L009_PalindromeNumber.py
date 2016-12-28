import math

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s=str(x)
        l=len(s)
        isP=True
        for i in range(int(math.floor((l+1)/2))):
        	if s[i]!=s[l-1-i]:
        		isP=False
        		break
        return isP

s1=Solution()
print Solution.isPalindrome(s1,030)