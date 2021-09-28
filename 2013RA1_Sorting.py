""" L1
simulate insert sort and cound number of insert
"""
def Sorting(A):
    ans = 0
    A = [int(a) for a in A.split()]
    print(A)
    return ans
        
t = int(input())
for i in range(1, t+1):
    l = input()
    A = input()
    ans = Sorting(A)
    print("Case #{}: {}\n".format(i, ans), flush=True)