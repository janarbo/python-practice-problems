# Complete the calculate_average function which accepts
# a list of numerical values and returns the average of
# the numbers.
#
# If the list of values is empty, the function should
# return None
#
# Pseudocode is available for you


def calculate_average(values):
    if len(values) == 0:
        return None

    sum = 0

    for each in values:
        sum += each
    return sum / len(values)
