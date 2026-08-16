class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)

        q = [0]
        farthest = 0

        while q:
            current_pos = q.pop(0)
            start = max(current_pos+minJump,farthest+1)
            end = min(current_pos+maxJump,n-1)
            if current_pos>=n-1:
                return True
            for i in range(start,end+1):
                if i>=n:
                    continue
                if s[i]=="1":
                    continue
                if i==n-1:
                    return True
                q.append(i)

            farthest = max(farthest, current_pos+maxJump)
        
        return False