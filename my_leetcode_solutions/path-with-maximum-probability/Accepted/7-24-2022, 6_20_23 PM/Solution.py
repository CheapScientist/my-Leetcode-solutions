// https://leetcode.com/problems/path-with-maximum-probability

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        l = len(edges)
        graph = {i:[] for i in range(n)}
        for i in range(l):
            u, v = edges[i]
            w = succProb[i]
            graph[u].append([w, v]) # right now [weight, node]
            graph[v].append([w, u])
            
        maxH = [(-1, -start)]
        maxProb = 0
        visit = set()
        
        while maxH:
            curP, curN = heapq.heappop(maxH)
            curP *= -1
            curN *= -1
            if curN == end:
                maxProb = max(maxProb, curP)
                return maxProb
            if curN in visit:
                continue
            visit.add(curN)

            for neiW, nei in graph[curN]:
                if nei not in visit:
                    heapq.heappush(maxH, [-curP*neiW, -nei])
        
        return maxProb

        