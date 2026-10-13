class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        result = []

        def backtrack(index, parts):
            if len(parts) == 4:
                if index == len(s):
                    result.append(".".join(parts))
                return

            for length in range(1, 4):
                segment = s[index:index + length]

                if index + length > len(s):
                    break

                if len(segment) > 1 and segment[0] == '0':
                    continue

                if int(segment) > 255:
                    continue

                backtrack(index + length, parts + [segment])

        if 4 <= len(s) <= 12:
            backtrack(0, [])

        return result