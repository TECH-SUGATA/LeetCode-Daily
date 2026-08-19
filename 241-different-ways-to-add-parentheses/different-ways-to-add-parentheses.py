class Solution:
    def diffWaysToCompute(self, s):
        res = []

        for i, c in enumerate(s):
            if c in "+-*":
                for a in self.diffWaysToCompute(s[:i]):
                    for b in self.diffWaysToCompute(s[i+1:]):
                        res.append(a+b if c=="+" else a-b if c=="-" else a*b)

        return res or [int(s)]