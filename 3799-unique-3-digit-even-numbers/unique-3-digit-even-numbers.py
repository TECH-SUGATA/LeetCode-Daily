class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        ans = set()

        for i in range(len(digits)):
            for j in range(len(digits)):
                for k in range(len(digits)):
                    # Same copy cannot be used twice
                    if i == j or j == k or i == k:
                        continue

                    # First digit cannot be 0
                    if digits[i] == 0:
                        continue

                    # Last digit must be even
                    if digits[k] % 2 != 0:
                        continue

                    num = digits[i] * 100 + digits[j] * 10 + digits[k]
                    ans.add(num)

        return len(ans)