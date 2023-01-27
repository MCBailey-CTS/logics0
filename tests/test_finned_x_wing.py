from tests.test_small_explicit import solve
from pytest import mark

@mark.skip("EXPLICITLY")
def test_shashimi_x_wing_east_fins1():
    actual = \
        f"""
        _234a ____a   234_b ____b
        ____a ____a   ____b ____b

        _234c ____c   ____d _234d
        ____c ____c   ____d ____d
        """

    expected = \
        f"""
        _234a ____a   234_b ____b
        ____a ____a   _234b ____b

        _234c ____c   ____d _234d
        ____c ____c   ____d _234d
        """
    if solve(4, actual, expected, None):
        return
    assert False


@mark.skip("EXPLICITLY")
def test_finned_x_wing_east_fins1():
    actual = \
        f"""
        _234a ____a   234_b ____b
        ____a ____a   ____b ____b

        _234c ____c   ____d ____d
        ____c ____c   ____d ____d
        """

    expected = \
        f"""
        _234a ____a   234_b ____b
        ____a ____a   ____b ____b

        _234c ____c   ____d ____d
        ____c ____c   ____d _234d
        """
    if solve(4, actual, expected, None):
        return
    assert False