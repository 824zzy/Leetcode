# Note

## Template

``` py
def search(self, nums: List[int], target: int) -> int:
   l, r = 0, len(nums)-1
   while l<=r:
      m = (l+r)//2
      # print(m)
      if nums[m]==target:
            return m
      elif nums[m]<target:
            l = m+1
      else:
            r = m-1
   return -1
```

## Tips

1. Reverse a list sometime useful.

## Modules

- `bisect`
   1. `insort(list, num)`, `insort_left(list, num)` and `insort_right(list, num)`: Insert num in a list. If list has repeat value, insort_left and insort_right will insert num in different position.
   2. `bisect(list, num)`, `bisect_left(list, num)` and `bisect_right(list, num)`: find the location where the value will be inserted and return without inserting.
