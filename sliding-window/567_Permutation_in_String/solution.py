def check_inclusion(s1: str, s2: str) -> bool:
    """
    Check if any permutation of s1 exists as a substring in s2.

    This function uses a sliding window approach with hash maps to efficiently
    track character counts and determine if any permutation of s1 is present in s2.

    :param s1: The string whose permutations we want to find in s2.
    :param s2: The string in which we're searching for permutations of s1.
    :return: True if any permutation of s1 is found as a substring in s2, False otherwise.
    """
    pattern_hash = {}
    for character in s1:
        if character not in pattern_hash:
            pattern_hash[character] = 1
        else:
            pattern_hash[character] += 1

    hash_copy = pattern_hash.copy()
    pattern_length = len(s1)

    for index in range(len(s2)):
        if index >= pattern_length:
            outgoing_character = s2[index - pattern_length]
            if outgoing_character in pattern_hash:
                if outgoing_character not in hash_copy:
                    hash_copy[outgoing_character] = 1
                else:
                    hash_copy[outgoing_character] += 1
                if hash_copy[outgoing_character] == 0:
                    del hash_copy[outgoing_character]

        incoming_character = s2[index]
        if incoming_character in pattern_hash:
            if incoming_character in hash_copy:
                hash_copy[incoming_character] -= 1
            else:
                hash_copy[incoming_character] = -1
            if hash_copy[incoming_character] == 0:
                del hash_copy[incoming_character]
            if len(hash_copy) == 0:
                return True
    return False


assert check_inclusion(s1='ab', s2='eidbaooo') == True, 'Test 1 Failed'
assert check_inclusion(s1='ab', s2='eidboaoo') == False, 'Test 2 Failed'
assert check_inclusion(s1='adc', s2='dcda') == True, 'Test 3 Failed'