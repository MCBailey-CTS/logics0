from pytest import mark


@mark.skip("EXPLICITLY")
def test_almost_locked_candidates_pointing_row():
    actual = \
        f"""
        ____a 12__a   ____b ____b
        ____a ____a   12__b __34b

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
    if solve(4, actual, expected, tech.AlmostLockedCandidatesPointing()):
        return
    assert False