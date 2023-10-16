# Boyer-Moore Voting Algorithm

The Boyer-Moore voting algorithm is used to find the majority element among the given elements.

This algorithm works on the fact that if an element occurs more than N/X times, it means that the remaining elements other than this would definitely be less than N/X.

## Template

Note that it can be extend to find all the elements that occur more than N/X times.

``` py
cnt, cand = 0, None
for x in A:
    if x==cand: cnt += 1
    elif cnt==0: cand = x
    else: cnt -= 1
return cand
```

## Reference

- [GeeksforGeeks Boyer-Moore Voting Algorithm](https://www.geeksforgeeks.org/boyer-moore-majority-voting-algorithm/)