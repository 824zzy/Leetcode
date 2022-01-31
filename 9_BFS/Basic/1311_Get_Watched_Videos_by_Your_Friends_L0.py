""" https://leetcode.com/problems/get-watched-videos-by-your-friends/
bfs + hash table
not hard and be careful
"""
class Solution:
    def watchedVideosByFriends(self, V: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        G = defaultdict(dict)
        for i, v in enumerate(friends):
            for j in v:
                G[i][j] = V[j]
        
        Q = [[id, 0]]
        seen = set()
        seen.add(id)
        ans = Counter()
        while Q:
            i, l = Q.pop(0)
            l += 1
            if l>level: continue
            for j in G[i]:
                if j not in seen:
                    
                    if l==level:
                        for x in G[i][j]: ans[x] += 1
                    seen.add(j)
                    Q.append([j, l])        
        
        return [k for k, v in sorted(ans.items(), key=lambda x: (x[1], x[0]))]