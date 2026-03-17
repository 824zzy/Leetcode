# String

## When to Use

| Problem Signal | Technique |
|---|---|
| Check if palindrome (case/non-alphanumeric insensitive) | Filter + reverse comparison |
| Check if anagram | Counter comparison or sorted comparison |
| Group strings by anagram class | Hash table with sorted tuple as key |
| String comparison with custom order | `cmp_to_key` + sort |
| Find longest common prefix | `zip(*strs)` + check all equal |
| Digit-by-digit arithmetic (add, multiply) | Reverse iteration + carry tracking |
| Parse structured input (IP, number, time) | Split + validation helpers |
| Two-pointer simulation (spreading forces) | Mark boundaries, fill between |
| Character frequency constraints | Counter + validation |
| Case/format normalization | `.lower()`, `.upper()`, `.swapcase()`, `.isalpha()`, `.isnumeric()` |

## Common Patterns

### Palindrome Check

**Alphanumeric only, case insensitive (LC 125):**

```py
s = [c.lower() for c in s if c.isalnum()]
return s == s[::-1]
```

Alternative with string methods:

```py
s = s.lower().replace(" ", "")
for p in string.punctuation:
    s = s.replace(p, "")
return s == s[::-1]
```

### Anagram Check

**Exact character counts (LC 242):**

```py
return Counter(s) == Counter(t)
```

Alternative with sorting:

```py
return sorted(s) == sorted(t)
```

**Group anagrams (LC 49):**

```py
D = defaultdict(list)
for x in A:
    D[tuple(sorted(x))].append(x)
return D.values()
```

### Longest Common Prefix

**Zip all strings and check column equality (LC 14):**

```py
ans = ""
for c in zip(*strs):
    if len(set(c)) != 1:
        return ans
    ans += c[0]
return ans
```

### Digit Arithmetic

**Add two strings as numbers (LC 415):**

```py
a, b = list(map(int, a)), list(map(int, b))
carry = 0
ans = []
while a or b:
    x = a.pop() if a else 0
    y = b.pop() if b else 0
    ans.append((x + y + carry) % 10)
    carry = (x + y + carry) // 10
if carry:
    ans.append(carry)
return "".join(map(str, ans[::-1]))
```

### Custom String Comparison

**Sort by comparing concatenations (LC 179):**

```py
from functools import cmp_to_key

nums = sorted(
    map(str, nums),
    key=cmp_to_key(lambda x, y: int(y + x) - int(x + y))
)
ans = "".join(nums)
return ans if ans[0] != "0" else "0"
```

### Parsing and Validation

**Validate number with exponent (LC 65):**

Split by `e/E`, validate base as integer/decimal, validate exponent as integer.

```py
def is_integer(s):
    if not s: return False
    if s[0] in "+-": s = s[1:]
    return s.isdigit()

def is_decimal(s):
    if s[0] in "+-": s = s[1:]
    parts = s.split(".")
    if len(parts) > 2: return False
    if parts[0] == "": return parts[1].isdigit()
    return (parts[0].isdigit() and parts[1] == "") or \
           (parts[0].isdigit() and parts[1].isdigit())
```

**Parse string to integer (LC 8 atoi):**

```py
s = s.lstrip().split()
if not s: return 0
x = s[0]
sign = "+"
digits = ["0"]
for i, c in enumerate(x):
    if i == 0 and c in "+-":
        sign = c
    elif c.isdigit():
        digits.append(c)
    else:
        break
result = int("".join(digits))
if sign == "+":
    return min(result, 2**31 - 1)
else:
    return max(-result, -2**31)
```

### Two-Pointer Simulation

**Push dominoes (LC 838):**

Add boundary markers, find all L/R positions, fill intervals based on direction pairs.

```py
D = list("L" + D + "R")
A = [(i, x) for i, x in enumerate(D) if x in "LR"]
for i in range(1, len(A)):
    idx_l, sign_l = A[i - 1]
    idx_r, sign_r = A[i]
    if sign_l == "L" and sign_r == "L":
        D[idx_l + 1 : idx_r] = ["L"] * (idx_r - idx_l - 1)
    if sign_l == "R" and sign_r == "R":
        D[idx_l + 1 : idx_r] = ["R"] * (idx_r - idx_l - 1)
    if sign_l == "R" and sign_r == "L":
        n = (idx_r - idx_l - 1) // 2
        D[idx_l + 1 : idx_l + n + 1] = ["R"] * n
        D[idx_r - n : idx_r] = ["L"] * n
return "".join(D[1:-1])
```

