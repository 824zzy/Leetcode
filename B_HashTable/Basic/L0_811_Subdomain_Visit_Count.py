""" https://leetcode.com/problems/subdomain-visit-count/
string formatting + hash table
"""


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        cnt = Counter()
        for cpdomain in cpdomains:
            times, domain = cpdomain.split()
            times = int(times)
            d = domain.split(".")
            if len(d) == 3:
                cnt[".".join(d)] += times
                cnt[".".join([d[1], d[2]])] += times
                cnt[d[2]] += times
            elif len(d) == 2:
                cnt[".".join(d)] += times
                cnt[d[1]] += times

        return [" ".join([str(v), k]) for k, v in cnt.items()]
