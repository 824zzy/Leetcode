# Digit DP

## When to Use

| Problem Signal | Template Variant |
|---|---|
| Count numbers in [0, n] with property P | Basic template (upper bound only) |
| Count numbers in [low, high] with property P | Lower and upper bound template |
| Exclude numbers with leading zeros (e.g., "007" invalid) | Leading zero template (most common) |
| Constraint on digit sums, unique digits, or digit patterns | Add state tracking (mask, sum, previous digit, etc.) |
| String pattern matching (e.g., no substring "evil") | Digit DP + KMP automaton |
| Binary constraints (e.g., no consecutive 1s) | Use binary representation + previous digit state |
| Fixed suffix or prefix requirement | Constrain digit choices at certain positions |

## Core Concepts

Digit DP builds numbers digit by digit from left to right, tracking whether we're still bounded by the limit.

Key insight: `limit` tracks whether the current prefix still matches the upper bound. If we ever pick a digit smaller than the limit, all subsequent digits can be 0-9.

For range queries [low, high], compute `count(high) - count(low - 1)` or track both limits simultaneously.

## 1. Basic Template (Upper Bound Only)

Use when counting numbers in [1, n] with no leading zero concerns.

LC 233, 1067

```py
high = str(n)
n = len(high)

@cache
def dfs(i, limit):
    if i == n:
        return 1  # found one valid number
    ans = 0
    hi = int(high[i]) if limit else 9
    for d in range(hi + 1):
        ans += dfs(i + 1, limit and d == int(high[i]))
    return ans

return dfs(0, True)
```

## 2. Lower and Upper Bound Template

Use when counting numbers in [low, high] and leading zeros are allowed or irrelevant.

LC 2999

```py
high = str(n)
n = len(high)
low = str(m).zfill(n)  # pad to same length

@cache
def dfs(i, limit_low, limit_high):
    if i == n:
        return 1
    ans = 0
    lo = int(low[i]) if limit_low else 0
    hi = int(high[i]) if limit_high else 9
    for d in range(lo, hi + 1):
        ans += dfs(i + 1, limit_low and d == lo, limit_high and d == hi)
    return ans

return dfs(0, True, True)
```

## 3. Leading Zero Template (Most Common)

Use when numbers must not have leading zeros (e.g., "007" is invalid, treat as 7).

LC 902, 2376, 2719, 2801, 2827, 1012, 357

Key insight: `is_num` tracks whether we've started building the number. If `is_num == False` and we see '0' in low bound, we can skip this position (continue leading zeros).

```py
high = str(n)
n = len(high)
low = str(m).zfill(n)

@cache
def dfs(i, limit_low, limit_high, is_num):
    if i == n:
        return 1 if is_num else 0  # must have picked at least one digit
    ans = 0
    # option to skip this digit (continue leading zeros)
    if not is_num and low[i] == '0':
        ans += dfs(i + 1, True, False, False)

    lo = int(low[i]) if limit_low else 0
    hi = int(high[i]) if limit_high else 9
    d0 = 0 if is_num else 1  # if not started, can't pick 0
    for d in range(max(lo, d0), hi + 1):
        ans += dfs(i + 1, limit_low and d == lo, limit_high and d == hi, True)
    return ans

return dfs(0, True, True, False)
```

## State Tracking Variants

Add extra DP parameters to track problem-specific constraints.

### Tracking Digit Sum

LC 2719

```py
@cache
def dfs(i, limit_low, limit_high, is_num, digit_sum):
    if i == n:
        return 1 if min_sum <= digit_sum <= max_sum else 0
    # ... (rest similar to leading zero template)
    for d in range(max(lo, d0), hi + 1):
        ans += dfs(i + 1, limit_low and d == lo, limit_high and d == hi, True, digit_sum + d)
    return ans
```

### Tracking Unique Digits (Bitmask)

LC 2376, 1012, 357

```py
@cache
def dfs(i, limit_low, limit_high, is_num, mask):
    if i == n:
        return 1 if is_num else 0
    # ... (rest similar)
    for d in range(max(lo, d0), hi + 1):
        if mask & (1 << d) == 0:  # digit not used yet
            ans += dfs(i + 1, ..., mask | (1 << d))
    return ans
```

### Tracking Previous Digit

LC 600 (no consecutive 1s in binary)

Key insight: pass `pre` to avoid consecutive 1s or enforce patterns.

