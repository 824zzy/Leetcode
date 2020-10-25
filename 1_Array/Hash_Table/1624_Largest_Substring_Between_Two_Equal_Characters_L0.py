class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        pos = collections.defaultdict(list)
        for i, c in enumerate(s):
            if c not in pos:
                pos[c].append(i)
            else:
                if len(pos[c])==1:
                    pos[c].append(i)
                else:
                    pos[c][1] = i
        ans = [v[1]-v[0]-1 for k, v in pos.items() if len(v)>1]
        return max(ans) if ans else -1
    
# Better one pass solution
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        index_adj_list = defaultdict(int)
        ans_max = -1
        for i in range(len(s)):
            if s[i] in index_adj_list:
                ans_max = max(ans_max, i - index_adj_list[s[i]] - 1)
            else:
                index_adj_list[s[i]] = i
        return ans_max