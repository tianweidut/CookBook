class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0

        l1, l2 = len(text1), len(text2)
        self.dp = [[0] *(l2+1) for i in range(0, l1+1)]
        
        for i in range(1, l1+1):
            for j in range(1, l2+1):
                if text1[i-1] == text2[j-1]:
                    self.dp[i][j] = self.dp[i-1][j-1] + 1
                else:
                    self.dp[i][j] = max(self.dp[i][j-1], self.dp[i-1][j]) 
        
        return self.dp[i][j]