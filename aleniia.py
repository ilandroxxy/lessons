# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


while True:
    s = input()
    if len(s) == 0:
        break

    s = s.lstrip("@#$")
    s = s.rstrip("!,.")

    if s.startswith("And"):
        s = s.replace("and", "or")
    elif s.endswith("end"):
        s = s.replace("or", "and")

    print(s)

# @@@#And six and little mice were rustling or in the reeds and in the forest.
# $##$Six sick hicks or and end!!!
# nick and six slick or bricks,.
# #@with picks or sticks end
# forty mice were walking and six found pennies,!


# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 3, 4, 6, 9, 10]
# на следующем уроке: