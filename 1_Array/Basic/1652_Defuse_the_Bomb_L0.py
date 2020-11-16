class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k<0:
            k, code = abs(k), code[::-1]
            return [sum([code[j%len(code)] for j in range(i+1, i+k+1)]) for i in range(len(code))][::-1]
        else:
            return [sum([code[j%len(code)] for j in range(i+1, i+k+1)]) for i in range(len(code))]