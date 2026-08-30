class Solution:
    def minimumDeletions(self, nums: list[int]) -> int:
        n = len(nums)

        min_pos = nums.index(min(nums))
        max_pos = nums.index(max(nums))

        left = min(min_pos, max_pos)
        right = max(min_pos, max_pos)

        # 3 possible ways:
        # 1. Remove both from the front
        # 2. Remove both from the back
        # 3. Remove one from front and one from back

        front = right + 1
        back = n - left
        both = (left + 1) + (n - right)

        return min(front, back, both)