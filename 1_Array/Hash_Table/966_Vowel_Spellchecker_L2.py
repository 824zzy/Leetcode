# Triple hashmap
class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        words = {w: w for w in wordlist}
        cap = {w.lower(): w for w in wordlist[::-1]}
        vowel = {re.sub("[aeiou]", '#', w.lower()): w for w in wordlist[::-1]}
        return [words.get(w) or cap.get(w.lower()) or vowel.get(re.sub("[aeiou]", '#', w.lower()), "") for w in queries]