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
    right = None
    result = 1

    for index in range(length):
        if seats[index] == 0:
            if left is None:
                left = index
            right = index
            if (left == 0) or (right == length - 1):
                result = max(result, right - left + 1)
            else:
                result = max(result, (right - left + 2) // 2)
        else:
            left = None
            right = None
    return result


assert max_dist_to_closest(seats=[1, 0, 0, 0, 1, 0, 1]) == 2, 'Test 1 Failed'
assert max_dist_to_closest(seats=[1, 0, 0, 0]) == 3, 'Test 2 Failed'
assert max_dist_to_closest(seats=[0, 1]) == 1, 'Test 3 Failed'
