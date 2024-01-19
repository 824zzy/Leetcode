# Find Difference

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