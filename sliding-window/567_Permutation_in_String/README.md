# Permutation in String

## Problem Description

Given two strings `s1` and `s2`, return `true` if `s2` contains a permutation of `s1`,
or `false` otherwise.

In other words, return `true` if one of `s1`'s permutations is the substring of `s2`.

**Example 1:**

* Input: `s1 = "ab", s2 = "eidbaooo"`
* Output: `true`
* Explanation: `s2` contains one permutation of `s1` (`"ba"`).

**Example 2:**

* Input: `s1 = "ab", s2 = "eidboaoo"`
* Output: `false`

**Constraints:**

* `1 <= s1.length, s2.length <= 10^4`
* `s1` and `s2` consist of lowercase English letters.

## Solution

```python
def check_inclusion(s1: str, s2: str) -> bool:
    """
    Check if any permutation of s1 exists as a substring in s2.

    This function uses a sliding window approach with hash maps to efficiently
    track character counts and determine if any permutation of s1 is present in s2.

    :param s1: The string whose permutations we want to find in s2.
    :param s2: The string in which we're searching for permutations of s1.
    :return: True if any permutation of s1 is found as a substring in s2, False otherwise.
    """
    pattern_hash = {}
    for character in s1:
        if character not in pattern_hash:
            pattern_hash[character] = 1
        else:
            pattern_hash[character] += 1

    hash_copy = pattern_hash.copy()
    pattern_length = len(s1)

    for index in range(len(s2)):
        if index >= pattern_length:
            outgoing_character = s2[index - pattern_length]
            if outgoing_character in pattern_hash:
                if outgoing_character not in hash_copy:
                    hash_copy[outgoing_character] = 1
                else:
                    hash_copy[outgoing_character] += 1
                if hash_copy[outgoing_character] == 0:
                    del hash_copy[outgoing_character]

        incoming_character = s2[index]
        if incoming_character in pattern_hash:
            if incoming_character in hash_copy:
                hash_copy[incoming_character] -= 1
            else:
                hash_copy[incoming_character] = -1
            if hash_copy[incoming_character] == 0:
                del hash_copy[incoming_character]
            if len(hash_copy) == 0:
                return True
    return False
```

* **Time Complexity:** $O(n)$
* **Space Complexity:** $O(1)$

## Explanation of the Solution

The problem reduces to finding a window in `s2` where the character frequency exactly matches that of `s1` 
(regardless of order). This is equivalent to checking for an anagram of `s1` in `s2`.

1. Frequency Map for s1 (pattern_hash)
    * Create a hash map counting occurrences of each character in `s1`.
2. Sliding Window over s2
    * Traverse `s2` while maintaining a dynamically adjusted window of size `len(s1)`.
    * Use a copy of `pattern_hash` (`hash_copy`) to track how much the current window deviates from `s1`'s frequencies.
        * Goal: `hash_copy` becomes empty when the window matches `s1`'s frequencies.
3. Window Adjustment Logic
    * For each new character (incoming_character):
        * If it exists in `pattern_hash`, decrement its count in `hash_copy`.
        * If a count reaches 0, remove the key (indicates balance with `s1`).
    * For the character exiting the window (outgoing_character):
        * Re-increment its count in `hash_copy` (reversing the earlier decrement).
        * Remove the key if the count rebalances to 0.
4. Check for Permutation
    * If `hash_copy` is ever empty, the current window is a permutation of `s1` → return `True`.
    * If the loop ends without finding such a window → return `False`.