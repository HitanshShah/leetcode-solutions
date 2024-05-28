class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq = {}
        for pre in prerequisites:
            if pre[0] in prereq:
                prereq[pre[0]].append(pre[1])
            else:
                prereq[pre[0]] = [pre[1]]
        # print(prereq)
        visited = set()
        for c in prereq:
            if self.hasCycle(prereq, c, c, visited):
                return False
        return True

    def hasCycle(self, prereq, c1, c2, visited):
        visited.add(c2)
        req = prereq[c2]
        for r in req:
            if r in prereq:
                if c1 in prereq[r]:
                    return True
                elif not r in visited:
                    return self.hasCycle(prereq, c1, r, visited)
        return False