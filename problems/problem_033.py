# Complete the sum_of_first_n_even_numbers function which
# accepts a numerical count n and returns the sum of the
# first n even numbers
#
# If the value of the limit is less than 0, then it should
# return None
#
# Examples:
#   * -1 returns None
#   * 0 returns 0
#   * 1 returns 0+2=2
#   * 2 returns 0+2+4=6
#   * 5 returns 0+2+4+6+8+10=30
#
# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.python -m pytest -k "033"


def sum_of_first_n_even_numbers(n):
    if n < 0:
        return None

    sum = 0

    for number in range(n * 2 + 1):
        if number % 2 == 0:
            sum += number
    return sum
