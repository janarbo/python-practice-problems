# Complete the remove_duplicate_letters that takes a string
# parameter "s" and returns a string with all of the
# duplicates removed.
#
# Examples:
#   * For "abc", the result is "abc"
#   * For "abcabc", the result is "abc"
#   * For "abccba", the result is "abc"
#   * For "abccbad", the result is "abcd"
#
# If the list is empty, then return the empty string.


def remove_duplicate_letters(s):
    if len(s) == 0:
        return s
    new_string = ""
    for each in s:
        if each not in new_string:
            new_string += each
    return new_string
