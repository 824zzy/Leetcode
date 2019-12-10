# Sort by multiple condition
class Solution:
    def longestWord(self, words: List[str]) -> str:
        word_set = set(words)
        words.sort(key=lambda x:(-len(x), x))
        def traverse(word):
            for i in range(len(word), 1, -1):
                if word[:i] not in word_set:
                    return False
            return True
        
        for word in words:
            if traverse(word):
                return word