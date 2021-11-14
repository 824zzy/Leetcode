# Microsoft
from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r_c, m_c = Counter(ransomNote), Counter(magazine)
        for k, v in r_c.items():
            if v > m_c[k] or k not in m_c:
                return False
        return True