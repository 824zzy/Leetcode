# Note

## Bottom up

"""py
def dfs(node, args):
    if not node:
        return 0/None
    node.left = dfs(node.left)
    node.right = dfs(node.right)
    # do sth
    return node
"""

## Regular