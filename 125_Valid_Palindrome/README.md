# Valid Palindrome

## Problem Description
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string `s`, return `True` if it is a palindrome, or `False` otherwise.

**Example 1:**  
Input: `s = "A man, a plan, a canal: Panama"`  
Output: `true`  
Explanation: "amanaplanacanalpanama" is a valid palindrome.

**Example 2:**  
Input: `s = "race a car"`  
Output: `false`  
Explanation: "raceacar" is not a palindrome.

## Solutions

### Solution 1: String Comparison

```python
def is_palindrome(s: str) -> bool:
    s = ''.join([char.lower() for char in s if char.isalnum()])
    return s == s[::-1]
```

* **Time Complexity:** O(n)
  * Linear pass to filter/convert characters
  * O(n) string reversal comparison

* **Space Complexity:** O(n)
  * Stores cleaned version of input string

### Solution 2: Two Pointers (In-Place)

```pethon
def is_palindrome2(s: str) -> bool:
    left = 0
    right = len(s) - 1

    while left < right:
        while (left < right) and not s[left].isalnum():
            left += 1
        while (left < right) and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True
```

* **Time Complexity:** O(n)
  * Each character processed at most twice (once per pointer)
* **Space Complexity:** O(1)
  * Operates directly on input with pointer variables

### Implementation Notes for Two-Pointer Solution

* **Case Conversion is Critical**

    Always convert compared characters to lowercase using .lower() before comparison.
    Example: 'A' vs 'a' should be treated as equal.
* **Update Pointers After Comparison**

    Remember to increment left and decrement right at the end of the loop.
    Failure to update pointers causes infinite loops.