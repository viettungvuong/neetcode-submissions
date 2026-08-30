class Solution:
    # def heuristic(self, str1, str2):
    #     forward_h = sum(abs(ord(c1) - ord(c2)) for c1, c2 in zip(str1, str2))
    #     backward_h = 
    #     return sum(abs(ord(c1) - ord(c2)) for c1, c2 in zip(str1, str2))
    def openLock(self, deadends: List[str], target: str) -> int:
        frontier = []
        start = "0000"
        heapq.heappush(frontier, (0, start))
        visited = set()
        visited.add(start)

        prev_digit = ["9", "0", "1", "2", "3", "4", "5", "6", "7", "8"]
        next_digit = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

        while frontier:
            steps, current = heapq.heappop(frontier)

            if current in deadends:
                continue

            if current==target:
                return steps

            for i in range(4):
                current_char = int(current[i])
                
                # Get the neighbor codes using string slicing
                move_prev = current[:i] + prev_digit[current_char] + current[i+1:]
                if move_prev not in visited:
                    visited.add(move_prev)
                    heapq.heappush(frontier, (steps+1, move_prev))
                next_prev = current[:i] + next_digit[current_char] + current[i+1:]
                if next_prev not in visited:
                    visited.add(next_prev)
                    heapq.heappush(frontier, (steps+1, next_prev))

        return -1