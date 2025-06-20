def top_k_frequent(nums: list[int], k: int) -> list[int]:
    """Returns the `k` most frequent elements from the input list.

    :param nums: A list of integers where frequencies need to be counted.
    :param k: The number of top frequent elements to return (must be <= unique elements in `nums`).
    :return: A list of the `k` most frequent elements.
    """
    nums_hash = {}
    for num in nums:
        if num in nums_hash:
            nums_hash[num] += 1
        else:
            nums_hash[num] = 1

    return sorted(nums_hash, key=lambda x: nums_hash[x], reverse=True)[:k]

assert top_k_frequent([1,1,1,2,2,3], 2) == [1, 2], 'Test 1 Failed'
assert top_k_frequent([1], 1) == [1], 'Test 2 Failed'
