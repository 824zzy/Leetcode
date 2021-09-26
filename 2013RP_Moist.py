""" L1
simulate insert sort and cound number of insert
"""
def Moist(S):
    prev = S[0]
    ans = 0
    for i in range(1, len(S)):
        if S[i]<prev: ans += 1
        else: prev = S[i]
    return ans
        

t = int(input())

for i in range(1, t+1):
    card_num = int(input())
    S = [input() for _ in range(card_num)]
    ans = Moist(S)
    print("Case #{}: {}\n".format(i, ans), flush=True)