""" https://leetcode.com/problems/validate-ip-address/
be careful
"""


class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        def check_IPV4(s):
            if len(s) != 4:
                return False
            for c in s:
                # check leading zero
                if len(c) > 1 and c[0] == '0':
                    return False
                # check valid range
                try:
                    int(c)
                except BaseException:
                    return False
                if not 0 <= int(c) <= 255:
                    return False
            return True

        def check_IPV6(s):
            if len(s2) != 8:
                return False
            for c in s:
                # check length
                if not 1 <= len(c) <= 4:
                    return False
                # check valid range
                try:
                    int(c, 16)
                except BaseException:
                    return False
            return True

        s1 = queryIP.split('.')
        s2 = queryIP.split(':')

        is_IPV4 = check_IPV4(s1)
        is_IPV6 = check_IPV6(s2)
        if is_IPV4:
            return "IPv4"
        if is_IPV6:
            return "IPv6"
        else:
            return "Neither"
