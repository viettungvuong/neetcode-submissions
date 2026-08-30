from typing import List


class Solution:

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = list(range(len(edges) + 1))

        def find(node: int) -> int:
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]

        def union(n1: int, n2: int) -> bool:
            root1, root2 = find(n1), find(n2)
            if root1 == root2:
                return False  # Already connected -> cycle detected
            parent[root1] = root2
            return True

        for u, v in edges:
            if not union(u, v):
                return [u, v]

        return []
