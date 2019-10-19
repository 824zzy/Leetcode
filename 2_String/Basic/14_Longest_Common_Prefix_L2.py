""" *zip trick: unzip
"""
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ans = ""
        for c in zip(*strs):
            if len(set(c)) == 1:
                ans += c[0]
            else:
                break
        return ans