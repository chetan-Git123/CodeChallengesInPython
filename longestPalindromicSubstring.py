'''
Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"
 
Constraints:
1 <= s.length <= 1000
s consist of only digits and English letters.
'''
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        #h1
        n = len(s)
        if n == 0:
            return ""
        
        start = 0
        max_length = 1
        
        dp = [[False] * n for _ in range(n)]
        
        for i in range(n):
            dp[i][i] = True  # Single characters are palindromes
        
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                
                if s[i] == s[j]:
                    if length == 2:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                    
                    if dp[i][j] and length > max_length:
                        start = i
                        max_length = length
        
        return s[start:start + max_length]
