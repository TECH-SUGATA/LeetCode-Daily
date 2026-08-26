class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        left = 0
        ones = 0
        ans = ""

        for right in range(len(s)):
            if s[right] == '1':
                ones += 1

            while ones == k:
                current = s[left:right + 1]

                if ans == "" or len(current) < len(ans):
                    ans = current
                elif len(current) == len(ans) and current < ans:
                    ans = current

                if s[left] == '1':
                    ones -= 1

                left += 1

        return ans