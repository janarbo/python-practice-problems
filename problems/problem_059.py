# Write a function that meets these requirements.
#
# Name:       specific_random
# Parameters: none
# Returns:    a random number between 10 and 500, inclusive,
#             that is divisible by 5 and 7
#
# Examples:
#     * returns: 35
#     * returns: 105
#     * returns: 70
#
# Guidance:
#   * Generate all the numbers that are divisible by 5
#     and 7 into a list
#   * Use random.choice to select one

import random


def specific_random():
    nums = []
    for each in range(10,501):
        nums.append(each)
    new_list = []
    for each in nums:
        if each % 5 == 0 and each % 7 == 0:
            new_list.append(each)
    return random.choice(new_list)
