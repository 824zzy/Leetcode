""" https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/submissions/
1. build trie using template
2. dfs to traverse the trie
"""

from header import *


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = {}
        for f in folder:
            node = trie
            for c in f.split("/"):
                node = node.setdefault(c, {})
            node["#"] = f

        def dfs(node):
            if "#" in node:
                return [node["#"]]
            ans = []
            for n in node:
                ans.extend(dfs(node[n]))
            return ans

        return dfs(trie)
