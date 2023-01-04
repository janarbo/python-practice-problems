# Complete the can_make_pasta function to
# * Return true if the ingredients list contains
#   "flour", "eggs", and "oil"
# * Otherwise, return false
#
# The ingredients list will always contain three items.

# Do some planning in ./planning.md

# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.


def can_make_pasta(ingredients):
    ingredients_list = []
    each_ingredient = ingredients_list[0]
    for each_ingredient in ingredients:
        if (
            each_ingredient == "flours"
            and each_ingredient == "eggs"
            and each_ingredient == "oil"
        ):
            return True
        else:
            return False
