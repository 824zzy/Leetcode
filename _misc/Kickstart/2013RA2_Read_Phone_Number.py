""" L1
simulate insert sort and cound number of insert
"""
from itertools import groupby
M = {
    '0': 'zero',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine',
    1: '',
    2: 'double',
    3: 'triple',
    4: 'quadruple',
    5: 'quintuple',
    6: 'sextuple',
    7: 'septuple',
    8: 'octuple',
    9: 'nonuple',
    10: 'decuple',
}
def ReadPhoneNumber(P, F):
    ans = []
    lengths = F.split('-')
    pref = 0
    pref_L = []
    for l in lengths:
        pref += int(l)
        pref_L.append(pref)
    pref_L = [0] + pref_L
    for i in range(len(pref_L)-1):
        p = [[k, len(list(v))] for k, v in groupby(P[pref_L[i]:pref_L[i+1]])]
        s = []
        for k, l in p:
            if l>10: s.append(" ".join(l*[M[k]]))
            elif l==1: s.append(M[k])
            else: s.append(M[l]+" "+M[k])
        ans.append(" ".join(s))
    return ' '.join(ans)
        
t = int(input())
for i in range(1, t+1):
    P, F = input().split()
    ans = ReadPhoneNumber(P, F)
    print("Case #{}: {}\n".format(i, ans), flush=True)