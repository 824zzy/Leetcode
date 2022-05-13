""" https://foobar.withgoogle.com/free_the_bunny_workers
compute the limiting matrices of absorbing markov chain

"""
from __future__  import division
from itertools import combinations

def solution(b, r):
    keys = list(combinations([i for i in range(b)], b-r+1))
    print(keys)


ans = solution(5, 3)