""" Advanced usage of hash map
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        sorted_s = {}
        
        for s in strs:
            x = ''.join(sorted(s))
            if x in sorted_s:
                sorted_s[x].append(s)
            else:
                sorted_s[x] = [s]
        
        for k, v in sorted_s.items():
            ans.append(v)
        
        return ans