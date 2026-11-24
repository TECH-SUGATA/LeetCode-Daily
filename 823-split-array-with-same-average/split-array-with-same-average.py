class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)

        # Check possible subset sizes
        valid_sizes = [
            k for k in range(1, n // 2 + 1)
            if (total * k) % n == 0
        ]

        if not valid_sizes:
            return False

        mid = n // 2
        left = nums[:mid]
        right = nums[mid:]

        # Store right subset sums by subset size
        m = len(right)
        right_sums = [set() for _ in range(m + 1)]
        sums = [0] * (1 << m)

        for mask in range(1 << m):
            if mask:
                bit = mask & -mask
                idx = bit.bit_length() - 1
                sums[mask] = sums[mask ^ bit] + right[idx]

            right_sums[mask.bit_count()].add(sums[mask])

        # Check left subsets
        m = len(left)
        sums = [0] * (1 << m)

        for mask in range(1 << m):
            if mask:
                bit = mask & -mask
                idx = bit.bit_length() - 1
                sums[mask] = sums[mask ^ bit] + left[idx]

            count = mask.bit_count()

            for k in valid_sizes:
                remaining = k - count

                if 0 <= remaining < len(right_sums):
                    target = (total * k) // n - sums[mask]

                    if target in right_sums[remaining]:
                        return True

        return False