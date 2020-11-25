class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        mapper = {'a': ".-", 'b': "-...", 'c': "-.-.", 'd': "-..", 
                  'e': ".", 'f': "..-.", 'g': "--.", 'h': "....", 
                  'i': "..", 'j': ".---", 'k': "-.-", 'l': ".-..",
                  'm': "--", 'n': "-.", 'o': "---", 'p': ".--.", 
                  'q': "--.-", 'r': ".-.", 's': "...", 't': "-", 'u': "..-"
                  , 'v': "...-", 'w': ".--", 'x': "-..-",'y': "-.--", 'z': "--.."}
        ans = set()
        for word in words:
            morse = ''
            for c in word:
                morse += mapper[c]
            ans.add(morse)
        return len(ans)