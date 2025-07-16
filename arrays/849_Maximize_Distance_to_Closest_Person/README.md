# Maximize Distance to Closest Person

## Problem Description

You are given an array representing a row of seats where `seats[i] = 1` 
represents a person sitting in the `i`th seat, and `seats[i] = 0` represents 
that the `i`th seat is empty (0-indexed).

There is at least one empty seat, and at least one person sitting.

Alex wants to sit in the seat such that the distance between him and the 
closest person to him is maximized. 

Return that maximum distance to the closest person.

**Example 1:**

* Input: `seats = [1, 0, 0, 0, 1, 0, 1]`
* Output: `2`
* Explanation: 

  If Alex sits in the second open seat (i.e. `seats[2]`), then the closest person 
  has distance 2.
  If Alex sits in any other open seat, the closest person has distance 1.
  Thus, the maximum distance to the closest person is 2.

**Example 2:**

* Input: `seats = [1, 0, 0, 0]`
* Output: `3`
* Explanation: 

  If Alex sits in the last seat (i.e. `seats[3]`), the closest person is 3 seats away.
  This is the maximum distance possible, so the answer is 3.

**Example 3:**

* Input: `seats = [0, 1]`
* Output: `1`

**Constraints:**

* `2 <= seats.length <= 2 * 10^4`
* `seats[i]` is `0` or `1`.
* At least one seat is empty.
* At least one seat is occupied.


## Solution

```python
def max_dist_to_closest(seats: list[int]) -> int:
    """
    Calculate the maximum distance to the closest occupied seat in a row.

    The function finds the maximum possible distance a person can have to the nearest
    occupied seat when choosing a seat in a row represented by a binary list,
    where 1 represents an occupied seat and 0 represents an empty seat.

    :param seats: A list of integers where 0 represents an empty seat and 1 represents
    an occupied seat. The list must contain at least one occupied seat.
    :return: The maximum distance to the closest occupied seat. The distance is measured
    as the number of seats between two positions (inclusive of endpoints).
    """
    length = len(seats)
    left = None
    result = 1

    for index in range(length):
        if seats[index] == 0:
            if left is None:
                left = index
            if (left == 0) or (index == length - 1):
                result = max(result, index - left + 1)
            else:
                result = max(result, (index - left + 2) // 2)
        else:
            left = None
    return result
```

* **Time Complexity:** $O(n)$
* **Space Complexity:** $O(1)$

## Explanation of the Solution

### Key Insights

1. **Empty Seats Between Occupied Seats:**
   * The optimal position is the middle of the longest block of empty seats between two 1s.
2. **Edge Cases:**
   * If the first or last seat is empty, the farthest position is at that edge (no need to sit in the middle). 

### Approach

1. **Track Empty Seat Blocks Efficiently:**
   * Use a single pointer left to mark the start of a block of empty seats.
   * If the block touches the start (`left=0`) or end (`index=last seat`) of the row, the distance is the full block length `(index - left + 1)`.
   * For internal blocks, the maximum distance is `(index - left + 2) // 2` (middle position).
2. **Update Result Dynamically:**
   * When encountering an occupied seat (`1`), reset `left` to `None` (indicating no current empty block).
   * For empty seats (`0`), update left if starting a new block, then compute the current maximum distance.