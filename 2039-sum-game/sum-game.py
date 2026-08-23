class Solution:
    def sumGame(self, num):
        n = len(num)
        mid = n // 2

        left = num[:mid]
        right = num[mid:]

        diff = sum(int(x) for x in left if x != '?') - sum(int(x) for x in right if x != '?')
        ql = left.count('?')
        qr = right.count('?')

        if (ql + qr) % 2:
            return True

        return diff != (qr - ql) * 9 // 2