import pytest

from _defaults import default_test_puzzle
from puzzles import Magnets
from solving import Solving


# @pytest.mark.skip("skip")


@pytest.mark.skip("skip")
def test_magnets_001():
    # ┼────┼────┼────┼────┼
    # │+-. │+-. │+-.  +-. │02 02
    # ┼    ┼    ┼────┼────┼
    # |+-. │+-. │+-.  +-. │01 01
    # ┼────┼────┼────┼────┼
    # |+-. │+-.  +-. │+-. │01 00
    # ┼─   ┼────┼────┼─   ┼
    # |+-. │+-.E +-.E│+-. │01 02
    # ┼────┼────┼────┼────┼
    # 01   01   02   01   +  .
    # 01   02   00   02   .  -
    puzzle_string = f"""
    001.magnets
    4
    +-.A +-.C +-.G +-.G 02 02
    +-.A +-.C +-.H +-.H 01 01
    +-.B +-.D +-.D +-.F 01 00
    +-.B +-.E +-.E +-.F 01 02
    01   01   02   01   +  .
    01   02   00   02   .  -
    """
    assert default_test_puzzle(puzzle_string, Magnets, Solving.magnets_techniques())


@pytest.mark.skip("skip")
def test_magnets_002():
    puzzle_string = f"""
    002.magnets
    4
    +-.A +-.A +-.E +-.G 01 01
    +-.B +-.B +-.E +-.G 02 02
    +-.C +-.C +-.F +-.H 02 02
    +-.D +-.D +-.F +-.H 02 02
    02   01   02   02   ++ $$
    01   02   02   02   $$ --
    """
    assert default_test_puzzle(puzzle_string, Magnets, Solving.magnets_techniques())


@pytest.mark.skip("skip")
def test_magnets_003():
    puzzle_string = f"""
    003.magnets
    5
    +-.A +-.A +-.B +-.B +-.K 02 03
    +-.C +-.E +-.E #### +-.K 02 01
    +-.C +-.F +-.H +-.I +-.I 00 00
    +-.D +-.F +-.H +-.J +-.L 01 02
    +-.D +-.G +-.G +-.J +-.L 03 02
    01   01   02   02   02   ++ $$
    02   02   01   01   02   $$ --
    """
    assert default_test_puzzle(puzzle_string, Magnets, Solving.magnets_techniques())


@pytest.mark.skip("skip")
def test_magnets_004():
    puzzle_string = f"""
    004.magnets
    5
    #### +-.f +-.g +-.g +-.i 2 2
    +-.a +-.f +-.h +-.h +-.i 3 2
    +-.a +-.e +-.e +-.j +-.j 2 3
    +-.b +-.d +-.d +-.k +-.l 2 2
    +-.b +-.c +-.c +-.k +-.l 1 1
    1 2 2 3 2 + $
    1 2 2 2 3 $ +
    """
    assert default_test_puzzle(puzzle_string, Magnets, Solving.magnets_techniques())


@pytest.mark.skip("skip")
def test_magnets_005():
    puzzle_string = f"""
    005.magnets
    5
    A E F F # ? ?
    A E G H I ? 0
    B D G H I ? ?
    B D J K L ? ?
    C C J K L 2 ?
    2 1 2 ? 2 + $
    ? ? ? 2 2 $ -
    """
    assert default_test_puzzle(puzzle_string, Magnets, Solving.magnets_techniques())


@pytest.mark.skip("skip")
def test_magnets_006():
    puzzle_string = f"""
    006.magnets
    5
    # C D D F ? ?
    A C E E F ? 3
    A G G K L ? 2
    B H H K L ? ?
    B I I J J 2 ?
    ? ? 3 ? ? + $
    ? 2 2 2 2 $ -
    """
    assert default_test_puzzle(puzzle_string, Magnets, Solving.magnets_techniques())


@pytest.mark.skip("skip")
def test_magnets_007():
    puzzle_string = f"""
    007.magnets
    5
    A A G H I 1 1
    B D G H I 1 2
    B D F F # 2 1
    C E J J L 2 1
    C E K K L 1 2
    2 1 1 1 2 + $
    2 1 2 0 2 $ -
    """
    assert default_test_puzzle(puzzle_string, Magnets, Solving.magnets_techniques())


@pytest.mark.skip("skip")
def test_magnets_008():
    puzzle_string = f"""
    008.magnets
    5
    +-a +-a +-b +-b ### 2 2
    +-c +-c +-d +-d +-l 1 2
    +-e +-e +-i +-j +-l 2 1
    +-f +-g +-i +-j +-k 2 2
    +-f +-g +-h +-h +-k 1 1
    02  01  01  02  02  + $
    02  01  02  01  02  $ -
    """
    assert default_test_puzzle(puzzle_string, Magnets, Solving.magnets_techniques())


