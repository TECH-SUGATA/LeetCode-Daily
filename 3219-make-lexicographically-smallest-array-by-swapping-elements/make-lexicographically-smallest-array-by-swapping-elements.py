class Solution:
    def lexicographicallySmallestArray(self, nums, limit):
        n = len(nums)

        # Store (value, original index)
        arr = sorted((value, i) for i, value in enumerate(nums))

        ans = nums[:]

        start = 0

        while start < n:
            end = start

            # Find one connected group
            while (
                end + 1 < n
                and arr[end + 1][0] - arr[end][0] <= limit
            ):
                end += 1

            # Original indices of this group
            indices = sorted(arr[i][1] for i in range(start, end + 1))

            # Values of this group are already sorted
            values = [arr[i][0] for i in range(start, end + 1)]

            # Put smallest values at smallest indices
            for idx, value in zip(indices, values):
                ans[idx] = value

            start = end + 1

        return ans