class Solution:
    def firstStableIndex(self, nums, k):
        n = len(nums)
        
        suffix = [0] * n
        suffix[-1] = nums[-1]

        for i in range(n - 2, -1, -1):
            suffix[i] = min(nums[i], suffix[i + 1])

        mx = nums[0]

        for i in range(n):
            mx = max(mx, nums[i])

            if mx - suffix[i] <= k:
                return i

        return -1