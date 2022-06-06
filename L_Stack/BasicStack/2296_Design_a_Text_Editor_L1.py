""" https://leetcode.com/problems/design-a-text-editor/
"""
class TextEditor:
    def __init__(self):
        self.before = []
        self.after = []
        
    def addText(self, text: str) -> None:
        self.before += list(text)
        
    def deleteText(self, k: int) -> int:
        ans = 0
        while self.before and k:
            self.before.pop()
            k -= 1
            ans += 1
        return ans

    def cursorLeft(self, k: int) -> str:
        while self.before and k:
            self.after.append(self.before.pop())
            k -= 1
        return ''.join(self.before[-10:])

    def cursorRight(self, k: int) -> str:
        while self.after and k:
            self.before.append(self.after.pop())
            k -= 1
        return ''.join(self.before[-10:])