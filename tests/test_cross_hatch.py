
from tests.test_small_explicit import solve
from techniques.CrossHatch import CrossHatch

def test_cross_hatch():
    actual = \
        f"""
        1___a ____a   ____b ____b
        ____a ____a   ____b ____b

        ____c ____c   ____d ____d
        ____c ____c   ____d ____d
        """
    expected = \
        f"""
        1___a _234a   _234b _234b
        _234a _234a   ____b ____b

        _234c ____c   ____d ____d
        _234c ____c   ____d ____d
            """
    if solve(4, actual, expected, CrossHatch()):
        return
    assert False

