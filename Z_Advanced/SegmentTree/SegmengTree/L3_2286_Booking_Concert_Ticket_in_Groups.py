""" https://leetcode.com/problems/booking-concert-tickets-in-groups/
Gather: query & update minimum available row
Scatter: query & update range of available rows

Reference: https://leetcode.com/problems/booking-concert-tickets-in-groups/discuss/2083802/C%2B%2B-Segment-Tree-(Max-Sum)-with-Explanation

TODO: update answer
"""


class Node:
    def __init__(self, lo, hi, sm=0, mx=0, lazy=0):
        self.lo = lo
        self.hi = hi
        self.mx = mx  # range max
        self.sm = sm  # range sum
        self.lazy = lazy  # lazy propagation for range update
        self.left = None
        self.right = None


class SegmentTree:
    def __init__(self, lo, hi, n, m):
        self.n = n
        self.m = m
        self.root = self.buildTree([m] * n, lo, hi)

    def buildTree(self, A, lo, hi):
        if lo > hi:
            return
        node = Node(lo, hi)
        if lo == hi:
            node.sm = self.m
            node.mx = self.m
        else:
            m = (lo + hi) // 2
            node.left = self.buildTree(A, lo, m)
            node.right = self.buildTree(A, m + 1, hi)
            node.sm = node.left.sm + node.right.sm
            node.mx = max(node.left.mx, node.right.mx)
        return node

    def rangeMax(self, node, lo, hi, k, maxRow):
        if lo > maxRow:
            return
        if node.mx < k:
            return
        if lo == hi:
            return lo, self.m - node.mx
        m = (lo + hi) // 2
        ans = self.rangeMax(node.left, lo, m, k, maxRow)
        if ans:
            return ans
        return self.rangeMax(node.right, m + 1, hi, k, maxRow)

    # def rangeMax(self, node, lo, hi, k):
    #     if node.mx<k: return 0, 0
    #     if node.lo==lo and node.hi==hi: return lo, self.m-node.mx
    #     m = (node.lo+node.hi)//2
    #     if hi<=m: return self.rangeMax(node.left, lo, hi, k)
    #     elif lo>m: return self.rangeMax(node.right, lo, hi, k)
    #     else:
    #         ll, lmx = self.rangeMax(node.left, lo, m, k)
    #         rr, rmx = self.rangeMax(node.right, m+1, hi, k)
    #         if ll>=rr: return ll, lmx
    #         else: return rr, rmx

    def updateMax(self, node, lo, hi, val, maxRow):
        if lo > maxRow or hi < maxRow:
            return
        if lo == hi:
            node.mx -= val
            node.sm -= val
            return
        m = (lo + hi) // 2
        node.sm -= val
        self.updateMax(node.left, lo, m, val, maxRow)
        self.updateMax(node.right, m + 1, hi, val, maxRow)
        node.mx = max(node.left.mx, node.right.mx)

    def rangeSum(self, node, lo, hi):
        if node.lo == lo and node.hi == hi:
            return node.sm
        m = (node.lo + node.hi) // 2
        if hi <= m:
            return self.rangeSum(node.left, lo, hi)
        elif lo > m:
            return self.rangeSum(node.right, lo, hi)
        else:
            return self.rangeSum(node.left, lo, m) + self.rangeSum(
                node.right, m + 1, hi
            )

    def updateSum(self, node, lo, hi, val, maxRow):
        if lo > maxRow:
            return
        if lo == hi:
            node.mx -= val
            node.sm -= val
            return
        m = (lo + hi) // 2
        node.sm -= val
        if m + 1 > maxRow or node.left.sm >= val:
            self.updateSum(node.left, lo, m, val, maxRow)
        else:
            val -= node.left.sm
            self.updateSum(node.left, lo, m, node.left.sm, maxRow)
            self.updateSum(node.right, m + 1, hi, val, maxRow)
        node.mx = max(node.left.mx, node.right.mx)


class BookMyShow:
    def __init__(self, n: int, m: int):
        self.ST = SegmentTree(0, n - 1, n, m)
        self.n = n
        self.m = m

    def gather(self, k: int, maxRow: int) -> List[int]:
        ans = self.ST.rangeMax(self.ST.root, 0, self.n - 1, k, maxRow)
        # ans = self.ST.rangeMax(self.ST.root, 0, maxRow, k)
        if ans:
            self.ST.updateMax(self.ST.root, 0, self.n - 1, k, ans[0])
        return ans

    def scatter(self, k: int, maxRow: int) -> bool:
        cnt = self.ST.rangeSum(self.ST.root, 0, maxRow)
        # print(cnt)
        if cnt >= k:
            self.ST.updateSum(self.ST.root, 0, self.n - 1, k, maxRow)
            return True
        return False


"""
["BookMyShow","gather","gather","scatter","scatter"]
[[2,5],[4,0],[2,0],[5,1],[5,1]]
["BookMyShow","scatter","scatter"]
[[2,6],[2,1],[8,0]]
["BookMyShow","scatter","gather","gather","gather","scatter"]
[[5,9],[2,2],[7,2],[4,1],[6,2],[2,1]]
["BookMyShow","scatter","scatter","gather","gather","gather","gather","gather","scatter","scatter","scatter"]
[[19,40],[34,14],[5,5],[20,6],[3,3],[50,7],[16,5],[12,0],[23,14],[36,0],[25,12]]
["BookMyShow","scatter","scatter","gather","scatter","gather","scatter","scatter","gather","gather","scatter","gather","gather","gather","scatter","scatter"]
[[18,48],[24,13],[12,5],[12,5],[3,12],[36,13],[25,6],[32,14],[29,6],[3,11],[30,0],[45,15],[23,17],[23,2],[41,10],[40,6]]
"""
