class Solution:
    def longestSubstring(self, s, k):
        if len(s) < k:
            return 0

        freq = {}

        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1

        for ch in freq:
            if freq[ch] < k:
                parts = s.split(ch)
                ans = 0

                for part in parts:
                    result = self.longestSubstring(part, k)
                    if result > ans:
                        ans = result

                return ans

        return len(s)