class Solution:
    def braceExpansionII(self, expression: str):
        n = len(expression)

        def parse(i):
            result = set()
            current = {""}

            while i < n:
                # End of current brace
                if expression[i] == '}':
                    result |= current
                    return result, i + 1

                # Union: ","
                if expression[i] == ',':
                    result |= current
                    current = {""}
                    i += 1
                    continue

                # Get the next part
                if expression[i].isalpha():
                    part = {expression[i]}
                    i += 1

                elif expression[i] == '{':
                    part, i = parse(i + 1)

                # Concatenation
                current = {
                    a + b
                    for a in current
                    for b in part
                }

            result |= current
            return result, i

        ans, _ = parse(0)
        return sorted(ans)