""" https://leetcode.com/problems/find-closest-node-to-given-two-nodes/
1. run DFS independently for node 1 and 2, memoising the distance to each node we reach.
2. we check each node and return the one with minimum max distance.
"""
class Solution:
    def closestMeetingNode(self, E: List[int], node1: int, node2: int) -> int:
        seen1 = [-1]*len(E)
        seen2 = [-1]*len(E)
        def dfs(node, dist, seen):
            if node!=-1 and seen[node]==-1:
                seen[node] = dist
                dfs(E[node], dist+1, seen)
                
        dfs(node1, 0, seen1)
        dfs(node2, 0, seen2)
        
        ans = -1
        mn = inf
        for i, (x, y) in enumerate(zip(seen1, seen2)):
            if x!=-1 and y!=-1 and max(x, y)<mn:
                ans = i
                mn = max(x, y)
        return ans