# 3084 - Given a string s and a character c, return the total number of substrings of s that start and end with c.
class Solution(object):
    def countSubstrings(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: int
        """
        cnt = 0
        substrings = 0
        for v in s:
            if v==c:
                substrings = substrings+cnt+1
                cnt += 1
        return substrings

