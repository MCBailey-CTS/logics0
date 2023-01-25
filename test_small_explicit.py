actual0 = \
    f"""
        ____a ____a   ____b ____b
        ____a ____a   ____b ____b

        ____c ____c   ____d ____d
        ____c ____c   ____d ____d
        """


def test_():
    actual = \
        f"""
        ____a ____a   ____b ____b
        ____a ____a   ____b ____b

        ____c ____c   ____d ____d
        ____c ____c   ____d ____d
        """

    expected = \
        f"""
        ____a ____a   ____b ____b
        ____a ____a   ____b ____b

        ____c ____c   ____d ____d
        ____c ____c   ____d ____d
        """
    assert False


def test_cross_hatch():
    actual = \
        f"""
        1___a ____a   ____b ____b
        ____a ____a   2___b ____b
        
        ____c 3___c   ____d ____d
        ____c ____c   ____d ___4d
        """
    expected = \
        f"""
        1___a _2_4a   1_34b 123_b
        _234a _2_4a   _2__b 123_b

        _2_4c 3___c   1_34d 123_d
        _2__c 12__c   1_34d ___4d
            """
    assert False


def test_xy_chain_west():
    actual = \
        f"""
        ____a ____a   ____b ____b
        ____a 12__a   ____b _23_b

        ____c ____c   ____d ____d
        1__4c ____c   ____d __34d
        """

    expected = \
        f"""
        _234a ____a   ____b ____b
        _234a 12__a   ____b _23_b

        ____c _234c   ____d ____d
        1__4c _234c   ____d __34d
        """
    assert False


def test_hidden_unique_rectangle_row_chute_south_east():
    actual = \
        f"""
        ____a 12__a   ____b 1234b
        _234a 1234a   _234b 1234b

        ____c ____c   ____d _234d
        ____c ____c   ____d _234d
        """

    expected = \
        f"""
        ____a 12__a   ____b 1234b
        _234a 1234a   _234b 1_34b

        ____c ____c   ____d _234d
        ____c ____c   ____d _234d
        """
    assert False


def test_xyz_wing_fences2_row_chute():
    actual = \
        f"""
        ____a 123_a   1_3_b ____b
        _23_a ____a   ____b ____b

        ____c ____c   ____d ____d
        ____c ____c   ____d ____d
        """

    expected = \
        f"""
        12_4a 123_a   1_3_b ____b
        _23_a ____a   ____b ____b

        ____c ____c   ____d ____d
        ____c ____c   ____d ____d
        """
    assert False

def test_sudoku_4x4_wxyz_fences2_south():
    actual = \
        f"""
        _234a 1__4a   ____b ____b
        ____a 1_3_a   ____b ____b

        ____c ____c   ____d ____d
        2_4_c ____c   ____d ____d
        """

    expected = \
        f"""
        _234a 1__4a   ____b ____b
        123_a 1_3_a   ____b ____b

        ____c ____c   ____d ____d
        2_4_c ____c   ____d ____d
        """
    assert False


def test_sudoku_4x4_wxyz_fences2_north():
    actual = \
        f"""
        ____a ____a   ____b ____b
        _23_a ____a   ____b ____b

        12__c 1__4c   ____d ____d
        ____c __34c   ____d ____d
        """

    expected = \
        f"""
        ____a ____a   ____b ____b
        _23_a ____a   ____b ____b

        12__c 1__4c   ____d ____d
        12_4c __34c   ____d ____d
        """
    assert False