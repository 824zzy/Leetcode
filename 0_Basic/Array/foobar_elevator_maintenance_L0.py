""" https://foobar.withgoogle.com/elevator-maintenance
"""
def solution(A):
    A = [[int(c) for c in x.split('.')] for x in A]
    A.sort()
    A = ['.'.join([str(c) for c in x]) for x in A]
    return A