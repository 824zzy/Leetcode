import heapq
from collections import defaultdict

def solution(A):
    """ {C(2), D(3)} ==> A(0) ==> B(1), F(5) ==> E(4)
    A: [[(100, 1), (100, 5)], 
        [(200, 4)], 
        [(200, 0)], 
        [(200, 0)], 
        [],
        [(200, 4)]
        ]
    """
    G = defaultdict(list)
    for i, F in enumerate(A):
        for j in F:
            G[i].append(j)
    H = [(200, 0)] # start from A(0)
    seen = set()
    ans = []
    while H:
        h1, i = heapq.heappop(H)
        seen.add(i)
        ans.append([i, h1])
        for h2, j in G[i]:
            if j not in seen:
                heapq.heappush(H, (h2, j))
    print(ans)
        
# N = int(input())

# ans = []
# for i in range(N):
#     _ = int(input())
#     A = list(map(int, input().split()))
#     ans.append(solution(A))

# for i in range(len(ans)): 
#     print(ans[i])
A = [[(100, 1), (100, 5)], [(200, 4)], [(200, 0)], [(200, 0)], [], [(200, 4)]]
solution(A)

"""
1
3
1 2 10
d
"""