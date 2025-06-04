class Solution(object):
    def maxVowels(self, s, k):
        """
        Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        p1, p2 = 0,k-1
        vowels = ['a','e','i','o','u']
        max_sum = 0
        for i in range(n-k+1):
            curr_sum = 0
            for j in range(i,i+k):
                if s[j] in vowels:
                    curr_sum +=1
            if curr_sum > max_sum:
                max_sum = curr_sum     
        return max_sum
