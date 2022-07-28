# Histogram Model

Template:

``` py
hist = [0] * len(A[0])
        
for i in range(len(A)):
    for j in range(len(A[0])):
        if A[i][j]: hist[j] += 1
        else: hist[j] = 0
```
