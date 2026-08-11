class Solution:
    def missingInteger(self, nums):
        s = nums[0]

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                s += nums[i]
            else:
                break

        while s in nums:
            s += 1

        return s