class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        best = [0] * 26
        length = 0

        for i in range(len(s)):
            # Check whether current character continues
            # the wraparound sequence
            if i > 0 and (
                ord(s[i]) - ord(s[i - 1]) == 1
                or (s[i - 1] == 'z' and s[i] == 'a')
            ):
                length += 1
            else:
                length = 1

            index = ord(s[i]) - ord('a')

            # Maximum valid substring ending at this character
            best[index] = max(best[index], length)

        return sum(best)