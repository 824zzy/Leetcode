class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_index = {}
        for index, ch in enumerate(s):
            last_index[ch] = index 
        cur_result = []
        for i, ch in enumerate(s):
            if ch not in cur_result:
                while cur_result and ch < cur_result[-1] and i < last_index[cur_result[-1]]:
                    cur_result.pop()
                cur_result.append(ch)
        return ''.join(cur_result)