@pytest.mark.skip("skip")
def test_magnets_009():
    puzzle_string = f"""
    009.magnets
    5
    # a a i j ? ?
    b b h i j ? ?
    c c h k k 1 ?
    d d g g l ? 1
    e e f f l 2 2
    1 ? ? ? ? + .
    2 ? ? 2 2 . -
    """
    assert default_test_puzzle(puzzle_string, Magnets, Solving.magnets_techniques())


@pytest.mark.skip("skip")
def test_magnets_010():
    puzzle_string = f"""
    010.magnets
    5
    a g h h j ? ?
    a g i i j ? 1
    b k k l l 2 2
    b # e e f ? 2
    c c d d f ? ?
    ? ? ? ? ? + .
    2 ? 2 2 ? . -
    """
    assert default_test_puzzle(puzzle_string, Magnets, Solving.magnets_techniques())


@pytest.mark.skip("skip")
def test_magnets_011():
    puzzle_string = f"""
    011.magnets
    6
    A E E J K K 1 2
    A F F J L L 3 2
    B B G M M T 2 3
    C C G N N T 3 2
    D H I O P W 2 2
    D H I O P W 2 2
    2 2 2 1 3 3 + .
    2 3 1 1 3 3 . -
    """
    assert default_test_puzzle(puzzle_string, Magnets, Solving.magnets_techniques())


@pytest.mark.skip("skip")
def test_magnets_012():
    puzzle_string = f"""
    012.magnets
    6
    a b c c d d 3 3
    a b e e f f 2 2
    g h i j k k 2 2
    g h i j l l 1 1
    m m o p p r 1 3
    n n o q q r 2 0
    1 3 3 1 1 2 + .
    2 2 3 1 1 2 . -
    """
    assert default_test_puzzle(puzzle_string, Magnets, Solving.magnets_techniques())


@pytest.mark.skip("skip")
def test_magnets_013():
    puzzle_string = f"""
    013.magnets
    6
    a b c d e f 3 2
    a b c d e f 2 3
    g g h h i i 2 2
    j j k k l l 2 2
    m m n n o o 0 0
    p p q q r r 3 3
    3 2 2 1 2 2 + .
    2 3 2 1 2 2 . -
    """
    assert default_test_puzzle(puzzle_string, Magnets, Solving.magnets_techniques())


@pytest.mark.skip("skip")
def test_magnets_014():
    puzzle_string = f"""
    014.magnets
    6
    a i j k l l ? ?
    a i j k q r 3 2
    b m m o q r ? ?
    b n n o p p 3 3
    c f f g g h 2 1
    c d d e e h 2 ?
    ? ? ? 2 3 ? + .
    ? ? 2 2 3 ? . -
    """
    assert default_test_puzzle(puzzle_string, Magnets, Solving.magnets_techniques())


@pytest.mark.skip("skip")
def test_magnets_015():
    puzzle_string = f"""
    015.magnets
    6
    a i i j j p 2 2
    a h k l o p ? 2
    b h k l o q ? 3
    b g g m n q ? 2
    c d e m n r 2 3
    c d e f f r 3 1
    ? ? ? ? 0 ? + .
    ? ? ? ? ? ? . -
    """
    assert default_test_puzzle(puzzle_string, Magnets, Solving.magnets_techniques())


@pytest.mark.skip("skip")
def test_magnets_016():
    puzzle_string = f"""
    016.magnets
    6
    a b c d d k 2 3
    a b c i j k 3 1
    e f f i j l 1 3
    e g g h h l 2 1
    m m o p r r 1 2
    n n o p q q 3 2
    2 3 2 2 2 1 + .
    3 2 2 1 3 1 . -
    """
    assert default_test_puzzle(puzzle_string, Magnets, Solving.magnets_techniques())


@pytest.mark.skip("skip")
def test_magnets_017():
    puzzle_string = f"""
    017.magnets
    6
    a a b b f g 2 1
    c d e e f g 2 2
    c d m n n q 1 1
    h h m o p q 2 3
    i l l o p e 2 1
    i j j k k e 1 2
    2 2 0 2 2 2 + .
    2 1 2 1 2 2 . -
    """
    assert default_test_puzzle(puzzle_string, Magnets, Solving.magnets_techniques())


