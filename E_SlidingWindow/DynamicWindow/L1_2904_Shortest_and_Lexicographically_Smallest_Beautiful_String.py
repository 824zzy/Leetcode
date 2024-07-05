""" https://leetcode.com/problems/shortest-and-lexicographically-smallest-beautiful-string/
sliding window template
"""
# sliding window: O(n)


class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ans = "z" * len(s)
        sw = []
        kk = 0
        for i in range(len(s)):
            while kk >= k or (sw and sw[0] == "0"):
                kk -= sw.pop(0) == "1"
            sw.append(s[i])
            kk += s[i] == "1"
            if kk == k:
                ans = min(ans, "".join(sw), key=lambda x: (len(x), x))

        if ans != "z" * len(s):
            return ans
        else:
            return ""


# brute force: O(n^3)
class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ans = "z" * len(s)
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                if s[i:j].count("1") == k:
                    ans = min(ans, s[i:j], key=lambda x: (len(x), x))
        if ans != "z" * len(s):
            return ans
        else:
            return ""


# enumerate length as we need to find the lexicographically smallest
# string: O(n^3)
class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        if s.count("1") < k:
            return ""
        for size in range(k, len(s) + 1):
            ans = ""
            for i in range(size, len(s) + 1):
                t = s[i - size : i]
                if t.count("1") == k and (ans == "" or t < ans):
                    ans = t
            if ans:
                return ans


"""
"100011001"
3
"1011"
2
"000"
1
"""
