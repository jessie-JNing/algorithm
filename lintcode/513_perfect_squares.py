"""
Test Case:

1
"""


class Solution:
    """
    @param: n: a positive integer
    @return: An integer
    """
    def numSquares(self, n):
        if not n:
            return 0

        INFINITY = float('inf')

        # `dp[i]` means the least number of perfect square numbers of `i`
        dp = [INFINITY] * (n + 1)
        dp[0] = 0
        dp[1] = 1

        for i in range(1, n + 1):
            for j in range(1, i):
                if j * j > i:
                    break
                dp[i] = min(dp[i], dp[i - j * j] + 1)

        return dp[n]
