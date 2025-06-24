# Majority Element

## Problem Description

Given an array nums of size `n`, return *the majority element.*

The majority element is the element that appears more than `⌊n / 2⌋` times. You may assume that the majority element always exists in the array.

**Example 1:**

Input: `nums = [3,2,3]`
Output: `3`

**Example 2:**

Input: `[2,2,1,1,1,2,2]`
Output: `2`

**Constraints:**


* `n == nums.length`
* `1 <= n <= 5 * 10^4`
* `-10^9 <= nums[i] <= 10^9`

## Solution

```python
def majority_element(nums: list[int]) -> int:
    """Finds the majority element in a list of integers.

    The majority element is the element that appears more than ⌊n / 2⌋ times,
    where n is the size of the array. It is assumed that the majority element always exists.

    :param nums: A list of integers where the majority element is to be found.
    :return: The majority element in the list.
    """

    counter = 1
    current_majority_element = nums[0]

    for num in nums[1:]:
        if current_majority_element != num:
            if counter:
                counter -= 1
            if counter == 0:
                current_majority_element = num
                counter = 1
        else:
            counter += 1

    return current_majority_element
```

* **Time Complexity:** $O(n)$
* **Space Complexity:** $O(1)$

## Explanation of the Solution

Intuition:

* The majority element occurs more than all other elements combined.
* We can "pair" each occurrence of the majority element with a different element and cancel them out. The remaining element will be the majority.
* The majority element appears more than n/2 times, so even if it gets "canceled" occasionally, it will still have votes remaining at the end.

### Implementation Notes

* Don't forget to start the cycle with `nums[1:]` or use `current_majority_element` at the beginning.