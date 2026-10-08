class Solution:
    def evaluate(self, expression: str) -> int:
        tokens = expression.replace("(", " ( ").replace(")", " ) ").split()

        def solve(i, env):
            token = tokens[i]

            # Number
            if token.lstrip("-").isdigit():
                return int(token), i + 1

            # Variable
            if token != "(":
                return env[token], i + 1

            # Skip "("
            i += 1
            op = tokens[i]
            i += 1

            # ADD
            if op == "add":
                a, i = solve(i, env)
                b, i = solve(i, env)
                return a + b, i + 1   # skip ')'

            # MULT
            if op == "mult":
                a, i = solve(i, env)
                b, i = solve(i, env)
                return a * b, i + 1   # skip ')'

            # LET
            new_env = env.copy()

            while True:
                # If current token is ')' -> invalid here
                if tokens[i] == ")":
                    return 0, i + 1

                # Check whether this is the final expression.
                # Example: (let x 2 x)
                # Here x is followed by ')'
                if i + 1 < len(tokens) and tokens[i + 1] == ")":
                    value, i = solve(i, new_env)
                    return value, i + 1

                # If it starts with '(' => this must be final expression
                # or an assigned expression.
                if tokens[i] == "(":
                    value, i = solve(i, new_env)
                    return value, i + 1

                # Variable assignment
                var = tokens[i]
                i += 1

                value, i = solve(i, new_env)
                new_env[var] = value

        return solve(0, {})[0]