# sort string by length and lexicographical order and compare one by one.
class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        dic = sorted(d, key=lambda x: (-len(x), x))
        for d in dic:
            cnt = 0
            for c in s:
                if c==d[cnt]: 
                    cnt += 1
                    if cnt==len(d): return d
        return ''