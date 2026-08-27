class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        cnt = [0] * 26

        for ch in s:
            cnt[ord(ch) - ord('a')] += 1

        n = len(s)
        ans = []

        # Try to match target
        for i in range(n):
            x = ord(target[i]) - ord('a')

            if cnt[x] > 0:
                cnt[x] -= 1
                ans.append(target[i])
            else:
                # Cannot match target[i].
                # Find the smallest character greater than target[i].
                for c in range(x + 1, 26):
                    if cnt[c] > 0:
                        ans.append(chr(c + ord('a')))
                        cnt[c] -= 1

                        # Fill remaining positions with smallest chars.
                        for k in range(26):
                            ans.extend([chr(k + ord('a'))] * cnt[k])

                        return ''.join(ans)

                # Need to backtrack
                break

        # Backtrack to make the string strictly greater.
        for i in range(len(ans) - 1, -1, -1):
            cnt[ord(ans[i]) - ord('a')] += 1

            x = ord(target[i]) - ord('a')

            # Find smallest available character > target[i]
            for c in range(x + 1, 26):
                if cnt[c] > 0:
                    result = ans[:i]
                    result.append(chr(c + ord('a')))
                    cnt[c] -= 1

                    # Smallest possible suffix
                    for k in range(26):
                        result.extend([chr(k + ord('a'))] * cnt[k])

                    return ''.join(result)

        return ""