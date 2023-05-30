from header import *

def solution(A):
    pass


A = input()
A = [int(x) for x in A.split()]
ans = solution(A)
print(ans)


"""
001
010
011
100
011

sum(A') = 1+2+3+4+5 = 15
sum(A) = 1+2+3+4+3 = 13
# find duplicate 3 and missing 5=3+(15-13)

"""