@pytest.mark.skip("skip")
def test_magnets_018():
    puzzle_string = f"""
    018.magnets
    6
    a n n p q q 2 3
    a o o p r r 2 1
    b b c c d d 1 1
    e k k l l m 2 3
    e i i j j m 2 1
    f f g g h h 2 2
    2 3 2 1 3 0 + .
    3 2 2 0 1 3 . -
    """
    assert default_test_puzzle(puzzle_string, Magnets, Solving.magnets_techniques())


@pytest.mark.skip("skip")
def test_magnets_019():
    puzzle_string = f"""
    019.magnets
    6
    A A G N N P 3 2
    B E G O O P 2 3
    B E H M Q Q 3 2
    C F H M R R 2 3
    C F I I K K 2 2
    D D J J L L 2 2
    3 3 2 1 2 3 + .
    3 3 1 2 3 2 . -
    """
    assert default_test_puzzle(puzzle_string, Magnets, Solving.magnets_techniques())


@pytest.mark.skip("skip")
def test_magnets_020():
    puzzle_string = f"""
    020.magnets
    6
    a f g g q r 3 2
    a f h i q r 2 2
    b e h i p p 2 3
    b e j k o o 2 1
    c d j k n n 2 2
    c d l l m m 1 2
    1 3 1 2 2 3 + .
    1 3 2 1 3 2 . -
    """
    assert default_test_puzzle(puzzle_string, Magnets, Solving.magnets_techniques())


@pytest.mark.skip("skip")
def test_magnets_021():
    puzzle_string = f"""
    021.magnets
    6
    a a i j j p 3 3
    b b i k l p 3 3
    c c h k l q 2 2
    d d h m n q 1 1
    e f g m n r 1 1
    e f g o o r 2 2
    2 3 1 1 3 2 + .
    2 3 1 3 1 2 . -
    """
    assert default_test_puzzle(puzzle_string, Magnets, Solving.magnets_techniques())


@pytest.mark.skip("skip")
def test_magnets_022():
    puzzle_string = f"""
    022.magnets
    6
    a f f g g j 2 2
    a h h i i j 3 3
    b b k k p q 3 3
    c c l l p q 3 3
    d e m m o r 3 2
    d e n n o r 1 2
    3 2 3 2 2 3 + .
    3 2 2 2 3 3 . -
    """
    assert default_test_puzzle(puzzle_string, Magnets, Solving.magnets_techniques())


@pytest.mark.skip("skip")
def test_magnets_023():
    puzzle_string = f"""
    023.magnets
    6
    a a d e e g 1 1
    b c d f f g ? ?
    b c o p p r ? ?
    h h o q q r 1 ?
    j i k l m m ? ?
    j i k l n n 2 3
    3 3 ? 2 ? ? + .
    3 3 1 2 2 ? . -
    """
    assert default_test_puzzle(puzzle_string, Magnets, Solving.magnets_techniques())


@pytest.mark.skip("skip")
def test_magnets_024():
    puzzle_string = f"""
    024.magnets
    6
    a a b b q r ? 2
    c k k l q r ? 2
    c i j l o p ? ?
    d i j m o p 3 3
    d h h m n n 2 ?
    e e f f g g ? ?
    3 ? ? ? 2 ? + .
    1 ? 2 3 ? ? . -
    """
    assert default_test_puzzle(puzzle_string, Magnets, Solving.magnets_techniques())


@pytest.mark.skip("skip")
def test_magnets_025():
    puzzle_string = f"""
    025.magnets
    6
    a j j m n n 2 2
    a i h m o p 3 2
    b i h l o p ? ?
    b k k l q r 3 2
    c e e f q r ? ?
    c d d f g g 3 2
    2 3 2 ? 1 3 + .
    ? 2 3 ? ? 2 . -
    """
    assert default_test_puzzle(puzzle_string, Magnets, Solving.magnets_techniques())


@pytest.mark.skip("skip")
def test_magnets_027():
    puzzle_string = f"""
    027.magnets
    6
    A B C C E E ? ?
    A B D D F F 2 ?
    G I I M O O ? 3
    G J J M P Q 3 1
    H K K N P Q ? ?
    H L L N R R 3 2
    ? ? 1 ? ? ? + .
    3 2 2 ? ? ? . -
    """
    assert default_test_puzzle(puzzle_string, Magnets, Solving.magnets_techniques())


