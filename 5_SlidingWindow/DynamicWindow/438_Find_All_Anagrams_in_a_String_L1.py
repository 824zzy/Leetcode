""" https://leetcode.com/problems/find-all-anagrams-in-a-string/
1. use a dynamic sliding window and a Counter to record p's frequency
2. when Counter values are all 0, we find an answer
3. if A[j] not in p, then refresh the window and reset i
"""
class Solution:
    def findAnagrams(self, A: str, p: str) -> List[int]:
        i = 0
        cnt = Counter(p)
        ans = []
        
        for j in range(len(A)):
            if A[j] in cnt:
                cnt[A[j]] -= 1
                while cnt[A[j]]<0:
                    cnt[A[i]] += 1
                    i += 1
                if sum(cnt.values())==0: ans.append(i)
            else: 
                i = j + 1
                cnt = Counter(p)
        return ans