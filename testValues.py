
# Example variations (notes only; replace the active arrays above to use one).
#regular check
_DIST_A_VALUES = (5, 4, 3, 2, 1, 0, 1, 2, 0, 4, 5, 6, 7, 8, 9, 10)
_DIST_B_VALUES = (11, 12, 13, 14, 15, 16, 17, 18, 19, 20,19, 18, 17, 16, 15, 14, 13, 12, 11)

# Both arrays reach 0 twice at matching positions (8 and 14):
#_DIST_A_VALUES = (7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 2, 1, 0, 1,9,7)
#_DIST_B_VALUES = (4, 3, 2, 1, 2, 3, 4, 0, 1, 2, 3, 2, 1, 0, 1,9,7)
#
# Float values use 0.1 instead of 0:
#_DIST_A_VALUES = (7.5, 6.4, 5.3, 4.2, 3.1, 2.2, 1.1, 0.1, 1.2, 2.3, 3.4, 2.5, 1.6, 0.1, 1.3, 1.6)
#_DIST_B_VALUES = (4.6, 3.5, 2.4, 1.3, 2.2, 3.1, 4.2, 0.1, 1.2, 2.3, 3.4, 2.5, 1.6, 0.1, 1.3, 1.6)
#
# Values stay at or above 1 (the minimum is 1, not 0):
#_DIST_A_VALUES = (7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3)
#_DIST_B_VALUES = (4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2)

_dist_a_index = 0
_dist_b_index = 0


def get_dist_a(location):
    global _dist_a_index
    if _dist_a_index >= len(_DIST_A_VALUES):
        raise IndexError("get_dist_a has no values remaining")
    value = _DIST_A_VALUES[_dist_a_index]
    _dist_a_index += 1
    return value


def get_dist_b(location):
    global _dist_b_index
    if _dist_b_index >= len(_DIST_B_VALUES):
        raise IndexError("get_dist_b has no values remaining")
    value = _DIST_B_VALUES[_dist_b_index]
    _dist_b_index += 1
    return value