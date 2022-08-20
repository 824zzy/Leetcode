""" https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/
"""
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        cnt = defaultdict(list)
        for i, x in enumerate(groupSizes):
            cnt[x].append(i)
        
        ans = []
        for k, v in cnt.items():
            for i in range(0, len(v), k):
                ans.append(v[i:i+k])
        return ans