class Solution:
    def merge(self, intervals):
        intervals.sort()
        ans = []

        for start, end in intervals:
            if not ans or start > ans[-1][1]:
                ans.append([start, end])
            else:
                ans[-1][1] = max(ans[-1][1], end)

        return ans