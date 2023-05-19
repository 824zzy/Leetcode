from collections import Counter
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        all_city = []
        end = []
        for path in paths:
            all_city.extend(path)
            end.append(path[-1])
        
        all_city = Counter(all_city)
        
        ans = []
        for k, v in all_city.items():
            if v == 1:
                ans.append(k)
        
        for a in ans:
            if a in end:
                return a