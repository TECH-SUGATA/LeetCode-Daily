
from typing import List

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def digit_sum(n):
            return sum(int(d) for d in str(n))

        sorted_nums = sorted(nums, key=lambda x: (digit_sum(x), x))
        target = {num: i for i, num in enumerate(sorted_nums)}

        visited = [False] * len(nums)
        swaps = 0

        for i in range(len(nums)):
            if visited[i] or target[nums[i]] == i:
                continue

            cycle_size = 0
            j = i

            while not visited[j]:
                visited[j] = True
                j = target[nums[j]]
                cycle_size += 1

            swaps += cycle_size - 1

        return swaps
