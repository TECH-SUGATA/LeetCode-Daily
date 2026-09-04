from collections import deque

class Solution:
    def minMutation(self, startGene, endGene, bank):
        bank = set(bank)

        if endGene not in bank:
            return -1

        q = deque([(startGene, 0)])
        genes = "ACGT"

        while q:
            cur, steps = q.popleft()

            if cur == endGene:
                return steps

            for i in range(8):
                for ch in genes:
                    new = cur[:i] + ch + cur[i+1:]

                    if new in bank:
                        bank.remove(new)
                        q.append((new, steps + 1))

        return -1