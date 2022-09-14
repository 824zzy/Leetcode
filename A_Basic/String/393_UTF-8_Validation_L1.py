""" https://leetcode.com/problems/utf-8-validation/
simulate four rules of UTF-8 encoding
"""
class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        A = [bin(d)[2:] .zfill(8)for d in data]
        i = 0
        while i<len(A):
            # 4 bytes
            if A[i][:5]=='11110':
                if i+3>=len(A) or any(x[:2]!='10' for x in A[i+1:i+4]):
                    return False
                i += 4
            # 3 bytes:
            elif A[i][:4]=='1110':
                if i+2>=len(A) or any(x[:2]!='10' for x in A[i+1:i+3]):
                    print('qq')
                    return False
                i += 3
            # 2 bytes:
            elif A[i][:3]=='110':
                if i+1>=len(A) or A[i+1][:2]!='10':
                    return False
                i += 2
            # 1 byte
            elif A[i][:1]=='0':
                i += 1
            else:
                return False

        return True
    
"""
[197,130,1]
[235,140,4]
[230,136,145]
"""