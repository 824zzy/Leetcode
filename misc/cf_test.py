""" https://codeforces.com/problemset/problem/263/A
"""
""" Amazon OA Problem 1
"""
class solution:
    def solution(self, s):
        return ''.join([chr((219-ord(c))) if 97<=ord(c)<=122 else c for c in s])
            

s = solution()
ans = s.solution('wrw blf hvv ozhg mrtsg\'h vkrhlwv?')
print(ans)



# L  = [int(x) for x in input().split()]
# From  = [int(x) for x in input().split()]
# To = [int(x) for x in input().split()]

# ans = L
# for i, j in zip(From, To):
#     ans.remove(i)
#     ans.append(j)

# print(sorted(list(ans)))

# """
# 1. 1 1 7 6 8
# 2. 1 2 7 6 8
# 3. 1 2 9 6 8
# 4. 1 5 9 6 8

# 5 6 8 9
# """