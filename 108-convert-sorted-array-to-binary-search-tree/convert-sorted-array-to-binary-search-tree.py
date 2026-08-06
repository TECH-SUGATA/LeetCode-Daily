class Solution:
    def sortedArrayToBST(self, nums):
        if not nums:
            return None
        m = len(nums) // 2
        return TreeNode(
            nums[m],
            self.sortedArrayToBST(nums[:m]),
            self.sortedArrayToBST(nums[m+1:])
        )