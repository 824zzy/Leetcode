# Sliding Window Template

Sliding window is usually used in array, there are two pointer `i` and `j`, `i` is alway initialize by 0 and `j` is initialize in for loop.

We need to always find the value k or initiate w, which are the threshold and container for updating the sliding window. And generally use while loop to maintain threshold k and index i.

Note that sliding window technique only for **Non-Negative element array**.

## Dynamic Window

``` py
i = 0
# cnt/container
for j in range(len(A)):
    # update cnt/container
    while/if logic:
        # update i
    # update answer
```