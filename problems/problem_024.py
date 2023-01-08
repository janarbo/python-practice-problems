# Complete the calculate_average function which accepts
# a list of numerical values and returns the average of
# the numbers.
#
# If the list of values is empty, the function should
# return None
#
# Pseudocode is available for you


def calculate_average(values):
    sum = 0
    if len(values) == 0:
        return None

    for each in values:
        sum += each
    return sum / len(values)


values = []

print(calculate_average(values))
