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


assert majority_element(nums=[3,2,3]) == 3, 'Test 1 failed'
assert majority_element(nums=[2,2,1,1,1,2,2]) == 2, 'Test 2 failed'
assert majority_element(nums=[6,5,5]) == 5, 'Test 3 failed'