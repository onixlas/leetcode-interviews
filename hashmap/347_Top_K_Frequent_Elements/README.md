# Top K Frequent Elements

## Problem Description

Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. 
You may return the answer in any order.

**Example 1:**

* Input: `nums = [1, 1, 1, 2, 2, 3], k = 2`
* Output: `[1, 2]`

**Example 2:**

* Input: `nums = [1], k = 1`
* Output: `[1]`

**Constraints:**


* $1$ `<= nums.length <=` $10^5$
* $-10^4$ `<= nums[i] <=` $10^4$
* `k` is in the range [1, the number of unique elements in the array].
* It is guaranteed that the answer is unique.

## Solution

```python
def top_k_frequent(nums: list[int], k: int) -> list[int]:
    """Returns the `k` most frequent elements from the input list.

    :param nums: A list of integers where frequencies need to be counted.
    :param k: The number of top frequent elements to return (must be <= unique elements in `nums`).
    :return: A list of the `k` most frequent elements.
    """
    nums_hash = {}
    for num in nums:
        if num in nums_hash:
            nums_hash[num] += 1
        else:
            nums_hash[num] = 1

    return sorted(nums_hash, key=lambda x: nums_hash[x], reverse=True)[:k]
```

* **Time Complexity:** $O(n \cdot log(n))$
* **Space Complexity:** $O(n)$

## Explanation of the Solution

1. Count Frequencies:
    * A dictionary `nums_hash` is used to store each number’s frequency in nums.
    * For each number in nums:
        * If the number exists in `nums_hash`, increment its count by 1.
        * If the number does not exist, add it to `nums_hash` with a count of 1.
2. Sort by Frequency:
    * The dictionary keys (unique numbers) are sorted in descending order based on their frequency (`nums_hash[x]`).
    * `reverse=True` ensures higher frequencies appear first.
3. Select Top k Elements:
    * The first `k` elements from the sorted list are returned.
