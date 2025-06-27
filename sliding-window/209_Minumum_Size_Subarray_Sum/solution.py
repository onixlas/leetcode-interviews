def min_sub_array_len(target: int, nums: list[int]) -> int:
    """
    Finds the minimal length of a contiguous subarray of which the sum is greater than or equal to the target.
    If there is no such subarray, returns 0.

    :param target: The target sum to achieve.
    :param nums: List of integers representing the array.
    :return: The minimal length of the subarray, or 0 if no such subarray exists.
    """
    first_pointer = 0
    current_sum = 0
    min_len = float('inf')

    for second_pointer in range(len(nums)):
        current_sum += nums[second_pointer]

        while current_sum >= target:
            min_len = min(min_len, second_pointer - first_pointer + 1)
            current_sum -= nums[first_pointer]
            first_pointer += 1

    return min_len if min_len != float('inf') else 0

assert min_sub_array_len(target=7, nums=[2,3,1,2,4,3]) == 2, 'Test 1 Failed'
assert min_sub_array_len(target=4, nums=[1,4,4]) == 1, 'Test 2 Failed'
assert min_sub_array_len(target=11, nums=[1,1,1,1,1,1,1,1]) == 0, 'Test 3 Failed'
assert min_sub_array_len(target=11, nums=[1,2,3,4,5]) == 3, 'Test 4 Failed'
assert min_sub_array_len(target=15, nums=[1,2,3,4,5]) == 5, 'Test 5 Failed'