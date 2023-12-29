# Two pointer

## Explanation

Two pointer is usually used in array, there are two pointer `i` and `j` point to the begin and end of the array.
We need to use a `while` loop to move the two pointers and add logic based on problem requirement.

## Template

Same direction template:

``` py
# basic version
def twopointers(self, A: List[int]) -> int:
    i = 0
    ans = ?
    for j in range(len(A)):
        if LOGIC:
            MOVE_i
        UPDATE_answer

# advanced version
def twopointers(self, A: List[int]) -> int:
    i = 0
    DEFINE CONTAINER
    ans = ?
    for j in range(len(A)):
        while LOGIC: 
            UPDATE_CONTAINER
            i += 1
        UPDATE_answer
```

Different direction template:

``` py
def twopointers(self, A: List[int]) -> int:
    l, r = 0, len(A)-1
    ans = 0
    while l<=r:
        "Logic for A and ans"
    return ans
```
