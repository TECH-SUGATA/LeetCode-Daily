
class Solution:
    def countOperationsToEmptyArray(self, nums: List[int]) -> int:
        n = len(nums)

        # Sort indices by their corresponding values
        indices = sorted(range(n), key=lambda i: nums[i])

        # Fenwick Tree (BIT)
        bit = [0] * (n + 1)

        def update(i):
            while i <= n:
                bit[i] += 1
                i += i & -i

        def query(i):
            total = 0
            while i > 0:
                total += bit[i]
                i -= i & -i
            return total

        ans = 0
        prev = -1

        for idx in indices:
            if idx > prev:
                ans += (idx - prev) - (query(idx + 1) - query(prev + 1))
            else:
                ans += (n - prev + idx) - (
                    query(n) - query(prev + 1) + query(idx + 1)
                )

            # Mark this index as removed
            update(idx + 1)
            prev = idx

        return ans
