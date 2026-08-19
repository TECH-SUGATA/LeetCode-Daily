class Solution:
    def maxNumberOfFamilies(self, n, reservedSeats):
        rows = {}

        for r, c in reservedSeats:
            rows[r] = rows.get(r, 0) | (1 << c)

        ans = 2 * (n - len(rows))

        for x in rows.values():
            left = (x & 60) == 0
            middle = (x & 240) == 0
            right = (x & 960) == 0

            if left:
                ans += 1
            if right:
                ans += 1

            if not left and not right and middle:
                ans += 1

        return ans