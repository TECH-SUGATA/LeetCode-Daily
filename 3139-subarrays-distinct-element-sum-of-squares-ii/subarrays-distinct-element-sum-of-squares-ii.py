class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        total = [0] * (4 * n)
        squares = [0] * (4 * n)
        lazy = [0] * (4 * n)

        def apply(node, length, val):
            squares[node] = (
                squares[node] + 2 * val * total[node]
                + length * val * val
            ) % MOD
            total[node] = (total[node] + length * val) % MOD
            lazy[node] += val

        def push(node, left, right):
            if lazy[node] and left != right:
                mid = (left + right) // 2
                apply(node * 2, mid - left + 1, lazy[node])
                apply(node * 2 + 1, right - mid, lazy[node])
                lazy[node] = 0

        def update(node, left, right, ql, qr):
            if ql <= left and right <= qr:
                apply(node, right - left + 1, 1)
                return

            push(node, left, right)
            mid = (left + right) // 2

            if ql <= mid:
                update(node * 2, left, mid, ql, qr)
            if qr > mid:
                update(node * 2 + 1, mid + 1, right, ql, qr)

            total[node] = (
                total[node * 2] + total[node * 2 + 1]
            ) % MOD
            squares[node] = (
                squares[node * 2] + squares[node * 2 + 1]
            ) % MOD

        last = {}
        ans = 0

        for i, x in enumerate(nums):
            left = last.get(x, -1) + 1
            update(1, 0, n - 1, left, i)
            last[x] = i
            ans = (ans + squares[1]) % MOD

        return ans