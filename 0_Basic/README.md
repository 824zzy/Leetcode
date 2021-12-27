# Basic Python

## Operations

1. `If Else` in `For`: `[a if cond1 else cond2 for a in A]`
2. Jump steps in a list: `list[::step]`
3. Insert item to list with specific index: `stk.insert(0, n)`
4. Sort array by multiple conditions: `arr.sort(key=lambda x: (cond1, cond2, ..))`. Condition can be `len(x)`, `x` #720
5. `sorted(list, key=functools.cmp_to_key(lambda x, y: int(y+x)-int(x+y)))`: custom compare function to a list