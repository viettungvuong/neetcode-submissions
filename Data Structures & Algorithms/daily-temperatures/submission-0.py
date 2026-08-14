class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)

        st = [] # store days that have not found answers

        for i in range(len(temperatures)):
            # find answers for all unresolved days
            while len(st) > 0 and temperatures[i] > temperatures[st[-1]]:
                prev = st.pop()
                res[prev] = i - prev

            st.append(i)
        
        return res