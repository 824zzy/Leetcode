class Codec:
    def __init__(self):
        self.tree = defaultdict(list)

    def serialize(self, node: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        def encode(node):
            if not node:
                return ''
            else:
                return str(node.val)+'-'+encode(node.left)+encode(node.right)
        return encode(node)
        

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        def insert(node, val):
            if not node:
                return TreeNode(val)
            if val<=node.val:
                node.left = insert(node.left, val)
            else:
                node.right = insert(node.right, val)
            return node
        data = data.split('-')
        data.pop()
        node = None
        for d in data:
            node = insert(node, int(d))
        return node