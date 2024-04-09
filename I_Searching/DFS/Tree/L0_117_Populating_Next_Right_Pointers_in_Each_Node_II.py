""" https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
1. apply level order traversal using dfs and hash table
2. assign next node level by level
"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        T = defaultdict(list)

        def dfs(node, i):
            if not node:
                return
            T[i].append(node)
            dfs(node.left, i + 1)
            dfs(node.right, i + 1)

        dfs(root, 0)
        for _, nodes in T.items():
            for i in range(len(nodes) - 1):
                nodes[i].next = nodes[i + 1]
        return root
