def max_ones_after_remove_one(nums: list[int]) -> int:
    """
    Finds the maximum length of a consecutive subarray of 1s after removing exactly one element (0 or 1).

    :param nums: A list of integers containing only 0s and 1s.
    :return: The maximum length of consecutive 1s achievable by deleting exactly one element from the list.
    """
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


assert max_ones_after_remove_one([0, 0]) == 0, 'Test 1 failed'
assert max_ones_after_remove_one([0, 1]) == 1, 'Test 2 failed'
assert max_ones_after_remove_one([1, 0, 1]) == 2, 'Test 3 failed'
assert max_ones_after_remove_one([1, 1, 1]) == 3, 'Test 4 failed'
assert max_ones_after_remove_one([1, 1, 0, 1, 1]) == 4, 'Test 5 failed'
assert max_ones_after_remove_one([1, 1, 1, 0, 1, 1, 0]) == 5, 'Test 6 failed'
assert max_ones_after_remove_one([1, 1, 0, 1, 0, 1]) == 3, 'Test 7 failed'
assert max_ones_after_remove_one([1, 1, 0, 0, 1, 0, 1]) == 2, 'Test 8 failed'
assert max_ones_after_remove_one([1, 0, 1, 0, 1, 1, 1]) == 4, 'Test 9 failed'
assert max_ones_after_remove_one([0, 0, 0, 0]) == 0, 'Test 10 failed'
assert max_ones_after_remove_one([1, 0, 1, 1, 0]) == 3, 'Test 11 failed'
