# Probability

1. `random.randint(a, b)`: Choose integer from `a<=x<=b`.
2. `random.random()`: Return the next random floating point number in the range [0.0, 1.0).

## Reservoir Sampling

``` py
cnt, ans = 0, 0
for i in range(len(A)):
    cnt += 1
    p = random.random()
    if p < 1/cnt:
        ans = A[i]
return ans
```
