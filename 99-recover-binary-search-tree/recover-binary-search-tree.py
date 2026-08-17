class Solution:
    def recoverTree(self, root):
        stack = []
        current = root
        prev = None
        first = None
        second = None

        while stack or current:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()

            if prev and prev.val > current.val:
                if first is None:
                    first = prev
                second = current

            prev = current
            current = current.right

        first.val, second.val = second.val, first.val