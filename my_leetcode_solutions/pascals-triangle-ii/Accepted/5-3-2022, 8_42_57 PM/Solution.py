// https://leetcode.com/problems/pascals-triangle-ii

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # initialize data set:
        ans = []
        for i in range(1, rowIndex + 2):
            ans.append([0]*i)
        for i in ans:
            i[0], i[-1] = 1, 1
        if rowIndex < 2:
            return ans[-1]
        for i in range(2, rowIndex + 2):
            for j in range(i - 1):
                if ans[i - 1][j] == 0:
                    ans[i - 1][j] = ans[i - 2][j] + ans[i - 2][j - 1]
        return ans[-1]