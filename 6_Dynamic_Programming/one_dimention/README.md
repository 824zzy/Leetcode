# Note

## Pattern

``` py
if not nums:
    return 0
dp = [0] * len(nums)
dp[0] = 1
for i in range(1, len(nums)):
    # Do sth
    for j in range(0, i):
        # Do sth
    # Do sth
return sth
```

## TODO list

1. 256