@pytest.mark.skip("skip")
def test_magnets_028():
    puzzle_string = f"""
    028.magnets
    7
    A A C D # E E 3 3
    B B C D F F P 3 2
    G L L M N N P 1 1
    G K K M O O W 2 2
    H J Q Q U V W 0 2
    H J R S U V X 3 1
    I I R S T T X 3 4
    1 3 2 2 2 2 3 + .
    3 0 3 2 2 1 4 . -
    """
    assert default_test_puzzle(puzzle_string, Magnets, Solving.magnets_techniques())


@pytest.mark.skip("skip")
def test_magnets_029():
    puzzle_string = f"""
    029.magnets
    7
    a b b n n r s ? ?
    a # m o o r s 2 0
    c i m p p q q 1 ?
    c i k k l l w 3 ?
    d h j t t v w ? 4
    d h j u u v x 4 ?
    e e f f g g x 3 4
    2 3 1 ? ? ? ? + .
    ? ? ? ? ? 3 ? . -
    """
    assert default_test_puzzle(puzzle_string, Magnets, Solving.magnets_techniques())


@pytest.mark.skip("skip")
def test_magnets_030():
    puzzle_string = f"""
    030.magnets
    7
    a b k k s t t 3 4
    a b j l s u u ? ?
    c c j l r v w 3 ?
    d d i m r v w ? ?
    e f i m q q x 3 ?
    e f h # p p x 3 3
    g g h n n o o 3 ?
    ? ? ? 2 3 ? 3 + .
    ? ? ? ? ? ? 4 . -
    """
    assert default_test_puzzle(puzzle_string, Magnets, Solving.magnets_techniques())


@pytest.mark.skip("skip")
def test_magnets_031():
    puzzle_string = f"""
    031.magnets
    7
    a a k l r r # 3 3
    b c k l q s s 3 3
    b c j j q t u 3 3
    d d i p p t u 2 2
    e e i n o v v 1 2
    f f h n o w x 3 2
    g g h m m w x 3 3
    3 3 2 3 1 3 3 + .
    3 3 3 3 1 2 3 . -
    """
    assert default_test_puzzle(puzzle_string, Magnets, Solving.magnets_techniques())


@pytest.mark.skip("skip")
def test_magnets_032():
    puzzle_string = f"""
    032.magnets
    7
    a a b b c c # 1 1
    d d f s s t u 2 2
    e e f q r t u 3 3
    g o o q r v v 3 2
    g n n p p w x 2 3
    h h j k l w x 3 3
    i i j k l m m 3 3
    3 2 0 3 3 3 3 + .
    3 2 1 3 2 3 3 . -
    """
    assert default_test_puzzle(puzzle_string, Magnets, Solving.magnets_techniques())


@pytest.mark.skip("skip")
def test_magnets_033():
    puzzle_string = f"""
    033.magnets
    7
    # a a b b s t ? ?
    c c d d r s t ? 3
    g g h h r u u 3 ?
    e i i m q v w 3 ?
    e j j m q v w 3 ?
    f k k n p p x 2 0
    f l l n o o x ? ?
    ? ? 2 ? 4 1 ? + .
    ? ? ? 2 ? ? ? . -
    """
    assert default_test_puzzle(puzzle_string, Magnets, Solving.magnets_techniques())


@pytest.mark.skip("skip")
def test_magnets_034():
    puzzle_string = f"""
    034.magnets
    7
    a a b b # s t 3 3
    c d e e p s t 3 ?
    c d m n p u u ? ?
    f f m n q v v ? 2
    g g l o q w w 2 ?
    h h l o r r x ? 3
    i i j j k k x 4 ?
    4 ? 3 ? 3 ? ? + .
    2 ? ? ? 2 ? 3 . -
    """
    assert default_test_puzzle(puzzle_string, Magnets, Solving.magnets_techniques())


@pytest.mark.skip("skip")
def test_magnets_035():
    puzzle_string = f"""
    035.magnets
    7
    a A A B B C C 2 ?
    a D E F G H H ? ?
    b D E F G N O ? ?
    b # J K L N O ? 3
    c c J K L M M 2 2
    d d f g h i j 3 2
    e e f g h i j ? ?
    ? 0 3 2 2 0 4 + .
    ? 1 ? ? ? ? ? . -
    """
    assert default_test_puzzle(puzzle_string, Magnets, Solving.magnets_techniques())


@pytest.mark.skip("skip")
def test_magnets_036():
    puzzle_string = f"""
    036.magnets
    7
    a b # c c d d ? ?
    a b n o o p p 4 ?
    e e n q q r r ? 4
    f f m m s s x ? ?
    g g l l t u x 3 ?
    h h k k t u w ? ?
    i i j j v v w 2 ?
    ? ? ? 3 ? 2 3 + .
    2 2 ? ? ? 3 ? . -
    """
    assert default_test_puzzle(puzzle_string, Magnets, Solving.magnets_techniques())


