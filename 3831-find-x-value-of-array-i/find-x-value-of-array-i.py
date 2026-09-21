class Solution:
    def resultArray(self, nums, k):
        result = [0] * k

        # dp[r] = number of subarrays ending at previous position
        # whose product % k == r
        dp = [0] * k

        for num in nums:
            new_dp = [0] * k

            # Start a new subarray with only nums[i]
            r = num % k
            new_dp[r] += 1

            # Extend all previous subarrays
            for prev_r in range(k):
                if dp[prev_r]:
                    new_r = (prev_r * num) % k
                    new_dp[new_r] += dp[prev_r]

            dp = new_dp

            # Add all subarrays ending here to the answer
            for r in range(k):
                result[r] += dp[r]

        return result