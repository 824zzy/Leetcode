""" https://foobar.withgoogle.com/doomsday_fuel
"""
import numpy as np

def solution(A):
    print(A)
    # find_absorbing_state
    absorbing = [i for i, x in enumerate(A) if not sum(x)]
    non_absorbing = [i for i, x in enumerate(A) if sum(x)]
    # rearrange matrix to [I, O, R, Q]
    A = np.array(A)
    # A = A[np.ix_(absorbing+non_absorbing, absorbing+non_absorbing)]
    # print(A)
    I = A[np.ix_(absorbing, absorbing)]
    Q = A[np.ix_(non_absorbing, non_absorbing)]
    # comm_denom = np.prod(Q.sum(1)) 
    R = A[np.ix_(absorbing, non_absorbing)]
    print(I)
    print(Q)
    print(R)
    # I = np.identity(len(Q))
    F = (I-Q) ** (-1)
    print(F)
    B = F[0] * R * comm_denom / np.linalg.det(F)
    print(B)


# ans = solution([[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]]))
ans = solution([
  [0,1,0,0,0,1],  # s0, the initial state, goes to s1 and s5 with equal probability
  [4,0,0,3,2,0],  # s1 can become s0, s3, or s4, but with different probabilities
  [0,0,0,0,0,0],  # s2 is terminal, and unreachable (never observed in practice)
  [0,0,0,0,0,0],  # s3 is terminal
  [0,0,0,0,0,0],  # s4 is terminal
  [0,0,0,0,0,0],  # s5 is terminal
])
print(ans)
        
