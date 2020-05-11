import unittest
class Solution:
    def findJudge(self, N: int, trust):
        if N == 1:
            return 1
        people = []
        trustables = []
        for i in range(len(trust)):
            people.append(trust[i][0])
            trustables.append(trust[i][1])
        for trustable in trustables:
            if trustable not in people and trustables.count(trustable) == N - 1:
                return trustable
        return -1
    # Town judge is one who has N-1 inlets and 0 outward edges
    def findJudgeMethod2(self, N: int, trust):
        inn = [0 for i in range(N+1)]
        out =[0 for i in range(N+1)]
        if len(trust)<N-1:
            return -1
        else:
            for i in trust:
                print(i[0],i[1])
                inn[i[0]]+=1
                out[i[1]]+=1
        no_outs=[i for i in range(len(out)) if out[i]==0]
        maximum_in = [i for i in range(len(inn)) if i>=N-1]
        print(no_outs)
        print(maximum_in)
s=Solution()
print(s.findJudge(4, [[1,3],[1,4],[2,3],[2,4],[4,3]]))
print(s.findJudgeMethod2(4, [[1,3],[1,4],[2,3],[2,4],[4,3]]))