```py
high = bin(n)[2:]
n = len(high)

@cache
def dfs(i, limit_high, is_num, pre):
    if i == n:
        return is_num
    ans = 0
    if not is_num:
        ans += dfs(i + 1, False, False, None)
    hi = int(high[i]) if limit_high else 1
    for d in range(hi + 1):
        if pre != 1 or d != 1:  # no consecutive 1s
            ans += dfs(i + 1, limit_high and d == int(high[i]), True, d)
    return ans

return dfs(0, True, False, None) + 1  # +1 for zero
```

### Restricted Digit Set

LC 902, 788

Key insight: only iterate over allowed digits.

```py
allowed = set(map(int, digits))
# ... (rest similar)
for d in range(hi + 1):
    if d in allowed:
        ans += dfs(i + 1, limit_high and d == hi, True)
```

### Fixed Suffix Requirement

LC 2999

Key insight: after a certain prefix length, the digits must match a fixed suffix.

```py
diff = n - len(suffix)
# ...
if i < diff:
    # free choice (subject to limit and upper bound)
    for d in range(lo, min(hi, max_digit) + 1):
        ans += dfs(i + 1, limit_low and d == lo, limit_high and d == hi)
else:
    # must match suffix
    d = int(suffix[i - diff])
    if lo <= d <= min(hi, max_digit):
        ans = dfs(i + 1, limit_low and d == lo, limit_high and d == hi)
```

## Advanced: Digit DP + KMP

LC 1397

Use when counting strings (not numbers) that avoid a forbidden substring.

Key insight: track KMP state `j` representing longest matched prefix of evil string.

```py
# build KMP failure table
evil = " " + evil
sz = len(evil) - 1
ne = [0] * len(evil)
j = 0
for i in range(2, len(evil)):
    while j and evil[i] != evil[j + 1]:
        j = ne[j]
    if evil[i] == evil[j + 1]:
        j += 1
    ne[i] = j

@cache
def dfs(i, j, is_limit, s):
    if i == n:
        return 1
    up = ord(s[i]) if is_limit else 122
    ans = 0
    for d in range(97, up + 1):  # 'a' to limit
        x = chr(d)
        k = j
        while k and x != evil[k + 1]:
            k = ne[k]
        if x == evil[k + 1]:
            k += 1
        if k == sz:  # matched full evil string
            continue
        ans += dfs(i + 1, k, is_limit and d == up, s)
    return ans

return (dfs(0, 0, True, s2) - dfs(0, 0, True, s1) + (evil not in s1)) % MOD
```

## When to Pick Which Template

1. **Start with leading zero template** (template 3) unless the problem explicitly allows leading zeros.
2. **Add state parameters** (sum, mask, previous digit) as needed for constraints.
3. **Use lower+upper bound variant** (template 2) when range is [low, high] and you don't want to compute `count(high) - count(low - 1)`.
4. **Use binary representation** (`bin(n)`) when dealing with binary constraints (LC 600).
5. **Add KMP** when the constraint is substring-based (LC 1397).

## Common Gotchas

- Leading zeros: `is_num == False` means we haven't started the number yet. Once we pick a non-zero digit, `is_num` becomes True.
- Modulo: if the problem asks for result mod 1e9+7, apply mod in the return of each recursive call.
- Off-by-one: range [low, high] is inclusive. Pad `low` with `zfill(n)` to match length of `high`.
- Base case: return 1 (count this number) or 0 (invalid) when `i == n`.

## Deprecated Old Template

The following is kept for reference but not recommended. Use templates 1-3 above instead.

```py
"""
i: the current index of the digit array
isPrefix: if the new number is the prefix of N
isBigger: if the new number will be bigger than N when we reach final position

Extra parameters need to be added to the dp function depends on the problem
"""
# upper bound of the digit array
A = list(map(int, str(n)))

@cache
def dp(i, isPrefix, isBigger, *args):
    if i == len(A):
        return 0
    ans = 0
    for d in range(i == 0, 10):
        _isPrefix = isPrefix and d == A[i]
        _isBigger = isBigger or (isPrefix and d > A[i])
        if CONDITION and not (i == len(A) - 1 and _isBigger):
            # update answer
        ans += dp(i + 1, _isPrefix, _isBigger, *args)
    return ans

return dp(0, True, False)
```

## References

- [migfulcrum](https://leetcode.com/problems/rotated-digits/discuss/560601/python-digit-dp)
- [0x3ff template](https://leetcode.cn/problems/count-the-number-of-powerful-integers/solutions/2595149/shu-wei-dp-shang-xia-jie-mo-ban-fu-ti-da-h6ci/)