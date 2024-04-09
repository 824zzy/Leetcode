""" https://leetcode.com/problems/analyze-user-website-visit-pattern/
disgust test cases and problem description
"""
from header import *


class Solution:
    def mostVisitedPattern(
            self,
            username: List[str],
            timestamp: List[int],
            website: List[str]) -> List[str]:
        cnt = defaultdict(list)
        for u, t, w in zip(username, timestamp, website):
            cnt[u].append((t, w))
        for k, v in cnt.items():
            cnt[k] = sorted(v)

        ans = Counter()
        for u, v in cnt.items():
            tmp = Counter()
            for i in range(len(v)):
                for j in range(i + 1, len(v)):
                    for k in range(j + 1, len(v)):
                        tmp[(v[i][1], v[j][1], v[k][1])] = 1
            ans += tmp
        return sorted(ans.items(), key=lambda x: (-x[1], x[0]))[0][0]


"""
["joe","joe","joe","james","james","james","james","mary","mary","mary"]
[1,2,3,4,5,6,7,8,9,10]
["home","about","career","home","cart","maps","home","home","about","career"]
["ua","ua","ua","ub","ub","ub"]
[1,2,3,4,5,6]
["a","b","a","a","b","c"]
["ua","ua","ua","ub","ub","ub"]
[1,2,3,4,5,6]
["a","b","c","a","b","a"]
["dowg","dowg","dowg"]
[158931262,562600350,148438945]
["y","loedo","y"]
["zkiikgv","zkiikgv","zkiikgv","zkiikgv"]
[436363475,710406388,386655081,797150921]
["wnaaxbfhxp","mryxsjc","oz","wlarkzzqht"]
["h","eiy","cq","h","cq","txldsscx","cq","txldsscx","h","cq","cq"]
[527896567,334462937,517687281,134127993,859112386,159548699,51100299,444082139,926837079,317455832,411747930]
["hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","yljmntrclw","hibympufi","yljmntrclw"]
"""
