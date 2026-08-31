class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        q = []
        in_order = [0]*numCourses
        graph = {}
        for prereq in prerequisites:
            toc, fromc = prereq
            if graph.get(fromc) is None:
                graph[fromc]=[]
            graph[fromc].append(toc)
            in_order[toc]+=1

        for i in range(numCourses):
            if in_order[i]==0:
                q.append(i)

        visited=set()
        while q:
            currentCourse = q.pop(0)
            visited.add(currentCourse)
            for neighbor in graph.get(currentCourse,[]):
                in_order[neighbor]-=1
                if neighbor not in visited and in_order[neighbor]==0:
                    print(f"Added {neighbor} from {currentCourse}")
                    q.append(neighbor)
        return len(visited)==numCourses