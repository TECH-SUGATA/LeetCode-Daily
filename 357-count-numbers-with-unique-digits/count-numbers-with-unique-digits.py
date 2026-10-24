class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1

        n = min(n, 10)
        total = 10
        count = 9
        available = 9

        for i in range(2, n + 1):
            count *= available
            total += count
            available -= 1

        return total