# Sliding Window Template

Sliding window is usually used in array, there are two pointer `i` and `j`, `i` is alway initialize by 0 and `j` is initialize in for loop.

We need to always find the value k or initiate w, which are the threshold and container for updating the sliding window. And generally use while loop to maintain thredshold k and index i.

``` py
i = 0
for j in range(len(A)):
    while/if logic:
        update i
return ans/j-i+1
```
