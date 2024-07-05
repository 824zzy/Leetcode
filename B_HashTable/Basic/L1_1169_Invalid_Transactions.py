""" https://leetcode.com/problems/invalid-transactions/
complicated to implement...
1. linear scan all the transactions to find the first type invalid transactions and build a hash table
2. go over hash table to find second type invalid transactions
"""
from header import *


class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        T = [t.split(",") for t in transactions]
        cnt = defaultdict(SortedList)
        ans = []
        for n, t, p, c in T:
            if int(p) > 1000:
                ans.append(",".join([n, t, p, c]))
            cnt[n].add([t, c, p])

        for n, v in cnt.items():
            for i in range(len(v)):
                for j in range(len(v)):
                    if (
                        int(v[i][2]) <= 1000
                        and abs(int(v[i][0]) - int(v[j][0])) <= 60
                        and v[i][1] != v[j][1]
                    ):
                        ans.append(",".join([n, v[i][0], v[i][2], v[i][1]]))
                        break
        return ans
