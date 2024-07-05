""" L1: https://zhenchaogan.gitbook.io/leetcode-solution/leetcode-1650-lowest-common-ancestor-of-a-binary-tree-iii
cyclic two pointer
"""


class Solution:
    def lowestCommonAncestor(self, p: "Node", q: "Node") -> "Node":
        pp, qq = p, q
        while pp != qq:
            if not pp:
                pp = qq
        else:
            pp = pp.parent
        if not qq:
            qq = pp
        else:
            qq = qq.parent
        return pp
