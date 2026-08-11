class Solution:
    def rob(self, nums):
        prev = curr = 0

        for money in nums:
            prev, curr = curr, max(curr, prev + money)

        return curr