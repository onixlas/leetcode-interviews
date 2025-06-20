# Product of Array Except Self

## Problem Description

Given an integer array nums, return an array answer such that `answer[i]` is equal to the product of all the elements of 
`nums` except `nums[i]`.

The product of any prefix or suffix of `nums` is guaranteed to fit 
in a 32-bit integer.

You must write an algorithm that runs in `O(n)` time and 
without using the division operation.

**Example 1:**

Input: `nums = [1,2,3,4]`
Output: `[24,12,8,6]`

**Example 2:**

Input: `nums = [-1,1,0,-3,3]`
Output: `[0,0,9,0,0]`

**Constraints:**

* `2 <= nums.length <= 105`
* `-30 <= nums[i] <= 30`
* The input is generated such that `answer[i]` is guaranteed to fit in a 32-bit integer.

## Solution

```python
def product_except_self(nums: list[int]) -> list[int]:
    """
    Computes for each element the product of all other elements in the array.

    :param nums: Input array of integers. May contain negatives and zeros.
    :return: Array where output[i] = product of all elements except nums[i]
    """

    length = len(nums)
    left = 1
    right = 1
    output = [1] * length

    for index in range(length - 1):
        left *= nums[index]
        output[index + 1] *= left

    for index in range(length - 1, 0, -1):
        right *= nums[index]
        output[index - 1] *= right

    return output
```

* **Time Complexity:** O(n)
  * Each number processed only twice
* **Space Complexity:** O(1)
  * Only constant space required (excluding the output array)

## Explanation of the Solution

* Edge Elements:
    * The first element (output[0]) is updated only during the backward pass (product of all elements to its right).
    * The last element (output[length - 1]) is updated only during the forward pass (product of all elements to its left).
* Middle Elements:
  * Each middle element output[i] is the product of:
  * Elements to its left (computed in the forward pass).
  * Elements to its right (computed in the backward pass).