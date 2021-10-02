# Sliding Window Template

Sliding window is usually used in array, there are two pointer `i` and `j`, `i` is alway initialize by 0 and `j` is initialize in for loop.

We need to always find the value k or initiate w, which are the threshold and container for updating the sliding window. And generally use while loop to maintain thredshold k and index i.

``` sh
TODO: "https://leetcode.com/problems/frequency-of-the-most-frequent-element/discuss/1175090/JavaC%2B%2BPython-Sliding-Window

i = 0
ans = `condition`
`init s` # sliding window
for j in range(len(A)):
    `s -= A[j] or s += A[j] or s *= A[j] or s /= A[j]`
    while `condition for s and i j`:
        ans = `relate to j-i+1`
        `s -= A[j] or s += A[j] or s *= A[j] or s /= A[j]`
        i += 1
return ans or return ans % (len(A)+1)
```