@pytest.mark.skip("skip")
def test_magnets_037():
    puzzle_string = f"""
    037.magnets
    7
    a b b c c d d ? ?
    a p s s t t w 1 3
    e p # u u v w ? ?
    e q q r r v x 1 ?
    f f h h i i x 1 0
    g j j k k l l ? ?
    g m m n n o o 3 3
    ? 2 2 3 ? 1 ? + .
    2 ? ? 2 ? 0 ? . -
    """
    assert default_test_puzzle(puzzle_string, Magnets, Solving.magnets_techniques())


@pytest.mark.skip("skip")
def test_magnets_038():
    puzzle_string = f"""
    038.magnets
    8
    a b c c w y y B 3 3
    a b u v w z A B 4 4
    d d u v x z A E 4 4
    e e t t x C D E 2 2
    f n n o p C D F 2 2
    f i j o p q r F 2 2
    g i j k l q r s 3 2
    g h h k l m m s 3 4
    3 3 2 3 2 3 4 3 + .
    4 1 3 3 2 3 4 3 . -
    """
    assert default_test_puzzle(puzzle_string, Magnets, Solving.magnets_techniques())


@pytest.mark.skip("skip")
def test_magnets_039():
    puzzle_string = f"""
    039.magnets
    8
    a q q s t t G H 4 2
    a r r s A F G H 0 3
    b u v w A F I I 3 1
    b u v w B C D E 2 4
    c c j j B C D E 3 2
    d d i i k k l l 4 4
    e e h h m o o p 4 3
    f f g g m n n p 3 4
    4 3 3 2 2 4 2 3 + .
    4 4 3 1 4 2 3 2 . -
    """
    assert default_test_puzzle(puzzle_string, Magnets, Solving.magnets_techniques())


@pytest.mark.skip("skip")
def test_magnets_040():
    puzzle_string = f"""
    040.magnets
    8
    a c c d e f h h 3 ?
    a b b d e f g g 3 3
    i i s t t A C D 2 2
    j k s u v A C D 4 4
    j k r u v B B E ? 4
    l l r w y y z E ? 3
    m q q w x x z F 2 ?
    m n n o o p p F ? 2
    4 ? ? 2 ? 3 ? ? + .
    3 ? ? ? 2 1 ? ? . -
    """
    assert default_test_puzzle(puzzle_string, Magnets, Solving.magnets_techniques())


@pytest.mark.skip("skip")
def test_magnets_041():
    puzzle_string = f"""
    041.magnets
    8
    a a b b c c d d 4 4
    e f g h h i i F ? ?
    e f g u w x x F 2 ?
    j j l u w y y E ? ?
    k k l v v z z E 4 2
    m s s t t A D D 2 4
    m q q r r A B C 4 2
    n n o o p p B C ? ?
    2 4 2 2 1 4 ? ? + .
    ? ? 3 ? 1 4 ? 3 . -
    """
    assert default_test_puzzle(puzzle_string, Magnets, Solving.magnets_techniques())


@pytest.mark.skip("skip")
def test_magnets_042():
    puzzle_string = f"""
    042.magnets
    8
    a p p q q r r F 2 2
    a s t u v v x F 3 2
    b s t u w w x E 1 3
    b y y z z A B E 3 1
    c c d d k A B D 2 3
    e i i j k C C D 3 2
    e h h j l m n n 2 2
    f f g g l m o o 3 4
    2 2 2 4 3 2 2 2 + .
    4 1 2 3 3 1 2 3 . -
    """
    assert default_test_puzzle(puzzle_string, Magnets, Solving.magnets_techniques())


@pytest.mark.skip("skip")
def test_magnets_043():
    puzzle_string = f"""
    043.magnets
    8
    a h h i i l m m 4 3
    a j j k k l q r 3 3
    b n o o p p q r 1 1
    b n s v v A B B 3 3
    c c s w x A C C 1 2
    d t t w x z D D 3 1
    d u u y y z E F 2 3
    e e f f g g E F 1 2
    3 2 4 1 2 1 2 3 + .
    3 2 3 3 1 1 3 2 . -
    """
    assert default_test_puzzle(puzzle_string, Magnets, Solving.magnets_techniques())


