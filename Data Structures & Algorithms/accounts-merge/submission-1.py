class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = {}

        for account in accounts:
            prev = None
            for i in range(1, len(account)):
                if graph.get((account[0],account[i])) is None:
                    graph[(account[0],account[i])] = set()

                if prev is not None:
                    if graph.get((account[0],prev)) is None:
                        graph[(account[0],prev)] = set()
                    graph[(account[0],prev)].add((account[0],account[i]))
                    graph[(account[0],account[i])].add((account[0],prev))

                prev = account[i]

        res = []
        visited = set()

        for node in graph:
            if node is None:
                continue

            name, email = node

            if email in visited:
                continue

            current=[name]

            q=[email]
            visited.add(email)
            while q:
                current_email=q.pop(0)
                current.append(current_email)
                for _, next_email in graph[(name,current_email)]:
                    if next_email not in visited:
                        q.append(next_email)
                        visited.add(next_email)
            
            res.append(current)
        return res