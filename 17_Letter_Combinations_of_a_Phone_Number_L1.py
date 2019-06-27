class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        
        ans = ['']
        for digit in digits:
            ans = [c + letter for c in ans for letter in mapping[digit]]
        
        return ans if len(ans) > 1 else []
        

# Back-tracking solution
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        self.mapping = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        self.ans = []
        self.digits = digits

        def dfs(cur_d: str, tmp: str) -> None:
            if len(self.digits) == len(tmp):
                self.ans.append(tmp)
                return
            
            for i, d in enumerate(digits):
                for c in self.mapping[d]:
                    dfs(digits[i+1:], tmp+c)
        
        dfs(digits, '')
        return self.ans