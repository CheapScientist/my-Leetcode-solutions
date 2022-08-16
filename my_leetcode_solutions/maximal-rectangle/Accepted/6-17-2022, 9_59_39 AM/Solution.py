// https://leetcode.com/problems/maximal-rectangle

class Solution:
    def maximalRectangle(self, A: List[List[str]]) -> int:
        rows, cols = len(A), len(A[0])
        dp = [[0]*cols for _ in range(rows)]
        for c in range(cols): 
            dp[0][c] = 1 if A[0][c] == '1' else 0
        for r in range(1, rows): 
            for c in range(cols): 
                if A[r][c] == '1': 
                    dp[r][c] = 1 + dp[r - 1][c]
        ans = 0
        for r in range(rows): 
            B = dp[r]
            stack = [(-1, -1)] # height, idx
            B.append(0)
            for idx, height in enumerate(B):
                newIdx = idx
                while stack and stack[-1][0] > height: 
                    prevHeight, prevIdx = stack.pop()
                    ans = max(ans, prevHeight*(idx - prevIdx))
                    newIdx = prevIdx
                stack.append((height, newIdx))
        return ans