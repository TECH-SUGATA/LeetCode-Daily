class Solution:
    def scoreOfParentheses(self, s):
        stack = [0]

        for ch in s:
            if ch == '(':
                stack.append(0)
            else:
                inner = stack.pop()

                if inner == 0:
                    score = 1
                else:
                    score = 2 * inner

                stack[-1] += score

        return stack[0]