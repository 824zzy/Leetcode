""" L2: TODO:
"""
class DSU:
    def __init__(self, n):
        self.p = [i for i in range(n)]

    def find(self, u):
        # find the root/cluster-id of u
        if self.p[u]!=u:
            self.p[u] = self.find(self.p[u])
        return self.p[u]

    def union(self, x, y):
        # merge cluter x and cluster y
        self.p[self.find(x)] = self.find(y)
        
        
def split_group(P):
    names = set()
    for p in P:
        names.add(p[0])
        names.add(p[1])
    D = {n: i for i, n in enumerate(list(names))}
    dsu = DSU(len(names))
    for p in P:
        dsu.union(D[p[0]], D[p[1]])
    group_num = len(set([dsu.find(i) for i in range(len(dsu.p))]))
    print("dada", group_num)
    return 0
    # group_num = len(set([dsu.find(i) for i in range(len(dsu.p))]))
    # return "Yes"


t = int(input())
for i in range(1, t+1):
    n = int(input())
    P = []
    for _ in range(n):
        P.append(input().split())
    ans = split_group(P)
    print("Case #{}: {}".format(i, ans))