@pytest.mark.skip("skip")
def test_magnets_044():
    puzzle_string = f"""
    044.magnets
    8
    a b j j q r s s 3 3
    a b k l q r t t 2 3
    c c k l o o p p 4 3
    d e m m n n F G 3 3
    d e u y z A F G 3 3
    f g u y z A E E 3 4
    f g v x x B D D 2 1
    i i v w w B C C 4 4
    2 1 3 3 4 4 4 3 + .
    0 3 3 4 3 4 3 4 . -
    """
    assert default_test_puzzle(puzzle_string, Magnets, Solving.magnets_techniques())


@pytest.mark.skip("skip")
def test_magnets_045():
    puzzle_string = f"""
    045.magnets
    8
    a i i r r A G G 4 2
    a h q q s A E F 2 3
    b h o p s B E F 3 2
    b g o p t B D D 3 3
    c g n n t C C J 2 3
    c f f m u u H J 3 3
    d d j m v v H I 1 1
    e e j k k l l I 2 3
    3 3 1 1 4 3 2 3 + .
    2 4 1 2 2 3 3 3  . -
    """
    assert default_test_puzzle(puzzle_string, Magnets, Solving.magnets_techniques())


@pytest.mark.skip("skip")
def test_magnets_046():
    puzzle_string = f"""
    046.magnets
    8
    a a c d d e e C 1 2
    b b c o s s B C 2 3
    f n n o t u B D 3 4
    f m p p t u A D 4 2
    g m q v v y A E 2 2
    g l q w w y z E 3 2
    h l r r x x z F 3 2
    h i i j j k k F 2 3
    3 3 2 2 2 2 3 3 + .
    2 4 1 4 2 2 2 3 . -
    """
    assert default_test_puzzle(puzzle_string, Magnets, Solving.magnets_techniques())


@pytest.mark.skip("skip")
def test_magnets_047():
    puzzle_string = f"""
    047.magnets
    8
    a g g h h r s t 3 2
    a i o o q r s t 2 2
    b i p p q A A K 2 3
    b j j k k I J K 1 1
    c c l l C I J L 2 2
    d m m B C H H L 1 1
    d n n B D E F F 2 1
    e e f f D E G G 2 3
    3 2 2 1 1 3 1 2 + .
    1 4 1 1 2 2 1 3  . -
    """
    assert default_test_puzzle(puzzle_string, Magnets, Solving.magnets_techniques())


@pytest.mark.skip("skip")
def test_magnets_048():
    puzzle_string = f"""
    048.magnets
    8
    a j j o p p r s ? 3
    a k l o q q r s 2 ?
    b k l n t t u u ? 4
    b m m n A D D G 1 ?
    c c d d A E F G ? 2
    e B B C C E F K 3 ?
    e H H I I J J K ? 1
    f f g g h h i i 2 ?
    ? 2 ? 4 ? 1 ? 2 + .
    2 ? 2 ? 1 ? 3 ? . -
    """
    assert default_test_puzzle(puzzle_string, Magnets, Solving.magnets_techniques())


@pytest.mark.skip("skip")
def test_magnets_049():
    puzzle_string = f"""
    049.magnets
    8
    a o o p p F G G 3 2
    a n q q s F H H 3 3
    b n r r s D D E 1 1
    b m m t u u B E 1 3
    c c h t v w B C 1 2
    d f h k v w A C 2 2
    d f g k l l A Z 3 1
    e e g i i j j Z 2 2
    2 2 2 3 2 1 2 2 + .
    3 2 2 1 1 3 2 2 . -
    """
    assert default_test_puzzle(puzzle_string, Magnets, Solving.magnets_techniques())


@pytest.mark.skip("skip")
def test_magnets_050():
    puzzle_string = f"""
    050.magnets
    8
    a c c d f f g g 3 2
    a b b d e e D E 3 3
    h h s t u u D E 0 2
    f f s t v B B C 3 2
    i p q q v A A C 2 3
    i p r r w x y y 3 2
    j k l m w x z z 3 4
    j k l m n n o o 3 2
    4 2 3 1 3 2 2 3 + .
    3 3 2 2 3 2 1 4 . -
    """
    assert default_test_puzzle(puzzle_string, Magnets, Solving.magnets_techniques())


@pytest.mark.skip("skip")
def test_magnets_051():
    puzzle_string = f"""
    051.magnets
    8
    a a c d d y z z 2 2
    b b c u x y A A 4 4
    e t t u x B B E 4 4
    e s s v w C D E 4 4
    f r r v w C D F 4 3
    f o o p p q q F 2 3
    g h i i k l m m 2 2
    g h j j k l n n 3 3
    3 3 4 3 2 4 3 3 + .
    3 4 2 3 3 4 4 2 . -
    """
    assert default_test_puzzle(puzzle_string, Magnets, Solving.magnets_techniques())


