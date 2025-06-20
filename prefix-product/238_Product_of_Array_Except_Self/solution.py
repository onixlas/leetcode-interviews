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


assert product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6], 'Test 1 failed'
assert product_except_self([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0], 'Test 2 failed'
