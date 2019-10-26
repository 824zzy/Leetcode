class Solution:
    def countAndSay(self, n: int) -> str:
        ans = '1'
        for _ in range(1, n):
            temp, curr, freq = '', ans[0], 0
            for n in ans:
                if curr==n:
                    freq += 1
                else:
                    temp += str(freq) + curr
                    curr = n
                    freq = 1
            ans = temp + str(freq) + curr
        return ans