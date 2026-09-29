class Solution:
    def smallestGoodBase(self, n: str) -> str:
        n = int(n)

        # Maximum possible number of digits
        # Example: n = 13 -> binary is 1101, so max m = 3
        max_m = n.bit_length() - 1

        # Try maximum length first because it can give the smallest base
        for m in range(max_m, 1, -1):
            
            # k^m <= n, so k <= n^(1/m)
            left = 2
            right = int(n ** (1 / m)) + 1

            while left <= right:
                k = (left + right) // 2

                # Calculate 1 + k + k^2 + ... + k^m
                total = 1
                power = 1

                for _ in range(m):
                    power *= k
                    total += power

                    if total > n:
                        break

                if total == n:
                    return str(k)

                if total < n:
                    left = k + 1
                else:
                    right = k - 1

        # At least 11 is always possible:
        # n = 1 + (n-1)
        return str(n - 1)