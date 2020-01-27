# Leetcode fun

One question per day to ensure a sharp mind.

## Language Differences Cheatsheet

> `T` means data type: int, float etc.

### Data Structure

1. Array:
   1. C++: `T dirs[5]`
   2. Python: `[0] * 5`
2. Dynamic Array:
   1. C++: `vector<T>`
   2. Python: `[]`
3. Linked List:(rarely used)
   1. C++: `list<T>`
   2. Python: N/A
4. Ordered Set/Map:
   1. C++: `set<T>`, `map<T>`
   2. Python: N/A
5. Hash Set/Map:
   1. C++: `unordered_set<T>`, `unordered_map<T>`
   2. Python: `set()`, `dict()`
6. Heap:
   1. C++: `priority_queue<T>`
   2. Python: `[] via heapq APIs`
7. Queue/Deque:
   1. C++: `queue<T>`, `deque<T>`
   2. Python: `collections.deque()`
8. Stack:
   1. C++: `stack<T>`
   2. Python: `[]`
9. Pair/Tuple:
   1. C++: `pair<T1, T2>`, `tuple<T1, T2, T3>`
   2. Python: `(x, y)`, `(x, y, z)`
10. Customized:
    1. C++: `struct`, `class`, `long`
    2. Python: `class`, `tuple`

### Array Initialization

1. 1D:
   1. C++: `vector<int> a{1, 2, 3};`
   2. Python: `a=[1, 2, 3]`
2. 1D init to x:
   1. C++: `vector<int> a(n, x);`
   2. Python: `a = [x]*n`
3. 2D init to x:
   1. C++: `vector<vector<int>> a(m, vector<int>(n, x));`
   2. Python: `a = [[x]*n for _ in range(m)]`

### Array Operation

1. Add:
   1. C++: `vector<int> a;`, `a.push_back(x);`
   2. Python: `a = []`, `a.append(x)`
2. Remove:
   1. C++: `a.pop_back(x);`
   2. Python: `del a[-1]`/`a[:-1]` # made a copy
3. Access:
   1. C++: `a[index];`, `a.back();`
   2. Python: `a[index]`, `a[-1]`

### Hash Table

1. Create:
   1. C++: `unordered_map<int, int> m;`
   2. Python: `a = dict()`
2. Insert:
   1. C++: `m[key] = value;`
   2. Python: `a[key] = value`
3. Get:
   1. C++: `value = m[key]`
   2. Python: `value = a[key]`
4. Contain:
   1. C++: `m.count(key);`
   2. Python: `key in a`
5. Iterate:
   1. C++: `for(const auto& p: m){key=p.first; value=p.second;}`
   2. Python: `for k, v in a.items(): pass`

### Priority queue/ Heap

1. Create:
   1. C++(Max heap): `priority_queue<int> q;`. For minHeap is `priority_queue<int> `

## Reference

1. [用什么语言刷题？C++/Java/Python横向大比较](https://www.youtube.com/watch?v=ZyCQBrcr6jk&list=PLLuMmzMTgVK7XfFadhkPuF_ztvhxbriDr&index=7)