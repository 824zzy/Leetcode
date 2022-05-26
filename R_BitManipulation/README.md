# Bit Manipulation

## Operations

1. Get lowest bit in x: `x & 1`: 191, 461
2. Get lowest "1" bit and right side bits in x: `x & -x`
3. Set lowest "1" bit in x to "0": `x & (x-1)`
4. Flip whole n-bits bit mask: `x ^= (1 << n) - 1`
5. Three ways to flip a bit on/off:
   1. `x+(2**n)`: flip n-th bit on in `x`
   2. `x-(2**n)`: flip n-th bit off in `x`
   3. `x^(2**n)`: flip n-th bit on/off in `x`
   4. `x^(1<<n)`: flip n-th bit on/off in `x`
6. Gray code of a integer `i`: `(i>>1)^i`
7. 32 bit mask in hexadecimal: `0xffffffff`
8. XOR from 1 to n:

    ``` py
    def XOR_1_to_n(n):
        m = n%4
        if m==0: return n
        elif m==1: return 1
        elif m==2: return n+1
        else: return 0
    ```

### Functions

1. XOR operation: `a ^ 0 = a`  `a ^ a = 0`
2. bin(number): `0b***`
3. Decimal conversion: `int(num, decimal)`, e.g. `int('10', 2)==2`
4. Pre fill zero to num: `rjust(num)`; Post fill zero to num: `ljust(num)`
5. `str.zfill(32)`: fill a string with 0 to 32 bit
6. `'{0:032b}'.format`: a short way to format the integer to a 32 bit binary

## Bitmask

1. `range(1<<N)`: iterate all the states by bit mask
2. **`mask & (1<<i)`**: choose i-th bit in 2**i format in bit mask
3. `mask>>i & 1`: choose i-th bit in bit mask
4. `mask ^ 1<<i`: flip i-th bit in bit mask
5. `mask & ~masks[i]`: subtract i-th mask from current mask

``` py
for mask in range(1 << n): 
    for i in range(n):
        if mask & 1<<i :
            `mask ^ 1<<i`
    ans.append(seq)
return ans 
```

## Reference

- [bitmask problem list](https://leetcode.com/discuss/general-discussion/1125779/Dynamic-programming-on-subsets-with-examples-explained)
