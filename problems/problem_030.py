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
# Failed


def find_second_largest(values):
    if len(values) <= 1:
        return None
    values = []
    max = values[0]
    second_largest = values[0]

    for each_value in values:
        if each_value > max:
            max = each_value
        if each_value > second_largest and second_largest < max:
            second_largest = each_value
    return second_largest
