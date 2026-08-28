class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        from collections import Counter

        n = len(s)
        cnt = Counter(s)

        # A palindrome can have at most one character with odd frequency.
        odd = [ch for ch in cnt if cnt[ch] % 2 == 1]
        if len(odd) > 1:
            return ""

        half = []
        for ch in sorted(cnt):
            half.extend([ch] * (cnt[ch] // 2))

        mid = odd[0] if odd else ""

        # Build the lexicographically smallest possible palindrome
        # strictly greater than target.
        m = len(half)

        # We only need to compare the first half.
        target_half = target[:m]

        def make_pal(p):
            return p + mid + p[::-1]

        # Try all possibilities for the first half using backtracking.
        # At each position, keep the prefix as small as possible.
        used = [0] * 26
        chars = sorted(cnt.keys())

        half_count = Counter(half)
        result = []

        def dfs(pos, relation):
            # relation:
            # 0 -> prefix equal to target
            # 1 -> already greater

            if pos == m:
                p = ''.join(result)
                cand = make_pal(p)
                return cand if cand > target else None

            if relation == 1:
                # Once greater, use the smallest remaining characters.
                rem = []
                for ch in chars:
                    rem.extend([ch] * (half_count[ch] - used[ord(ch) - 97]))
                p = ''.join(result) + ''.join(rem)
                return make_pal(p)

            # Must choose a character >= target_half[pos].
            start = target_half[pos]

            for ch in chars:
                if used[ord(ch) - 97] >= half_count[ch]:
                    continue
                if ch < start:
                    continue

                idx = ord(ch) - 97
                used[idx] += 1
                result.append(ch)

                new_relation = 1 if ch > start else 0
                ans = dfs(pos + 1, new_relation)

                if ans is not None:
                    return ans

                result.pop()
                used[idx] -= 1

            return None

        ans = dfs(0, 0)

        return ans if ans is not None else ""