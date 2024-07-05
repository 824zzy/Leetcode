""" L0: https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435a5b/000000000077a882
basic stack usage
"""


def increasing_substring(L, S):
    stk = []
    ans = []
    for i in range(len(S)):
        if stk and stk[-1] >= S[i]:
            stk = []
        stk.append(S[i])
        ans.append(len(stk))
    return ans


N = int(input())
for i in range(N):
    L = int(input())
    S = input()
    ans = increasing_substring(L, S)
    ans = " ".join([str(a) for a in ans])
    print("Case #{}: {}".format(i + 1, ans))
