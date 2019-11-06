""" Facebook
celebrity is other people know him, but he does not know any of them.
bool know(a, b): whether
"""
class findCelebrity(self, n: int):
    candidate = 0
    for i in range(1, n):
        if knows(candidate, i)
            candidate = i
    for i in range(n):
        if i != candidate and knows(candidate, i) or  not know(i, candidate):
            return -1
    return candidate