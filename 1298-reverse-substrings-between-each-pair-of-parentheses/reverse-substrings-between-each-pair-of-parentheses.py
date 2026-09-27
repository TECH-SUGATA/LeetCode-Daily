class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []

        for ch in s:
            if ch == '(':
                # Start a new substring
                stack.append([])
            
            elif ch == ')':
                # Reverse the current substring
                curr = stack.pop()[::-1]

                # If there is an outer substring, add to it
                if stack:
                    stack[-1].extend(curr)
                else:
                    stack.append(curr)
            
            else:
                # Normal character
                if stack:
                    stack[-1].append(ch)
                else:
                    stack.append([ch])

        return ''.join(stack[0])