## String API Reference

### Searching and Indexing

```py
s.index(sub)         # First index of substring (raises ValueError if not found)
s.find(sub)          # First index of substring (returns -1 if not found)
s.count(sub)         # Count non-overlapping occurrences
```

### Splitting and Joining

```py
s.split(sep)         # Split by separator (default: whitespace)
s.split()            # Split by any whitespace and remove empty strings
"-".join(["a", "b"]) # "a-b"
```

### Case and Character Type

```py
s.lower()            # Convert to lowercase
s.upper()            # Convert to uppercase
s.swapcase()         # Swap lower <-> upper
s.capitalize()       # First char upper, rest lower
s.title()            # Title case (first char of each word)

c.isalpha()          # True if letter
c.isdigit()          # True if digit
c.isalnum()          # True if letter or digit
c.isnumeric()        # True if numeric character
s.islower()          # True if all cased chars are lowercase
s.isupper()          # True if all cased chars are uppercase
```

### Modification

```py
s.replace(old, new)  # Replace all occurrences
s.strip()            # Remove leading/trailing whitespace
s.lstrip()           # Remove leading whitespace
s.rstrip()           # Remove trailing whitespace
```

### Character Conversion

```py
ord(c)               # Character to ASCII code
chr(n)               # ASCII code to character
```

### Formatting

```py
f"{x:.2f}"           # Format float to 2 decimal places
f"{x:>5}"            # Right-align in width 5
f"{x:<5}"            # Left-align in width 5
```

### Iteration

```py
zip(s1, s2)          # Pair up characters from two strings
zip(*strs)           # Transpose list of strings (columns become rows)
```

```py
# Example: longest common prefix
for chars in zip(*strs):
    if len(set(chars)) == 1:
        prefix += chars[0]
```

### Other Utilities

```py
string.punctuation        # All punctuation characters: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
string.ascii_lowercase    # 'abcdefghijklmnopqrstuvwxyz'
string.ascii_uppercase    # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
```

## Collections

### Counter

```py
from collections import Counter

c = Counter(s)
c.most_common(n)     # List of n most common (char, count) pairs
c.total()            # Sum of all counts (Python 3.10+)
c1 + c2              # Add counts
c1 - c2              # Subtract (keep only positive)
c1 & c2              # Intersection: min(c1[x], c2[x])
c1 | c2              # Union: max(c1[x], c2[x])
```

### defaultdict

```py
from collections import defaultdict

# Avoid KeyError when accessing missing keys
d = defaultdict(list)
d = defaultdict(int)
d = defaultdict(set)
```

## LC References

### Palindrome
- LC 125: Valid Palindrome (alphanumeric, case insensitive)
- LC 9: Palindrome Number
- LC 2108: First Palindromic String in Array

### Anagram
- LC 242: Valid Anagram (compare two strings)
- LC 49: Group Anagrams (hash by sorted tuple)

### Prefix/Suffix
- LC 14: Longest Common Prefix (zip columns)
- LC 1961: Check if String is Prefix of Array
- LC 2255: Count Prefixes of Given String

### Digit Arithmetic
- LC 415: Add Strings (carry tracking)
- LC 989: Add to Array-Form of Integer
- LC 66: Plus One
- LC 43: Multiply Strings

### Custom Comparison
- LC 179: Largest Number (cmp_to_key with concatenation)
- LC 1433: Check if String Can Break Another String (sorted comparison)

### Parsing/Validation
- LC 65: Valid Number (split by exponent, validate parts)
- LC 8: String to Integer (atoi) (handle sign, digits, overflow)
- LC 468: Validate IP Address (split and validate octets/hextets)
- LC 393: UTF-8 Validation (bit manipulation + state machine)

### Simulation
- LC 838: Push Dominoes (boundary markers + interval filling)
- LC 2000: Reverse Prefix of Word
- LC 151: Reverse Words in String
- LC 557: Reverse Words in String III

### Character Frequency
- LC 451: Sort Characters by Frequency
- LC 1684: Count Consistent Strings
- LC 1832: Check if Sentence is Pangram

### Roman Numerals
- LC 12: Integer to Roman
- LC 13: Roman to Integer

### Transformation
- LC 2129: Capitalize the Title
- LC 520: Detect Capital
- LC 1768: Merge Strings Alternately
- LC 1957: Delete Characters to Make Fancy String

### Pattern Matching
- LC 1408: String Matching in Array
- LC 1813: Sentence Similarity III
