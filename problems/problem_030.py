# Complete the find_second_largest function which accepts
# a list of numerical values and returns the second largest
# in the list
#
# If the list of values is empty, the function should
# return None
#
# If the list of values has only one value, the function
# should return None
#
# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.


def find_second_largest(values):
    if len(values) <= 1:
        return None

    largest = values[0]
    second_largest = values[0]
    for number in values:
        if number > largest:
            second_largest = largest
            largest = number
        elif number > second_largest:
            second_largest = number
    return second_largest
