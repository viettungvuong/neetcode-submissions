class Solution:
    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0

        dist = [float("inf")] * n
        dist[0] = 0

        pq = [(0, 0)]

        while pq:
            cur_dist, u = heapq.heappop(pq)

            if u == n - 1:
                return cur_dist

            if cur_dist > dist[u]:
                continue

            max_reachable = min(n - 1, u + nums[u])
            for v in range(u + 1, max_reachable + 1):
                if dist[u] + 1 < dist[v]:
                    dist[v] = dist[u] + 1
                    heapq.heappush(pq, (dist[v], v))

        return dist[n - 1]