@pytest.mark.skip("skip")
def test_magnets_052():
    puzzle_string = f"""
    052.magnets
    8
    a a b b e g g h 2 4
    c c d d e f f h 4 2
    i q r r s s t t 3 3
    i q u u v v w w 3 3
    j j p A A D G H 2 4
    k k p B C D G H 3 2
    l o o B C E F I 3 3
    l m m n n E F I 3 2
    3 4 4 4 1 2 1 4 + .
    3 4 4 3 3 1 2 3 . -
    """
    assert default_test_puzzle(puzzle_string, Magnets, Solving.magnets_techniques())


@pytest.mark.skip("skip")
def test_magnets_053():
    puzzle_string = f"""
    053.magnets
    8
    a a b b c c d d 3 3
    e q q s t t u u 1 2
    e r r s w x x z 4 3
    f f v v w y y z 2 2
    g g A B C C E F 4 4
    h j A B D D E F 3 2
    h j k l l m m p 2 3
    i i k n n o o p 4 4
    3 2 4 1 3 3 4 3 + .
    3 2 3 3 2 3 3 4 . -
    """
    assert default_test_puzzle(puzzle_string, Magnets, Solving.magnets_techniques())


@pytest.mark.skip("skip")
def test_magnets_054():
    puzzle_string = f"""
    054.magnets
    8
    a a b b q r r t 4 4
    c n n p q s s t 4 4
    c o o p u u v v 2 2
    d w x x C D D F 3 3
    d w y z C E E F 2 3
    e e y z A A B B 3 2
    f g g i j k k m 2 3
    f h h i j l l m 4 3
    2 4 2 4 3 4 1 4 + .
    3 3 3 3 4 1 4 3 . -
    """
    assert default_test_puzzle(puzzle_string, Magnets, Solving.magnets_techniques())


@pytest.mark.skip("skip")
def test_magnets_055():
    puzzle_string = f"""
    055.magnets
    8
    a u u x z z A A 3 1
    a v w x B B C C 2 3
    b v w y y D E E 4 3
    b c c d d D F G 1 4
    e e f f g g F G 2 1
    h i l l m m n n 3 2
    h i o q q r s t 2 3
    k k o p p r s t 3 3
    4 2 1 4 1 1 3 4 + .
    3 2 2 3 2 1 3 4 . -
    """
    assert default_test_puzzle(puzzle_string, Magnets, Solving.magnets_techniques())


@pytest.mark.skip("skip")
def test_magnets_056():
    puzzle_string = f"""
    056.magnets
    8
    a a b b c c d d 4 4
    e k l r r s s D 3 4
    e k l t t B C D 3 1
    f f m m u B C F 1 1
    g g n o u E E F 2 2
    h h n o v v w w 2 3
    i i p p x y z z 3 2
    j j q q x y A A 3 4
    4 2 2 3 3 1 4 2 + .
    3 3 2 2 3 1 3 4 . -
    """
    assert default_test_puzzle(puzzle_string, Magnets, Solving.magnets_techniques())


@pytest.mark.skip("skip")
def test_magnets_057():
    puzzle_string = f"""
    057.magnets
    8
    a f f h i i j j ? ?
    a g g h A B B D 4 4
    b b z z A C C D 1 1
    c o o p p q q E 2 3
    c r r t u y y E 1 ?
    d d s t u x x F 3 2
    e k s v v w w F ? ?
    e k l l m m n n ? 3
    3 3 ? 1 2 ? ? 3 + .
    3 ? ? ? 2 ? 3 ? . -
    """
    assert default_test_puzzle(puzzle_string, Magnets, Solving.magnets_techniques())


@pytest.mark.skip("skip")
def test_magnets_058():
    puzzle_string = f"""
    058.magnets
    8
    a a b b c c d d ? 2
    e f f g g h h l ? ?
    e i i j j k k  l ? 2
    m m n n o o p  p ? ?
    q s t u v v w w ? 3
    q s t u Y Y G H  3 4
    r x y z z B G H 4 ?
    r x y A A B M M ? ?
    ? 4 1 ? 4 3 2 2 + .
    ? ? 0 ? 2 ? ? 1 . -
    """
    assert default_test_puzzle(puzzle_string, Magnets, Solving.magnets_techniques())


