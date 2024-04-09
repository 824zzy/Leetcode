""" https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/
1. Use union find to find how many edges need to be added to make A and B fully connected
2. Use countA and countB to check if A and B are fully connected
"""
from header import *


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        A = list(range(n + 1))
        B = list(range(n + 1))
        countA = [n]
        countB = [n]

        def find(arr, x):
            if arr[x] != x:
                arr[x] = find(arr, arr[x])
            return arr[x]

        def union(arr, x, y, count):
            arr[find(arr, x)] = find(arr, y)
            count[0] -= 1

        edges.sort(reverse=True)
        cnt = 0
        for t, x, y in edges:
            if t == 1:
                if find(A, x) != find(A, y):
                    union(A, x, y, countA)
                    cnt += 1
            if t == 2:
                if find(B, x) != find(B, y):
                    union(B, x, y, countB)
                    cnt += 1
            if t == 3:
                if find(A, x) != find(A, y) and find(B, x) != find(B, y):
                    union(A, x, y, countA)
                    union(B, x, y, countB)
                    cnt += 1
        return len(edges) - cnt if countA[0] == 1 and countB[0] == 1 else -1
