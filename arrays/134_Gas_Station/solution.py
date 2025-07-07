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

assert can_complete_circuit(gas=[1, 2, 3, 4, 5], cost=[3, 4, 5, 1, 2]) == 3, 'Test 1 Failed'
assert can_complete_circuit(gas=[2, 3, 4], cost=[3, 4, 3]) == -1, 'Test 2 Failed'
assert can_complete_circuit(gas=[5, 1, 2, 3, 4], cost=[4, 4, 1, 5, 1]) == 4, 'Test 3 Failed'
assert can_complete_circuit(gas=[3, 1, 1], cost=[1, 2, 2]) == 0, 'Test 4 Failed'
assert can_complete_circuit(gas=[1, 2, 3, 4, 5, 5, 70], cost=[2, 3, 4, 3, 9, 6, 2]) == 6, 'Test 5 Failed'