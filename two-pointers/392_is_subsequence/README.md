# Is Subsequence

## Problem Description

Given two strings `s` and `t`, return `true` if `s` is a subsequence of `t`, or `false` otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., `"ace"` is a subsequence of `"abcde"` while `"aec"` is not).

**Example 1:**

Input: `s = "abc"`, `t = "ahbgdc"`
Output: `true`

**Example 2:**

Input: `s = "axc"`, `t = "ahbgdc"`
Output: `false`

**Constraints:**

* `0 <= s.length <= 100`
* `0 <= t.length <= 10^4`
* `s` and `t` consist only of lowercase English letters.

## Solution

```python
def is_subsequence(self, s: str, t: str) -> bool:
    """
    Check if string `s` is a subsequence of string `t`.

    A subsequence is a sequence that can be derived from another sequence by deleting zero or more elements
    without changing the order of the remaining elements.

    :param self: The instance reference (for method implementation)
    :param s: The potential subsequence string to check
    :param t: The string in which to search for the subsequence
    :return: True if `s` is a subsequence of `t`, False otherwise
    """
    s_pointer = 0
    s_length = len(s)

    if not s_length:
        return True

    for t_pointer in range(len(t)):
        if s[s_pointer] == t[t_pointer]:
            s_pointer += 1
        if s_pointer == s_length:
            return True

    return False
```

* **Time Complexity:** $O(n)$
* **Space Complexity:** $O(1)$
