// https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings

class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n, m = len(s1), len(s2)
            
        @cache
        def dfs(i, j): # i -> idx of s1, j -> idx of s2
            if i == n and j == m: 
                return 0
            if i == n and j < m: 
                ans = 0
                for k in range(j, m):
                    ans += ord(s2[k])
                return ans
            if i < n and j == m: 
                ans = 0
                for k in range(i, n):
                    ans += ord(s1[k])
                return ans
            if s1[i] == s2[j]: 
                return dfs(i + 1, j + 1)
            else:
                return min(ord(s1[i]) + dfs(i + 1, j), ord(s2[j]) + dfs(i, j + 1))
        return dfs(0, 0)
                