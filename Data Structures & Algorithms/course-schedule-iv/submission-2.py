class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        prereq = {}
        for prerequisite in prerequisites:
            fromCourse, toCourse = prerequisite
            if prereq.get(toCourse) is None:
                prereq[toCourse]=[]
            prereq[toCourse].append(fromCourse)
        memo = [[0] * numCourses for _ in range(numCourses)]
        def dfs(current, target):
            if current==target:
                return True
            if memo[current][target] != 0:
                return memo[current][target] == 1
            
            for preCourse in prereq.get(current,[]):
                res = False
                if dfs(preCourse, target)==True:
                    memo[current][target] = 1
                    return True
            memo[current][target] = -1
            return False

        res = [False] * len(queries)
        for i in range(len(queries)):
            queryFrom,queryTo=queries[i]
            res[i]=dfs(queryTo,queryFrom)
        return res


