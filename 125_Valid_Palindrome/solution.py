def is_palindrome(s: str) -> bool:
    """
    First solution. Time complexity is O(n), memory complexity is O(n).
    Creates a cleaned string (lowercase alphanumeric characters) and checks if it reads the same forwards and backwards.
    :param s: Input string to check
    :return: True if the string is a valid palindrome, False otherwise
    """
    s = ''.join([char.lower() for char in s if char.isalnum()])
    return s == s[::-1]

assert is_palindrome("A man, a plan, a canal: Panama") == True, 'Test 1 failed'
assert is_palindrome("race a car") == False, 'Test 2 failed'
assert is_palindrome(" ") == True, 'Test 3 failed'

def is_palindrome2(s: str) -> bool:
    """
    Second solution. Time complexity is O(n), memory complexity is O(1).
    Uses two pointers to compare characters from both ends, skipping non-alphanumeric characters.
    Case-insensitive comparison is performed for alphanumeric characters.

    :param s: Input string to check
    :return: True if the string is a valid palindrome, False otherwise
    """
    left = 0
    right = len(s) - 1

    while left < right:
        while (left < right) and not s[left].isalnum():
            left += 1
        while (left < right) and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True

assert is_palindrome2("A man, a plan, a canal: Panama") == True, 'Test 1 failed'
assert is_palindrome2("race a car") == False, 'Test 2 failed'
assert is_palindrome2(" ") == True, 'Test 3 failed'