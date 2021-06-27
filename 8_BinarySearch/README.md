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
