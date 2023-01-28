from pytest import mark

from techniques.AlmostLockedCandidatesClaiming import AlmostLockedCandidatesClaiming
from tests_explicit.test_small_explicit import solve

@mark.skip("EXPLICITLY")
def test_almost_locked_candidates_claiming_row():
    actual = \
        f"""
        __34a 12__a   ____b ____b
        ____a ____a   12__b ____b

        ____c ____c   ____d ____d
        ____c ____c   ____d ____d
        """

    expected = \
        f"""
        __34a 12__a   ____b ____b
        ____a ____a   12__b __34b

        ____c ____c   ____d ____d
        ____c ____c   ____d ____d
        """
    if solve(4, actual, expected, AlmostLockedCandidatesClaiming()):
        return
    assert False
