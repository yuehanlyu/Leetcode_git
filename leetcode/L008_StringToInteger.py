'''
Created on Dec 21, 2016
This is to learn how to write regular expression    
@author: Google (not me)
'''
import re
class Solution(object):
    def atoi(self, str):
        str = str.strip()
        str = re.findall('(^[\+\-0]*\d+)\D*', str)

        try:
            result = int(''.join(str))
            MAX_INT = 2147483647
            MIN_INT = -2147483648
            if result > MAX_INT > 0:
                return MAX_INT
            elif result < MIN_INT < 0:
                return MIN_INT
            else:
                return result
        except:
            return 0

print(Solution.atoi(1, '1+-'))