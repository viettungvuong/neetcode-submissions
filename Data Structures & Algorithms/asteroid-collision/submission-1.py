class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []
        for a in asteroids:
            if len(st) == 0:
                st.append(a)
                continue
            
            while True:
                if len(st) > 0 and st[-1] > 0 and a < 0:
                    if abs(st[-1]) < abs(a):
                        st.pop(-1)
                    elif abs(st[-1]) == abs(a):
                        st.pop(-1)
                        break
                    else:
                        break
                else:
                    st.append(a)
                    break
        
        return st