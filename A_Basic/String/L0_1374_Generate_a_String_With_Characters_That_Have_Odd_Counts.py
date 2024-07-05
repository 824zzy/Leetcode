class Solution:
    def generateTheString(self, n: int) -> str:
        return (
            "".join([chr(97) for _ in range(n - 1)] + [chr(98)])
            if n % 2 == 0
            else "".join([chr(97) for _ in range(n)])
        )
