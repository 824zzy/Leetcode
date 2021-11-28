class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        cnt = Counter(s[:len(p)])
        t = Counter(p)
        ans = []
        for i in range(len(s)-len(p)):
            if cnt==t: ans.append(i)
            cnt[s[i]] -= 1
            if not cnt[s[i]]: del cnt[s[i]]
            cnt[s[i+len(p)]] += 1
        if cnt==t: ans.append(i+1)
        return ans