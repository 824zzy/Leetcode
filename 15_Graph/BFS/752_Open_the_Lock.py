""" L1: BFS template+string operation
"""
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        Q = ['0000']
        seen = set(deadends)
        if "0000" in seen: return -1
        ans = 0
        while Q:
            for _ in range(len(Q)):
                cur = Q.pop(0)
                if cur == target: return ans
                for i in range(4):
                    for d in (-1, 1):
                        new = cur[:i] + str((int(cur[i])+d+10)%10)+cur[i+1:]
                        if new not in seen:
                            seen.add(new)
                            Q.append(new)
            ans += 1
        return -1