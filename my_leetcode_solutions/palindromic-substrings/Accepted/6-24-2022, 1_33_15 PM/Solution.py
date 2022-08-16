// https://leetcode.com/problems/palindromic-substrings

class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        n = len(s)
        for i in range(n):
            # first check odd-length palindroms
            l, r = i, i
            while l >= 0 and r < n and s[r] == s[l]:
                ans += 1
                l -= 1
                r += 1
            # then check even-length ones
            l, r = i, i + 1
            while l >= 0 and r < n and s[r] == s[l]:
                ans += 1
                l -= 1
                r += 1
        return ans