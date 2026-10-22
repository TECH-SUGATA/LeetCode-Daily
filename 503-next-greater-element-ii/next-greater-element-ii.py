
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [-1] * n
        stack = []

        for i in range(2 * n):
            idx = i % n

            while stack and nums[stack[-1]] < nums[idx]:
                result[stack.pop()] = nums[idx]

            if i < n:
                stack.append(idx)

        return result
