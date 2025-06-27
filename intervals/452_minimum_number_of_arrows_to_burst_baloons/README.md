# Minimum Number of Arrows to Burst Baloons

## Problem Description

There are some spherical balloons taped onto a flat wall that represents the XY-plane. 
The balloons are represented as a 2D integer array points where 
`points[i] = [xstart, xend]` denotes a balloon whose horizontal diameter 
stretches between `xstart` and `xend`. You do not know the exact y-coordinates 
of the balloons.

Arrows can be shot up directly vertically (in the positive y-direction) 
from different points along the x-axis. A balloon with `xstart` and `xend` 
is burst by an arrow shot at x if `xstart <= x <= xend`. There is no limit 
to the number of arrows that can be shot. A shot arrow keeps traveling up 
infinitely, bursting any balloons in its path.

Given the array points, return the minimum number of arrows that must be shot 
to burst all balloons.

**Example 1:**

Input: `points = [[10,16],[2,8],[1,6],[7,12]]`
Output: `2`
Explanation: The balloons can be burst by 2 arrows:
- Shoot an arrow at `x = 6`, bursting the balloons `[2,8]` and `[1,6]`.
- Shoot an arrow at `x = 11`, bursting the balloons `[10,16]` and `[7,12]`.

**Example 2:**

Input: `points = [[1,2],[3,4],[5,6],[7,8]]`
Output: `4`
Explanation: One arrow needs to be shot for each balloon for a total of `4` arrows.

**Example 3:**

Input: `points = [[1,2],[2,3],[3,4],[4,5]]`
Output: `2`
Explanation: The balloons can be burst by 2 arrows:
- Shoot an arrow at `x = 2`, bursting the balloons `[1,2]` and `[2,3]`.
- Shoot an arrow at `x = 4`, bursting the balloons `[3,4]` and `[4,5]`.

**Constraints:**

* `1 <= points.length <= 105`
* `points[i].length == 2`
* `-231 <= xstart < xend <= 231 - 1`




## Solution

```python
def find_min_arrow_shots(points: list[list[int]]) -> int:
    """
    Calculate the minimum number of arrows needed to burst all balloons.

    The balloons are represented as intervals on a 2D plane (start and end points).
    An arrow shot at x-coordinate x bursts all balloons whose interval includes x.
    The function uses a greedy algorithm to find the optimal shooting points.

    :param points: A list of balloon intervals, where each interval is represented as [start, end]
    :return: The minimum number of arrows required to burst all balloons
    """
    points.sort(key=lambda x: x[1])

    shots = 1
    current_point = points[0]

    for point in points:
        if point[0] > current_point[1]:
            shots += 1
            current_point = point
    return shots
```

* **Time Complexity:** $O(n\cdot log(n)$
* **Space Complexity:** $O(n)$

## Explanation of the Solution

1. Sort Balloons by End Points
    * First, we sort all balloons based on their end coordinates in ascending order.
    * Why? This allows us to process balloons in an order where we can greedily select the earliest possible "burst point."
2. Initialize Variables
    * `shots = 1` (we need at least one arrow).
    * `current_end = points[0][1]` (the end of the first balloon).

3. Greedy Arrow Placement
    * Iterate through each balloon in the sorted list:
        * If the start of the current balloon > current end:
          * This means the balloon cannot be burst by the previous arrow.
          * We increment shots (a new arrow is needed).
          * Update current_end to the end of this new balloon.
        * Else:
          * The current balloon can be burst by the same arrow (since intervals overlap).

4. Return the Result
    * The variable shots now holds the minimum number of arrows needed.

