# Bitmask

## Bitmask Template

> `range(1<<N)`: iterate all the states by bit mask
> **`mask & 1<<i`**: choose i-th bit in 2**i format in bit mask
> `mask>>i & 1`: choose i-th bit in bit mask
> `mask ^ 1<<i`: flip i-th bit in bit mask

``` py
for mask in range(1 << N): 
    for i in range(N):
        if mask & 1<<i :
            `mask ^ 1<<i`
    ans.append(seq)
return ans 
```

## Reference

- [bitmask problem list](https://leetcode.com/discuss/general-discussion/1125779/Dynamic-programming-on-subsets-with-examples-explained)
