# Sliding Window Template

``` sh
i = 0
ans = [0 or len(A)+1]
`init s` # sliding window
for j in range(len(A)):
    `s -= A[j] or s += A[j] or s *= A[j] or s /= A[j]`
    while `condition for s and i j`:
        ans = `relate to j-i+1`
        `s -= A[j] or s += A[j] or s *= A[j] or s /= A[j]`
        i += 1
return ans or return ans % (len(A)+1)
```

TODO: https://leetcode.com/problems/frequency-of-the-most-frequent-element/discuss/1175090/JavaC%2B%2BPython-Sliding-Window
