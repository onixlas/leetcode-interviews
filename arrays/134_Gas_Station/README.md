# Gas Station

## Problem Description

There are n gas stations along a circular route, where the amount of gas at the ith station is `gas[i]`.

You have a car with an unlimited gas tank and it costs `cost[i]` of gas to travel from the `i`th station 
to its next `(i + 1)`th station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays `gas` and `cost`, return the starting gas station's index if you can travel 
around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, 
it is guaranteed to be unique.

**Example 1:**

* Input: `gas = [1,2,3,4,5], cost = [3,4,5,1,2]`
* Output: `3`
* Explanation:
  * Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
  * Travel to station 4. Your tank = 4 - 1 + 5 = 8
  * Travel to station 0. Your tank = 8 - 2 + 1 = 7
  * Travel to station 1. Your tank = 7 - 3 + 2 = 6
  * Travel to station 2. Your tank = 6 - 4 + 3 = 5
  * Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
  * Therefore, return 3 as the starting index.

**Example 2:**

* Input: `gas = [2,3,4], cost = [3,4,3]`
* Output: `-1`
* Explanation:
  * You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
  * Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
  * Travel to station 0. Your tank = 4 - 3 + 2 = 3
  * Travel to station 1. Your tank = 3 - 3 + 3 = 3
  * You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
  * Therefore, you can't travel around the circuit once no matter where you start.

**Constraints:**


* `n == gas.length == cost.length`
* `1 <= n <= 10^5`
* `0 <= gas[i], cost[i] <= 10^4`
* The input is generated such that the answer is unique.


## Solution

```python
def can_complete_circuit(gas: list[int], cost: list[int]) -> int:
    """
    Determine the starting gas station's index to travel around a circular route once.

    The car starts with an empty tank at one of the gas stations and has an unlimited gas capacity.
    It must be able to travel clockwise around all stations, refueling at each, without running out of gas.

    :param gas: A list of integers where gas[i] represents the amount of gas at station i.
    :param cost: A list of integers where cost[i] represents the gas cost to travel from station i to i+1.
    :return: The index of the starting gas station if the circuit can be completed, otherwise -1.
    """
    if sum(gas) < sum(cost):
        return -1
    length = len(gas)
    current_tank = 0
    start = -1
    for index in range(length):
        current_tank += gas[index] - cost[index]
        if current_tank < 0:
            start = -1
            current_tank = 0
        elif start == -1:
            start = index
    return start
```

* **Time Complexity:** $O(n)$
* **Space Complexity:** $O(1)$

## Explanation of the Solution

This problem involves finding a starting gas station in a circular route such that a car can travel 
around all stations without running out of gas. The solution efficiently checks for the valid starting 
point using a greedy approach with cumulative gas tracking.

1. Early Termination Check:
    * If total gas is insufficient, return `-1` immediately.
2. Initialize Variables:
    * `current_tank = 0` → Tracks gas balance during the journey.
    * `start = -1` → Stores the candidate starting station.
3. Iterate Through Stations:
    * For each station `i`, update `current_tank += gas[i] - cost[i]` (gas added minus gas spent).
    * If `current_tank < 0`:
      * The current candidate station (`start`) is invalid.
      * Reset `current_tank = 0` and mark `start = -1` (search for a new candidate).
    * If `current_tank >= 0` and no candidate is set (`start == -1`):
      * Set `start = i` (this station is a potential starting point).
4. Return the Valid Start:
    * After the loop, start holds the unique valid station (since `sum(gas) >= sum(cost)` guarantees a solution).

By resetting `current_tank` when it goes negative, we ensure the candidate station can cover all subsequent stations 
without deficits.

The loop checks stations in order, and the `sum(gas) >= sum(cost)` condition ensures the remaining stations (after the 
candidate) can compensate for any prior deficits.