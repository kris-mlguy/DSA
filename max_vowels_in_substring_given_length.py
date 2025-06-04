# Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.
class Solution(object):
    def maxVowelsBruteForce(self, s, k):
        """
        Brute force method
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
     def maxVowelsSlidingWindow(self, s, k):
        """
        Sliding window method
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        vowels = {'a','e','i','o','u'}
        p1, curr_sum, max_sum = 0, 0, 0
        for p2 in range(n):
            curr_sum += 1 if s[p2] in vowels else 0
            if p2-p1+1>k:
                curr_sum -= 1 if s[p1] in vowels else 0
                p1+=1
            max_sum = max(max_sum,curr_sum)
        return max_sum
