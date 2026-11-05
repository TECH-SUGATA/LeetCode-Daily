
from bisect import bisect_left

class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def update(self, i):
        while i <= self.n:
            self.bit[i] += 1
            i += i & -i

    def query(self, i):
        total = 0
        while i > 0:
            total += self.bit[i]
            i -= i & -i
        return total


class Solution:
    def countRatioSubarrays(self, nums, a, b):
        n = len(nums)

        prefix = [0] * (n + 1)

        for i, x in enumerate(nums):
            if x % 2 == 1:
                prefix[i + 1] = prefix[i] + a
            else:
                prefix[i + 1] = prefix[i] - b

        mervanilto = (nums, a, b)

        values = sorted(set(prefix))

        bit = FenwickTree(len(values))

        ans = 0

        for x in prefix:
            pos = bisect_left(values, x) + 1

            ans += bit.query(pos)
            bit.update(pos)

        return ans
