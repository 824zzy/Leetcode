class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        V1 = version1.split('.')
        V2 = version2.split('.')
        maxL = max(len(V1), len(V2))
        V1 += ['0'] * (maxL - len(V1))
        V2 += ['0'] * (maxL - len(V2))
        for v1, v2 in zip(V1, V2):
            v1, v2 = int(v1), int(v2)
            if v1>v2:
                return 1
            elif v1<v2:
                return -1
        return 0