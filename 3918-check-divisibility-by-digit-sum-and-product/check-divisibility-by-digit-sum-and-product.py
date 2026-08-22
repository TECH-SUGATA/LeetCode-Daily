class Solution:
    def checkDivisibility(self, n):
        digits = [int(x) for x in str(n)]
        s = sum(digits)
        p = 1

        for x in digits:
            p *= x

        return n % (s + p) == 0