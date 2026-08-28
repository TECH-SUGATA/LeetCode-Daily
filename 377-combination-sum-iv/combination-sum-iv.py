class Solution:
    def combinationSum4(self, nums, target):
        dp = [0] * (target + 1)

       
        dp[0] = 1

        for total in range(1, target + 1):
            for num in nums:
                if num <= total:
                    dp[total] += dp[total - num]

        return dp[target]