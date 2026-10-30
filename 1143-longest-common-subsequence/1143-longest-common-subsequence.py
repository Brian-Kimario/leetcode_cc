class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        m, n = len(text1), len(text2)
        
        # Create a 2D DP array initialized with 0
        # Dimensions are (m + 1) x (n + 1)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Build the DP table bottom-up
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # If characters match, take the diagonal value and add 1
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                # If they don't match, take the maximum of skipping a character from text1 or text2
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                    
        # The bottom-right cell contains the length of the LCS
        return dp[m][n]
