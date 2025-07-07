# Ransom Note

## Problem Description

Given two strings `ransomNote` and `magazine`, return `true` if `ransomNote` can be constructed by using the letters from `magazine` and `false` otherwise.

Each letter in `magazine` can only be used once in `ransomNote`.

**Example 1:**

* Input: `ransomNote = "a"`, `magazine = "b"`
* Output: `false`

**Example 2:**

* Input: `ransomNote = "aa"`, `magazine = "ab"`
* Output: `false`

**Example 3:**

* Input: `ransomNote = "aa"`, `magazine = "aab"`
* Output: ``true`

**Constraints:**

* `1 <= ransomNote.length, magazine.length <= 105`
* `ransomNote` and `magazine` consist of lowercase English letters.

## Solution

```python
def can_construct(self, ransom_note: str, magazine: str) -> bool:
    """
    Check if the `ransom_note` can be constructed from the letters of `magazine`.

    Each letter in `magazine` can only be used once in `ransom_note`. The function determines
    if there are enough characters in `magazine` to form the `ransom_note` (considering character counts).

    :param self: Instance reference (used if this is a method in a class).
    :param ransom_note: String that needs to be constructed.
    :param magazine: String containing available characters.
    :return: True if `ransom_note` can be constructed from `magazine`, False otherwise.
    """
    hashmap = {}
    for character in magazine:
        if character not in hashmap:
            hashmap[character] = 1
        else:
            hashmap[character] += 1
    for character in ransom_note:
        if character not in hashmap or hashmap[character] == 0:
            return False
        else:
            hashmap[character] -= 1
    return True
```

* **Time Complexity:** $O(m + n)$
* **Space Complexity:** $O(1)$

## Explanation of the Solution

Step-by-Step Breakdown:

1. Count Characters in magazine:

    * A hashmap (dictionary) is used to store the count of each character in magazine.
    * For each character in magazine:
      * If the character is not in the hashmap, add it with a count of 1.
      * If the character exists, increment its count by 1.

    **Example:**
    `magazine = "aab"` → `hashmap = {'a': 2, 'b': 1}`

2. Check Characters in ransom_note:
   * For each character in ransom_note:
        * If the character is missing in the hashmap or its count is 0, return False (cannot construct the note).
        * Otherwise, decrement the count of that character in the hashmap (to mark it as "used").
3. Return True if All Checks Pass:
   * If the loop completes without issues, ransom_note can be constructed → Return True.