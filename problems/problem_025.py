# Complete the calculate_sum function which accepts
# a list of numerical values and returns the sum of
# the numbers.
#
# If the list of values is empty, the function should
# return None
#


def calculate_sum(values):
    if len(values) == 0:
        return None
    sum = 0
    for each in values:
        sum += each
    return sum
