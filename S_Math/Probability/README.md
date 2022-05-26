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

## Rejection Sampling

``` py
while 1:
    SAMPLING
    if ACCPET: return sample
```

## Knuth/Fisher-Yates shuffle

``` py
for i in range(1, len(self.A)): 
    ii = randint(0, i)
    self.A[ii], self.A[i] = self.A[i], self.A[ii]
```

## Reference

- [Fisher–Yates shuffle](https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle)
- [Rejection sampling](https://en.wikipedia.org/wiki/Rejection_sampling)