# Minimum Size Subarray Sum

## Problem Description

Given an array of positive integers nums and a positive integer target, return the 
minimal length of a subarray whose sum is greater than or equal to `target`. 
If there is no such subarray, return `0` instead.

**Example 1:**

* Input: `target = 7`, nums = `[2,3,1,2,4,3]`
* Output: `2`
* Explanation: The subarray `[4,3]` has the minimal length under the problem constraint.

**Example 2:**

* Input: `target = 4`, `nums = [1,4,4]`
* Output: `1`

**Example 3:**

* Input: `target = 11`, `nums = [1,1,1,1,1,1,1,1]`
* Output: `0`

Constraints:

* `1 <= target <= 109`
* `1 <= nums.length <= 105`
* `1 <= nums[i] <= 104`


## Solution

```python
def min_sub_array_len(target: int, nums: list[int]) -> int:
    """
    Finds the minimal length of a contiguous subarray of which the sum is greater than or equal to the target.
    If there is no such subarray, returns 0.

    :param target: The target sum to achieve.
    :param nums: List of integers representing the array.
    :return: The minimal length of the subarray, or 0 if no such subarray exists.
    """
    first_pointer = 0
    current_sum = 0
    min_len = float('inf')

    for second_pointer in range(len(nums)):
        current_sum += nums[second_pointer]

        while current_sum >= target:
            min_len = min(min_len, second_pointer - first_pointer + 1)
            current_sum -= nums[first_pointer]
            first_pointer += 1

    return min_len if min_len != float('inf') else 0
```

* **Time Complexity:** $O(n)$
* **Space Complexity:** $O(1)$

## Explanation of the Solution

The algorithm efficiently tracks a "window" of elements in the array using two pointers 
(`first_pointer` and `second_pointer`). The window expands and contracts dynamically to 
find the smallest valid subarray.

1. Initialization
    * `first_pointer = 0` (marks the start of the current window)
    * `current_sum = 0` (stores the sum of elements in the current window)
    * `min_len = ∞` (tracks the smallest valid window length found so far)
2. Expand the Window (Move second_pointer)
    * Iterate through nums using second_pointer (from `0` to `len(nums)-1`).
    * Add `nums[second_pointer]` to `current_sum`.
3. Check if the Window Sum ≥ Target
    * If `current_sum >= target`, it means the current window (`[first_pointer ... second_pointer]`) is a valid subarray.
    * Update `min_len` to the smaller of:
      * Current `min_len`
      * Length of the current window (`second_pointer - first_pointer + 1`)
4. Contract the Window (Move `first_pointer`)
    *  While `current_sum >= target`:
      * Remove `nums[first_pointer]` from `current_sum` (shrinking the window from the left).
      * Move `first_pointer` forward.
    * This ensures we find the smallest possible valid window ending at `second_pointer``.
5. Repeat Until the End of the Array
    * Continue expanding (`second_pointer++`) and contracting (`first_pointer++`) until all possible windows are checked.
6. Return the Result
    * If a valid subarray was found (`min_len` is not ∞), return `min_len`.
    * Otherwise, return `0`.

