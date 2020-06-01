import math
class Solution:
    def kClosest(self, points, K):
        origin =[0,0]
        distance=[]
        for point in points:
            distance.append((math.dist(origin,point),point))  # tuple of dist , point
        print(distance)
        res =[]
        for dist,point in sorted(distance)[:K]:
            res.append(point)
        return res 



s = Solution()

print(s.kClosest([[3,3],[5,-1],[-2,4]],2))