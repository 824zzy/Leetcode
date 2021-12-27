""" Graph BFS
"""
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        queue = [node]
        ans = {node: Node(node.val, [])}
        while queue:
            currNode = queue.pop()
            for nei in currNode.neighbors:
                if nei not in ans:
                    newNode = Node(nei.val, [])
                    ans[nei] = newNode
                    queue.append(nei)
                ans[currNode].neighbors.append(ans[nei])
        return ans[node]