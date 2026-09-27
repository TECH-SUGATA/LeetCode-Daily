class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []

        for ch in s:
            if ch == '(':
                stack.append([])
            elif ch == ')':
                temp = stack.pop()
                temp.reverse()

                if stack:
                    stack[-1].extend(temp)
                else:
                    stack.append(temp)
            else:
                if not stack:
                    stack.append([])

                stack[-1].append(ch)

        return ''.join(stack[0])