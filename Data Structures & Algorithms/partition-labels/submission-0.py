class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_appear = {}
        for i in range(len(s)):
            c = s[i]
            if last_appear.get(c) is None:
                last_appear[c] = -1
            last_appear[c] = i
        res = []
        can_end = 0
        current = 0
        for i in range(len(s)):
            can_end = max(can_end, last_appear[s[i]])
            current += 1

            if i == can_end:
                res.append(current)
                current = 0
        return res

