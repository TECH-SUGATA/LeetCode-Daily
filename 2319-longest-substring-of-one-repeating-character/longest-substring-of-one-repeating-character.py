class Solution:
    def longestRepeating(self, s, queryCharacters, queryIndices):
        n = len(s)
        tree = [None] * (4 * n)

        def merge(a, b):
            l1, r1, p1, s1, m1, len1 = a
            l2, r2, p2, s2, m2, len2 = b

            p = p1
            su = s2
            best = max(m1, m2)

            if r1 == l2:
                best = max(best, s1 + p2)

                if p1 == len1:
                    p = len1 + p2

                if s2 == len2:
                    su = s1 + len2

            return (l1, r2, p, su, best, len1 + len2)

        def build(node, left, right):
            if left == right:
                tree[node] = (s[left], s[left], 1, 1, 1, 1)
                return

            mid = (left + right) // 2
            build(node * 2, left, mid)
            build(node * 2 + 1, mid + 1, right)
            tree[node] = merge(tree[node * 2], tree[node * 2 + 1])

        def update(node, left, right, idx, ch):
            if left == right:
                tree[node] = (ch, ch, 1, 1, 1, 1)
                return

            mid = (left + right) // 2

            if idx <= mid:
                update(node * 2, left, mid, idx, ch)
            else:
                update(node * 2 + 1, mid + 1, right, idx, ch)

            tree[node] = merge(tree[node * 2], tree[node * 2 + 1])

        build(1, 0, n - 1)

        ans = []

        for ch, idx in zip(queryCharacters, queryIndices):
            update(1, 0, n - 1, idx, ch)
            ans.append(tree[1][4])

        return ans