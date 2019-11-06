class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        mapping = {
            '2': ['a','b','c'],
            '3': ['d','e','f'],
            '4': ['g','h','i'],
            '5': ['j','k','l'],
            '6': ['m','n','o'],
            '7': ['p','q','r','s'],
            '8': ['t','u','v'],
            '9': ['w','x','y','z'],
        }
        ans = []
        def combination(S, curr):
            if len(curr)==len(digits):
                ans.append(curr[:])
                return
            for i, s in enumerate(S):
                for c in mapping[s]:
                    combination(S[i+1:], curr+c)
        combination(digits, '')
        return ans