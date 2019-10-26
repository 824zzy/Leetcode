# Note

## Bottom up

"""py
def dfs(node):
    if not node:
        return
    node.left = dfs(node.left)
    node.right = dfs(node.right)
    # do sth
    return node
"""
