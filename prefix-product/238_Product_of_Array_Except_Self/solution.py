def product_except_self(nums: list[int]) -> list[int]:
    """
    Computes for each element the product of all other elements in the array.

    :param nums: Input array of integers. May contain negatives and zeros.
    :return: Array where output[i] = product of all elements except nums[i]
    """

    length = len(nums)
    left_prefix = [1] * length
    right_prefix = [1] * length

    for index in range(length - 1):
        left_prefix[index + 1] *= nums[index] * left_prefix[index]

    for index in range(length - 1, 0, -1):
        right_prefix[index - 1] *= nums[index] * right_prefix[index]

    return [l * r for l, r in zip(left_prefix, right_prefix)]


assert product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6], 'Test 1 failed'
assert product_except_self([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0], 'Test 2 failed'
