class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        if rounds[0]<=rounds[-1]:
            return [i for i in range(rounds[0], rounds[-1]+1)]
        else:
            return [i for i in range(1, rounds[-1]+1)]+[i for i in range(rounds[0], n+1)]

"""
4
[1,3,1,2]
2
[2,1,2,1,2,1,2,1,2]
7
[1,3,5,7]
3
[3,2,1,2,1,3,2,1,2,1,3,2,3,1]
"""