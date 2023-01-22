# Complete the gear_for_day function which returns a list of
# gear needed for the day given certain criteria.
#   * If the day is not sunny and it is a workday, the list
#     needs to contain "umbrella"
#   * If it is a workday, the list needs to contain "laptop"
#   * If it is not a workday, the list needs to contain
#     "surfboard"


def gear_for_day(is_workday, is_sunny):
    gear = []
    if is_workday and not is_sunny:
        gear.append("umbrella")
    if is_workday:
        gear.append("laptop")
    else:
        gear.append("surfboard")
    return gear
