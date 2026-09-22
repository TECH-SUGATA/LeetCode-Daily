from typing import List


class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)

        # tree[node] = [whole_product_mod_k, count_of_prefixes_for_each_remainder]
        tree = [[0, [0] * k] for _ in range(4 * n)]

        def merge(left, right):
            left_prod, left_cnt = left
            right_prod, right_cnt = right

            # Product of entire combined segment
            prod = (left_prod * right_prod) % k

            # Prefixes completely inside left
            cnt = left_cnt[:]

            # Prefixes that use all of left + a prefix of right
            for r in range(k):
                cnt[(left_prod * r) % k] += right_cnt[r]

            return prod, cnt

        def build(node, l, r):
            if l == r:
                rem = nums[l] % k

                tree[node][0] = rem
                tree[node][1][rem] = 1
                return

            mid = (l + r) // 2

            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)

            left = tree[node * 2]
            right = tree[node * 2 + 1]

            prod, cnt = merge(left, right)

            tree[node][0] = prod
            tree[node][1] = cnt

        def update(node, l, r, idx, value):
            if l == r:
                rem = value % k

                tree[node][0] = rem
                tree[node][1] = [0] * k
                tree[node][1][rem] = 1
                return

            mid = (l + r) // 2

            if idx <= mid:
                update(node * 2, l, mid, idx, value)
            else:
                update(node * 2 + 1, mid + 1, r, idx, value)

            left = tree[node * 2]
            right = tree[node * 2 + 1]

            prod, cnt = merge(left, right)

            tree[node][0] = prod
            tree[node][1] = cnt

        def query(node, l, r, ql, qr):
            # Complete segment
            if ql <= l and r <= qr:
                return tree[node][0], tree[node][1][:]

            mid = (l + r) // 2

            if qr <= mid:
                return query(node * 2, l, mid, ql, qr)

            if ql > mid:
                return query(node * 2 + 1, mid + 1, r, ql, qr)

            left = query(node * 2, l, mid, ql, qr)
            right = query(node * 2 + 1, mid + 1, r, ql, qr)

            return merge(left, right)

        build(1, 0, n - 1)

        ans = []

        for index, value, start, x in queries:
            # Persistent update
            update(1, 0, n - 1, index, value)

            # We need the range [start, n-1].
            # cnt[x] = number of valid remaining arrays
            _, cnt = query(1, 0, n - 1, start, n - 1)

            ans.append(cnt[x])

        return ans