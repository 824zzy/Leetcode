class Solution:
    def minJumps(self, arr: List[int]) -> int:
        mp = collections.defaultdict(list)
        queue = [0]
        seen = {0}
        ans = 0
        for i in range(len(arr)): mp[arr[i]].append(i)
        
        while queue:
            newq = []
            for _ in range(len(queue)):
                n = queue.pop(0)
                if n==len(arr)-1: return ans
                rng = [n-1, n+1]
                if arr[n] in mp:
                    rng += mp[arr[n]]
                    mp.pop(arr[n])
                for nn in rng: 
                    if 0 <= nn < len(arr) and nn not in seen: 
                        queue.append(nn)
                        seen.add(nn)    
            ans += 1