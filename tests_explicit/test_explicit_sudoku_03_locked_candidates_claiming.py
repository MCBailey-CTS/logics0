from tests_explicit.test_small_explicit import solve
from techniques.LockedCandidatesClaiming import LockedCandidatesClaiming
import pytest

@pytest.mark.skip("")
def test_locked_candidates_claiming_rows():
    actual = \
        f"""
        123_a 123_a   ____b ____b
        ____a ____a   ____b ____b

        ____c ____c   ____d ____d
        ____c ____c   ____d ____d
        """
    expected = \
        f"""
        123_a 123_a   ____b ____b
        ____a ____a   123_b 123_b

        ____c ____c   ____d ____d
        ____c ____c   ____d ____d
        """
    if solve(4, actual, expected, LockedCandidatesClaiming()):
        return
    assert False

@pytest.mark.skip("")
def test_locked_candidates_claiming_cols():
    actual = \
        f"""
        123_a ____a   ____b ____b
        123_a ____a   ____b ____b

        ____c ____c   ____d ____d
        ____c ____c   ____d ____d
        """
    expected = \
        f"""
        123_a ____a   ____b ____b
        123_a ____a   ____b ____b

        ____c 123_c   ____d ____d
        ____c 123_c   ____d ____d
        """
    if solve(4, actual, expected, LockedCandidatesClaiming()):
        return
    assert False