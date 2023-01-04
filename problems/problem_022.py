# Complete the gear_for_day function which returns a list of
# gear needed for the day given certain criteria.
#   * If the day is not sunny and it is a workday, the list
#     needs to contain "umbrella"
#   * If it is a workday, the list needs to contain "laptop"
#   * If it is not a workday, the list needs to contain
#     "surfboard"


def gear_for_day(is_workday, is_sunny):
    gear_list = []
    if is_sunny is False and is_workday is True:
        "umbrela" == gear_list
    elif is_workday is True:
        "laptop" == gear_list
    elif is_workday is False:
        "surfboard" == gear_list
    else:
        return False
