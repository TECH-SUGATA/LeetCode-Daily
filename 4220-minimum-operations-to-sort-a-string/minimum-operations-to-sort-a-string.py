
class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)

        # Case 1: Already sorted
        if s == ''.join(sorted(s)):
            return 0

        # Case 2: Cannot sort a reversed string of length 2
        if n == 2:
            return -1

        mn = min(s)
        mx = max(s)

        # Case 3: One operation is enough
        if s[0] == mn or s[-1] == mx:
            return 1

        # Case 4: Minimum or maximum is in the middle
        for i in range(1, n - 1):
            if s[i] == mn or s[i] == mx:
                return 2

        # Case 5: Minimum is at the end and maximum is at the beginning
        return 3
