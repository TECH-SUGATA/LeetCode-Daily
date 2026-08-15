class Solution:
    def longestSubsequence(self, nums):
        x = 0
        zeros = 0

        for n in nums:
            x ^= n
            if n == 0:
                zeros += 1

        if x != 0:
            return len(nums)

        if zeros == len(nums):
            return 0

        return len(nums) - 1