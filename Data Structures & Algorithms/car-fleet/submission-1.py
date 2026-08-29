class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        n = len(position)

        for i in range(n):
            cars.append((position[i], speed[i]))
        
        cars = sorted(cars, key=lambda c: c[0], reverse=True)

        st = []
        for c in cars:
            if st:
                if (target-c[0])/c[1] <= (target-st[-1][0])/st[-1][1]: # ahead car and current car never meet
                    continue

            st.append(c)
        
        return len(st)