@pytest.mark.skip("skip")
def test_magnets_059():
    puzzle_string = f"""
    059.magnets
    8
    a a b b c c d d 2 ?
    e e g h i j k l ? ?
    f f g h i j k l 3 3
    m n o C C D E E 2 ?
    m n o A B D F F ? 2
    p x x A B G G H 3 4
    p u u v v w w H 4 3
    q q r r s s t t 4 ?
    2 ? 3 2 3 ? ? 2 + .
    ? 3 4 ? 3 ? ? 1 . -
    """
    assert default_test_puzzle(puzzle_string, Magnets, Solving.magnets_techniques())


@pytest.mark.skip("skip")
def test_magnets_060():
    puzzle_string = f"""
    060.magnets
    8
    a a b b c c r s 4 4
    d o p p q q r s 4 4
    d o t u v w x y 3 4
    e e t u v w x y ? ?
    f z z B C C E F ? 2
    f A A B D D E F ? ?
    g h h i i j j n 3 ?
    g k k l l m m n 3 4
    2 3 ? ? ? ? 3 3 + .
    ? ? ? ? ? 1 4 ? . -
    """
    assert default_test_puzzle(puzzle_string, Magnets, Solving.magnets_techniques())


@pytest.mark.skip("skip")
def test_magnets_063():
    puzzle_string = f"""
    063.magnets
    8
    a g g h h w y y ? ?
    a i q q s w z A ? ?
    b i r r s x z A ? 2
    b j j k k x B C 2 2
    c l l s t u B C 3 4
    c m n s t u v v 3 3
    d m n o o p q q 3 3
    d e e f f p r r 3 3
    3 ? 0 ? 3 3 ? 3 + .
    ? ? 1 ? 3 ? ? ? . -
    """
    assert default_test_puzzle(puzzle_string, Magnets, Solving.magnets_techniques())


@pytest.mark.skip("skip")
def test_magnets_082():
    puzzle_string = f"""
    082.magnets
    10
    A A J K L L M M N N 4 3
    B C J K O P P R S T 1 2
    B C D D O Q Q R S T 3 3
    E E U V V W W X X j 5 3
    F F U d e h h i i j 4 5
    G Y Y d e m n o p q 4 4
    G Z c f f m n o p q 4 4
    H Z c g l l r r s s 3 4
    H a a g k t t u u x 2 4
    I I b b k v v w w x 5 3
    5 5 3 5 3 1 3 3 3 4 + .
    5 5 3 5 3 3 1 2 4 4 . -
    """
    assert default_test_puzzle(puzzle_string, Magnets, Solving.magnets_techniques())


@pytest.mark.skip("skip")
def test_magnets_083():
    puzzle_string = f"""
    083.magnets
    10
    a   m   m   o   p   p   s   s   t   u 3 4
    a   l   n   o   q   q   r   r   t   u 5 4
    b   l   n   v   v   H   H   T   T   Z 4 4
    b   k   k   w   w   I   I   R   S   Z 5 5
    c   c   d   d   F   J   J   R   S   W 2 1
    e   j   j   E   F   K   O   Q   Q   W 4 4
    e   i   i   E   G   K   O   P   P   X 3 3
    f   h   D   D   G   L   L   M   N   X 4 3
    f   h   x   y   z   A   B   M   N   V 3 4
    g   g   x   y   z   A   B   C   C   V 3 4
    5   2   2   4   5   5   4   4   2   3 + $
    4   3   3   3   5   4   5   4   2   3 $ -
    """
    assert default_test_puzzle(puzzle_string, Magnets, Solving.magnets_techniques())


@pytest.mark.skip("skip")
def test_magnets_119():
    puzzle_string = f"""
    119.magnets
    10
    A A D E E G H H I I 5 5
    B C D F F G e f f h 4 ?
    B C Y Z a a e g g h 5 4
    J K Y Z b b i i w x ? 4
    J K X X c c j k w x 5 4
    L L W W d d j k v v 4 ?
    M S S V V l n p t u 2 ?
    M R R T U l n p t u ? ?
    N N P T U m o q s s 4 3
    O O P Q Q m o q r r 4 5
    ? 5 ? 5 ? 3 3 5 5 ?
    4 3 ? 4 ? 2 ? 4 5 ?
    """
    assert default_test_puzzle(puzzle_string, Magnets, Solving.magnets_techniques())


@pytest.mark.skip("skip")
def test_magnets_026():
    puzzle_string = f"""
    026.magnets
    6
    a a f g i i ? 3
    b b f g h h ? 3
    c c d d e e ? ?
    j k l m n n 1 2
    j k l m o o ? 1
    p p q q r r ? 2
    2 3 ? 3 ? 3 + .
    3 2 ? 2 ? ? . -
    """
    assert default_test_puzzle(puzzle_string, Magnets, Solving.magnets_techniques())
