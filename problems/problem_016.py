# Complete the is_inside_bounds function which takes an x
# coordinate and a y coordinate, and then tests each to
# make sure they're between 0 and 10, inclusive.
# does my solution work?


def is_inside_bounds(x, y):
    if 0 <= x <= 10 and 0 <= y <= 10:
        return True
    else:
        return False
