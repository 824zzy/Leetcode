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

### Priority Queue/ Heap

1. Create:
   1. C++(Max heap): `priority_queue<int> q;`. For minHeap is `priority_queue<int, vector<int>, great<int>> q;`
   2. Python: `q = []`
2. Create from array:
   1. C++: `vector<int> a{2,1,3,4}; priority_queue<int> q(begin(a), end(a));`
   2. Python: `q = [1,2,3,4,5], heapq.heapify(q)`
3. Insert:
   1. C++: `q.push(x)`
   2. Python: `heapq.heappush(q, x)`
4. Peek:
   1. C++: `int x = q.top();`
   2. Python: `x = q[0]`
5. Pop:
   1. C++: `q.pop()`
   2. Python: `x = heapq.heappop(q)`

### Type Conversion

1. Array to Set
   1. C++: `vector<int> a{1,2,3,4}, set<int> b(begin(a), end(a))`
   2. Python: `a = [1,2,3,4], b = set(a)`
2. Set to Array:
   1. C++: `set<int> a{1,2,3}; vector<int> b(begin(a), end(a));`
   2. Python: `a = set([1,2,3]), b = list(a)`
3. Integer to String:
   1. C++: `int x = 12345; string s = std::to_string(x);`
   2. Python: `x = 12345, s = str(x)`
4. String to Integer:
   1. C++: `string s{"12345"}; int x = std::stoi(s);`
   2. Python: `s = "12345", x= int(s)`
5. Char to ASCII:
   1. C++: `char c = '9'; int x = c - '9'`
   2. Python: `c = '9', x = ord(c)-ord('0'), x = int(c)`

### String Operation

1. Init:
   1. C++: `string s='111'`/`string s{"111"}`
   2. Python: `s='111'`
2. Interception:
   1. C++: `string s='12345'; s.substr(3)//'345'; s.substr(3, 2); //'34'`
   2. Python: `s='12345', s[3:]#'345', s[3:5]#'34'`
3. Modification:
   1. C++: `s[1]=2;//121`
   2. Python: `s = s[0:1]+'2'+s[2:]`

## Reference

1. [用什么语言刷题？C++/Java/Python横向大比较](https://www.youtube.com/watch?v=ZyCQBrcr6jk&list=PLLuMmzMTgVK7XfFadhkPuF_ztvhxbriDr&index=7)