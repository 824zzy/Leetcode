""" L1
Use Decimal to adjust precision to avoid asin overflow
"""
import math
from decimal import Decimal
def get_theta(V, D):
    return round(math.asin(D*Decimal(9.8)/V**2)/math.pi*180/2, 8)
        

t = int(input())

for i in range(1, t+1):
    V, D = input().split()
    ans = get_theta(Decimal(V), Decimal(D))
    print("Case #{}: {:.7f}".format(i, ans))