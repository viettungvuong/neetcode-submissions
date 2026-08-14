class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []

        operators = ["+", "-", "*", "/"]

        n = len(tokens)

        for i in range(n):
            if tokens[i] in operators:
                second = int(st.pop(-1))
                first = int(st.pop(-1))
                if tokens[i] == "+":
                    first += second
                elif tokens[i] == "-":
                    first -= second
                elif tokens[i] == "*":
                    first *= second
                else:
                    first /= second

                st.append(first)
            else:
                st.append(tokens[i])
            print(st)

        return int(st.pop())