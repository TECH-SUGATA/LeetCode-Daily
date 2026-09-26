class Solution:
    def findMaxLength(self, nums):
        balance = 0
        first = {0: -1}
        ans = 0

        for i, num in enumerate(nums):
            if num == 0:
                balance -= 1
            else:
                balance += 1

            if balance in first:
                ans = max(ans, i - first[balance])
            else:
                first[balance] = i

        return ans