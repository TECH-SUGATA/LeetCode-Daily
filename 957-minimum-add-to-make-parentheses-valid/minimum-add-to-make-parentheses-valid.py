class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_count = 0
        additions = 0

        for ch in s:
            if ch == '(':
                open_count += 1
            else:
                if open_count > 0:
                    open_count -= 1
                else:
                    additions += 1

        return additions + open_count