class Solution(object):
    def repeatedStringMatch(self, a, b):
        s = ""
        count = 0

        while len(s) < len(b):
            s += a
            count += 1

        if b in s:
            return count

        s += a

        if b in s:
            return count + 1

        return -1