
class Solution:
    def postorderTraversal(self, root):
        result = []

        def dfs(node):
            if not node:
                return

            dfs(node.left)
            dfs(node.right)
            result.append(node.val)

        dfs(root)
        return result
