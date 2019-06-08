class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        rightmost = {c:i for i, c in enumerate(S)}
        left, right = 0, 0
        ans = []

        for i, c in enumerate(S):
            right = max(right, rightmost[c])
            
            if i == right:
                ans.append(left-right+1)
                left = right + 1
        return ans