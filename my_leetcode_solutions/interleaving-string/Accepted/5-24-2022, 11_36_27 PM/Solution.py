// https://leetcode.com/problems/interleaving-string

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1, l2, l3 = len(s1), len(s2), len(s3)
        if l1 + l2 != l3:
            return False
        if not s1:
            return s2 == s3
        if not s2: return s1 == s3
        
        dp = [[False]*(l1 + 1) for _ in range(l2 + 1)]
        dp[0][0] = (s1[0] == s3[0] or s2[0] == s3[0])
        
        for i in range(1, l1 + 1):
            dp[0][i] = (s1[i - 1] == s3[i - 1] and dp[0][i - 1])
        
        for j in range(1, l2 + 1):
            dp[j][0] = (s2[j - 1] == s3[j - 1] and dp[j - 1][0])
        
        for i in range(1, l2 + 1):
            for j in range(1, l1 + 1):
                dp[i][j] = (s2[i - 1] == s3[i + j - 1] and dp[i - 1][j]) or (s1[j - 1] == s3[i + j - 1] and dp[i][j - 1])
        return dp[-1][-1]
        