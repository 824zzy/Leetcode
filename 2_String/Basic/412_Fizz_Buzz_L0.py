""" Google
"""
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        rl = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                rl.append('FizzBuzz')
            elif i % 3 == 0:
                rl.append('Fizz')
            elif i % 5 == 0:
                rl.append('Buzz')
            else:
                rl.append(str(i))
        return rl
        