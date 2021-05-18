class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        files = {}
        for path in paths:
            path = path.split()
            for i in range(1, len(path)):
                content = path[i].split('(')
                p = '/'.join([path[0], content[0]])
                c = content[1][:-1]
                if c not in files: files[c] = [p]
                else: files[c].append(p)
                
        return [v for _, v in files.items() if len(v)>1]