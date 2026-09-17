class Solution:
    def maxProduct(self, nums):
        current_max = nums[0]
        current_min = nums[0]
        answer = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]

            # If num is negative, max and min are swapped
            if num < 0:
                current_max, current_min = current_min, current_max

            current_max = max(num, current_max * num)
            current_min = min(num, current_min * num)

            answer = max(answer, current_max)

        return answer