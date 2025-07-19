# Time and Space Complexity Analysis

## Why Complexity Analysis Matters

Understanding how your algorithms perform is crucial for:
- **Scalability**: Will your solution work with large inputs?
- **Efficiency**: Is there a better approach?
- **Interview Success**: Essential for technical interviews

## Big O Notation

Big O describes the **worst-case** performance of an algorithm as input size grows.

### Common Time Complexities (Best to Worst)

1. **O(1) - Constant**: Always takes the same time
   ```python
   def get_first_element(arr):
       return arr[0]  # Always one operation
   ```

2. **O(log n) - Logarithmic**: Divides problem in half each step
   ```python
   def binary_search(arr, target):
       left, right = 0, len(arr) - 1
       while left <= right:
           mid = (left + right) // 2
           if arr[mid] == target:
               return mid
           elif arr[mid] < target:
               left = mid + 1
           else:
               right = mid - 1
       return -1
   ```

3. **O(n) - Linear**: Processes each element once
   ```python
   def find_max(arr):
       max_val = arr[0]
       for num in arr:  # n operations
           if num > max_val:
               max_val = num
       return max_val
   ```

4. **O(n log n) - Linearithmic**: Efficient sorting algorithms
   ```python
   def merge_sort(arr):
       if len(arr) <= 1:
           return arr
       mid = len(arr) // 2
       left = merge_sort(arr[:mid])
       right = merge_sort(arr[mid:])
       return merge(left, right)
   ```

5. **O(n²) - Quadratic**: Nested loops over input
   ```python
   def bubble_sort(arr):
       n = len(arr)
       for i in range(n):      # n operations
           for j in range(n-1-i):  # n operations each
               if arr[j] > arr[j+1]:
                   arr[j], arr[j+1] = arr[j+1], arr[j]
   ```

6. **O(2ⁿ) - Exponential**: Recursive problems without memoization
   ```python
   def fibonacci_naive(n):
       if n <= 1:
           return n
       return fibonacci_naive(n-1) + fibonacci_naive(n-2)
   ```

## Space Complexity

Space complexity measures additional memory used by algorithm.

### Examples

**O(1) Space - Constant**:
```python
def reverse_string(s):
    left, right = 0, len(s) - 1
    s = list(s)
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return ''.join(s)
```

**O(n) Space - Linear**:
```python
def fibonacci_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)
    return memo[n]
```

## Analysis Framework

### 4-Step Process:

1. **Identify the input size**: What is 'n'?
2. **Count basic operations**: Loops, comparisons, assignments
3. **Express as function of n**: How many operations for input size n?
4. **Find the dominant term**: Drop constants and lower-order terms

### Example Analysis:
```python
def example_function(arr):
    n = len(arr)
    
    # Step 1: O(1)
    max_val = arr[0]
    
    # Step 2: O(n)
    for i in range(n):
        if arr[i] > max_val:
            max_val = arr[i]
    
    # Step 3: O(n²)
    for i in range(n):
        for j in range(n):
            print(arr[i], arr[j])
    
    return max_val

# Total: O(1) + O(n) + O(n²) = O(n²)
```

## Common Patterns

### Array/String Operations:
- **Access by index**: O(1)
- **Search unsorted**: O(n)
- **Search sorted**: O(log n) with binary search
- **Insert at end**: O(1) amortized
- **Insert at beginning**: O(n)

### Hash Table Operations:
- **Search/Insert/Delete**: O(1) average, O(n) worst case

### Tree Operations:
- **Balanced tree search**: O(log n)
- **Unbalanced tree search**: O(n) worst case

## Practice Problems

1. What's the time complexity of checking if array has duplicates?
2. Optimize the naive Fibonacci to O(n) time and O(1) space
3. How would you find the kth largest element efficiently?

Remember: **Premature optimization is the root of all evil, but understanding complexity is essential!**