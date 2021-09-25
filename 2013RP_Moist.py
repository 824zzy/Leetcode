def Moist(S):
    ordered_S = sorted(S)
    ans = 0
    for i in range(len(S)):
        if S[i]>ordered_S[i]:
            print(S[i], ordered_S[i])
            ans += 1
    return ans
        

t = int(input())

for i in range(1, t+1):
    card_num = int(input())
    S = [input() for _ in range(card_num)]
    ans = Moist(S)
    print("Case #{}: {}\n".format(i, ans), flush=True)