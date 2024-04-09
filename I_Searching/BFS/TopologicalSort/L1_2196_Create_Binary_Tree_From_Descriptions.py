""" https://leetcode.com/problems/create-binary-tree-from-descriptions/
1. find all the nodes
2. build graph and in-degree counter
3. build tree by topological sort
"""


class Solution:
    def createBinaryTree(self, A: List[List[int]]) -> Optional[TreeNode]:
        # find all the nodes
        nodes = []
        for i, j, _ in A:
            nodes.extend([i, j])
        # build graph and in-degree counter
        e = defaultdict(list)
        inD = Counter(set(nodes))
        for i, j, k in A:
            e[i].append([j, k])
            inD[j] += 1
        # build tree by topological sort
        Q = [TreeNode(i) for i, d in inD.items() if d == 1]
        ans = Q[0]
        while Q:
            i = Q.pop(0)
            for j, is_left in e[i.val]:
                node = TreeNode(j)
                if is_left:
                    i.left = node
                else:
                    i.right = node
                inD[j] -= 1
                if inD[j] == 1:
                    Q.append(node)
        return ans
