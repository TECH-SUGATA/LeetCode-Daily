class Solution:
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        greater = {}

        for num in reversed(nums2):
            while stack and stack[-1] <= num:
                stack.pop()

            if stack:
                greater[num] = stack[-1]
            else:
                greater[num] = -1

            stack.append(num)

        return [greater[num] for num in nums1]