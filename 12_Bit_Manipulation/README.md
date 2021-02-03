# Note

## Operations

### Theory/Principle

1. get lowest set bit: `x & -x`
2. three ways to flip a bit on/off:
   1. `x+(2**n)`: flip n-th bit on in `x`
   2. `x-(2**n)`: flip n-th bit off in `x`
   3. `x^(2**n)`: flip n-th bit on/off in `x`
   4. `x^(1<<n)`: flip n-th bit on in `x`

### Coding

1. XOR operation: `a ^ 0 = 0`  `a ^ a = 0`
2. bin(number): `0b***`
3. Decimal conversion: `int(num, decimal)`, e.g. `int('10', 2)==2`
4. Pre fill zero to num: `rjust(num)`; Post fill zero to num: `ljust(num)`
5. 32 bit mask in hexadecimal: `0xffffffff`

## Examples

### Two sum

``` py
class Solution:
    def getSum(self, a: int, b: int) -> int:
        ## RC ##
        ## APPROACH : BITWISE OPERATIONS ##
        ## LOGIC ##
        #   1. For any two numbers, if their binary representations are completely opposite, then XOR operation will directly produce sum of numbers ( in this case carry is 0 )
        #   2. what if the numbers binary representation is not completely opposite, XOR will only have part of the sum and remaining will be carry, which can be produced by and operation followed by left shift operation.
        #   3. For Example 18, 13 => 10010, 01101 => XOR => 11101 => 31 (ans found), and operation => carry => 0
        #   4. For Example 7, 5
        #   1 1 1                   1 1 1
        #   1 0 1                   1 0 1
        #   -----                   -----
        #   0 1 0   => XOR => 2     1 0 1  => carry => after left shift => 1 0 1 0
        #   2                                                              10
        # now we have to find sum of 2, 10 i.e a is replace with XOR result and b is replaced wth carry result
        # similarly repeating this process till carry is 0
        #   steps will be 7|5 => 2|10 => 8|4  => 12|0

        ## TIME COMPLEXITY : O(1) ##
        ## SPACE COMPLEXITY : O(1) ##

        # 32 bit mask in hexadecimal
        mask = 0xffffffff # (python default int size is not 32bit, it is very large number, so to prevent overflow and stop running into infinite loop, we use 32bit mask to limit int size to 32bit )
        while(b & mask > 0):
            carry = (a & b) << 1
            a = a ^ b
            b = carry
        return (a & mask) if b > 0 else a
```
