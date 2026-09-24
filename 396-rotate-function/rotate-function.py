class Solution:
    def maxRotateFunction(self, nums):
        n = len(nums)

        total = sum(nums)

        # F(0)
        current = sum(i * nums[i] for i in range(n))

        maximum = current

        # Calculate F(1) ... F(n-1)
        for i in range(n - 1, 0, -1):
            current = current + total - n * nums[i]
            maximum = max(maximum, current)

        return maximum