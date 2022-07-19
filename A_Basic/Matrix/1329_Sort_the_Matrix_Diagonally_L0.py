""" https://leetcode.com/problems/sort-the-matrix-diagonally/
1. build diagnal hash table
2. sort the diagnal array
3. reconstruct matrix
"""
class Solution:
    def diagonalSort(self, A: List[List[int]]) -> List[List[int]]:
        # build diagnal hash table
        mp = defaultdict(list)
        for i in range(len(A)):
            for j in range(len(A[0])):
                mp[i-j].append(A[i][j])
        # sort the diagnal array
        mp = {k: sorted(v) for k, v in mp.items()}
        # reconstruct matrix
        for i in range(len(A)):
            for j in range(len(A[0])):
                A[i][j] = mp[i-j].pop(0)
        return A