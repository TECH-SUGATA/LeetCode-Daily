class Solution:
    def sumDistance(self, nums: List[int], s: str, d: int) -> int:
        MOD = 10**9 + 7

        # Calculate each robot's final position
        positions = []
        for i in range(len(nums)):
            if s[i] == 'L':
                positions.append(nums[i] - d)
            else:
                positions.append(nums[i] + d)

        # Sort the final positions
        positions.sort()

        # Calculate sum of distances using prefix sum
        ans = 0
        prefix = 0

        for i, pos in enumerate(positions):
            ans = (ans + i * pos - prefix) % MOD
            prefix += pos

        return ans