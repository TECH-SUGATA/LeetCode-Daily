class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        min_odd = float('inf')

        # Find the smallest odd number
        for x in nums1:
            if x % 2 == 1:
                min_odd = min(min_odd, x)

        # If there is an odd number smaller than an even number,
        # the even number cannot be changed to odd.
        for x in nums1:
            if x % 2 == 0 and min_odd != float('inf') and x < min_odd:
                return False

        return True