# Two pointer

## Explanation

Two pointer is usually used in array, there are two pointer `i` and `j` point to the begin and end of the array.
We need to use a `while` loop to move the two pointers and add logic based on problem requirement.

## Template

Same direction template:

``` py
# basic version
i = 0
ans = ?
for j in range(len(A)):
    if/while LOGIC:
        MOVE_i
    UPDATE_answer
# another version
i, j = 0, 0
ans = ?
while i<len(A) and j<len(A):
    MOVE_i
    MOVE_j
    UPDATE_answer
```

Different direction template:

``` py
l, r = 0, len(A)-1
ans = 0
while l<=r:
    "Logic for A and ans"
```
