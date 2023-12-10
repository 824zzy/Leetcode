# Sliding Window Template

Sliding window is usually used in array, there are two pointer `i` and `j`, `i` is alway initialize by 0 and `j` is initialize in for loop.

We need to always find the value k or initiate w, which are the threshold and container for updating the sliding window. And generally use while loop to maintain thredshold k and index i.

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

## Fixed Window

``` py
TODO:
```

## Find Difference

If the problem asks the number of subarrays with at most K distinct elements, please come up with this type of template immediately!

``` py
def atMost(A, k):
    cnt = Counter()
    i, ans = 0, 0
    for j in range(len(A)):
        cnt[A[j]] += 1
        while len(cnt)>k:
            cnt[A[i]] -= 1
            if cnt[A[i]]==0: del cnt[A[i]]
            i += 1
        ans += j-i+1
    return ans
return atMost(A, k)-atMost(A, k-1)
```
