""" https://leetcode.com/problems/display-table-of-food-orders-in-a-restaurant/
use dict of Counters and ordered food name list to build table
"""
class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        sd = defaultdict(Counter)
        foods = set()
        for _, t, f in orders:
            t = int(t)
            sd[t][f] += 1
            foods.add(f)
        
        foods = sorted(foods)
        ans = [["Table"]+foods]
        for k, cnt in sorted(sd.items()):
            row = [str(k)]
            for f in foods:
                row.append(str(cnt[f]))
            ans.append(row)
        return ans