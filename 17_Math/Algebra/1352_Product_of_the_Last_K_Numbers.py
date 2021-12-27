""" L1: https://leetcode.com/problems/product-of-the-last-k-numbers/
1. Initialize an array with value 1 and is used to store the prefix product.
2. Whenever a new number is added, append the prefix with (prefix[-1] x num)
3. Product of last k numbers would be (prefix[-1] // prefix[-1-k])
"""
class ProductOfNumbers:
    def __init__(self):
        self.prefix = [1]

    def add(self, num: int) -> None:
        if num==0: self.prefix = [1]
        else: self.prefix.append(self.prefix[-1]*num)

    def getProduct(self, k: int) -> int:
        if k>=len(self.prefix): return 0
        return self.prefix[-1]//self.prefix[-1-k]