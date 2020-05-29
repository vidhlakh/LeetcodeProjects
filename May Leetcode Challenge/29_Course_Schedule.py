from collections import defaultdict
class Solution:
    def canFinish(self, numCourses , prerequisites ):
        indegree =defaultdict(set)
        outdegree = defaultdict(set) 
        for x, y in prerequisites:
            outdegree[y].add(x)
            indegree[x].add(y)
        connection_removed =0 
        indegree_zero =[]
        for i in range (numCourses):
            if not indegree[i]:
                indegree_zero.append(i)
                connection_removed +=1
        while indegree_zero:
            node = indegree_zero.pop()
            for x in outdegree[node]:
                indegree[x].remove(node)
                if not indegree[x]:
                    indegree_zero.append(x)
                    connection_removed += 1
        return connection_removed == numCourses
s = Solution()
print(s.canFinish(2, [[1,0]]))