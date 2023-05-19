""" https://leetcode.com/problems/reconstruct-itinerary/
Hierholzer's Algorithm
"""
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        G = defaultdict(list)
        degree = defaultdict(int) # out-degree
        for i, j in tickets:
            G[i].append(j)
            degree[i] += 1
            degree[j] -= 1
        
        for i in G: G[i] = sorted(G[i], reverse=True) # make sure lexical order
        
        ans = []
        stk = ["JFK"]
        while stk:
            while G[stk[-1]]:
                stk.append(G[stk[-1]].pop())
            ans.append(stk.pop())
        return ans[::-1]
                