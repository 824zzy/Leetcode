""" https://leetcode.com/problems/maximum-bitwise-xor-after-rearrangement/
Greedy from MSB to LSB. To maximize the XOR result, at each bit position
prefer placing the opposite bit from t: if s[i]='1' use a '0' from t (XOR=1),
if s[i]='0' use a '1' from t (XOR=1). Fall back to the same bit if the
opposite is exhausted. O(n) time.
"""


class Solution:
    def maximumXor(self, s: str, t: str) -> str:
        s = list(s)
        cnt = Counter(t)
        for i in range(len(s)):
            if s[i] == '1':
                if cnt['0']:
                    cnt['0'] -= 1
                else:
                    cnt['1'] -= 1
                    s[i] = '0'
            elif s[i] == '0':
                if cnt['1']:
                    cnt['1'] -= 1
                    s[i] = '1'
                else:
                    cnt['0'] -= 1
        return ''.join(s)
