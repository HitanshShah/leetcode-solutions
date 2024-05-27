class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        n = len(points)
        for (x, y) in points:
            if(len(heap) == k):
                heapq.heappushpop(heap,(-self.distance(x, y), x, y))
            else:
                heapq.heappush(heap,(-self.distance(x, y), x, y))
        return [[x,y] for (dist, x, y) in heap]

    def distance(self,i,j):
        return i**2 + j**2