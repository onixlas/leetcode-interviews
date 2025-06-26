def is_subsequence(self, s: str, t: str) -> bool:
    """
    Check if string `s` is a subsequence of string `t`.

    A subsequence is a sequence that can be derived from another sequence by deleting zero or more elements
    without changing the order of the remaining elements.

    :param self: The instance reference (for method implementation)
    :param s: The potential subsequence string to check
    :param t: The string in which to search for the subsequence
    :return: True if `s` is a subsequence of `t`, False otherwise
    """
    s_pointer = 0
    s_length = len(s)

    if not s_length:
        return True

    for t_pointer in range(len(t)):
        if s[s_pointer] == t[t_pointer]:
            s_pointer += 1
        if s_pointer == s_length:
            return True

    return False


assert is_subsequence(s='abc', t='ahbgdc') == True, 'Test 1 Failed'
assert is_subsequence(s='axc', t='ahbgdc') == False, 'Test 2 Failed'
assert is_subsequence(s='', t='ahbgdc') == True, 'Test 3 Failed'