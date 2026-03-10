""" https://foobar.withgoogle.com/dodge-the-laser
It is an interesting math problem!
According to Beatty sequence theory:
1/r + 1/s = 1, where r = sqrt(2)
==> s = 2+sqrt(2)

Reference:
1. [Beatty sequence](https://en.wikipedia.org/wiki/Beatty_sequence)
2. [Rayleigh_theorem](https://en.wikipedia.org/wiki/Beatty_sequence#Rayleigh_theorem)
3. [Dodge The Lasers-Fantastic Question From Google hiring challenge](https://towardsdatascience.com/dodge-the-lasers-fantastic-question-from-googles-hiring-challenge-72363d95fec)
"""
from decimal import Decimal, getcontext


def solution(s):
    n = Decimal(s)
    getcontext().prec = 132
    r, s = Decimal(2).sqrt(), Decimal(2 + Decimal(2).sqrt())

    def dp(n):
        if n == 0:
            return 0
        B_r = int(r * n)
        B_rs = int(Decimal(B_r) / s)
        return (B_r * (B_r + 1)) / 2 - dp(B_rs) - B_rs * (B_rs + 1)

    return str(int(dp(n)))


ans = solution("5")
print(ans)
