# Max Consequitve Ones Variant

## Problem Description

Given a binary array nums, find the maximum length of a consecutive subarray consisting only of 1s after removing exactly one element (either 0 or 1).

**Example 1:**  

* Input: `[0, 0]`  
* Output: `0`
* Explanation: Removing any element leaves `[0]` (no `1`s).

**Example 2:**  

* Input: `[0, 1]`  
* Output: `1` 
* Explanation: Remove `0`: `[1]` → sequence of `1` has length `1`.

**Constraints:**

* `1 <= len(nums) <= 10^5`
* `nums[i]` is `0` or `1`

## Solution

```python
def max_ones_after_remove_one(nums: list[int]) -> int:
    left = 0

    zero_position = -1
    zero_counter = 0
    max_counter = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            if zero_counter == 1:
                left = zero_position + 1
                zero_counter -= 1
            zero_counter += 1
            zero_position = right
        max_counter = max(max_counter, right - left + 1 - zero_counter)

    return max_counter
```

* **Time Complexity:** O(n). The algorithm processes each element exactly once.
* **Space Complexity:** O(1), as only a few variables are used for tracking.

## Explanation of the Solution

The problem requires finding the maximum length of a consecutive subarray consisting only of 1s after removing exactly one element (either `0` or `1`) from the original array. The solution uses a sliding window approach to efficiently track the longest valid subarray.
Key Ideas:

1. **Sliding Window with At Most One Zero:**
   * The window `[left, right]` can contain at most one `0`. If a second `0` is encountered, the window is adjusted to exclude the first `0`.
   * This ensures that after removing one `0`, the remaining subarray consists of all 1s.
2. **Tracking Zero Position:**
   * `zero_position` keeps track of the index of the most recent `0` encountered.
   * `zero_counter` counts the number of `0`s in the current window (either `0` or `1`).
3. **Window Adjustment:**
   * If a new `0` is encountered when `zero_counter == 1`, the left boundary of the window (left) is moved to `zero_position + 1` (skipping the first `0`).
   * This allows the window to include the new `0` while maintaining at most one `0` in the window.
4.  **Calculating Maximum Length:**
	* The length of the current valid subarray is `right - left + 1 - zero_counter`. Since `zero_counter` is at most `1`, subtracting it accounts for the one allowed removal.
	* The maximum length encountered during the iteration is stored in `max_counter`.

