class Solution:
    def decodeString(self, s: str) -> str:
        res = ""

        st = []

        in_number = 0

        for c in s:
            if c != "]":
                st.append(c)
            else:
                current = ""
                while st and st[-1] != "[":
                    current_char = st.pop(-1)
                    current = current_char + current
                st.pop(-1) # remove "["
                quantity = ""
                while st and st[-1].isnumeric():
                    current_digit = st.pop(-1)
                    quantity = current_digit + quantity
                quantity = int(quantity)
                st.append(quantity*current)
        return "".join(st)