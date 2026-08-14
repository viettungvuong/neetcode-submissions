class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        print(people)

        n = len(people)

        l = 0
        r = n - 1

        res = 0

        while l < r:
            while l < r and people[l] + people[r] <= limit:
                print(f"{l} - {r}")

                l += 1
                r -= 1

                res += 1

            while l < r and people[l] + people[r] > limit:
                r -= 1
                res += 1
        
        if l == r:
            res += 1
        
        return res

            