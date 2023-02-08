from interaction import Interaction


def tests():
    test_get_pair()
    test_get_opposite_pair()
    opposite_tests()


def opposite_tests():
    interaction = Interaction()

    assert interaction.opposite(1) == 4, "Output should be 4"
    assert interaction.opposite(4) == 1, "Output should be 1"
    assert interaction.opposite(2) == 7, "Output should be 7"
    assert interaction.opposite(7) == 2, "Output should be 2"
    assert interaction.opposite(3) == 6, "Output should be 6"
    assert interaction.opposite(6) == 3, "Output should be 3"
    assert interaction.opposite(0) == 5, "Output should be 5"
    assert interaction.opposite(5) == 0, "Output should be 0"


def test_get_pair():
    interaction = Interaction()

    assert interaction.get_pair(0) == 0
    assert interaction.get_pair(1) == 0
    assert interaction.get_pair(2) == 1
    assert interaction.get_pair(3) == 1
    assert interaction.get_pair(4) == 2
    assert interaction.get_pair(5) == 2
    assert interaction.get_pair(6) == 3
    assert interaction.get_pair(7) == 3


def test_get_opposite_pair():
    interaction = Interaction()

    assert interaction.get_opposite_pair(0) == 2
    assert interaction.get_opposite_pair(1) == 2
    assert interaction.get_opposite_pair(2) == 3
    assert interaction.get_opposite_pair(3) == 3
    assert interaction.get_opposite_pair(4) == 0
    assert interaction.get_opposite_pair(5) == 0
    assert interaction.get_opposite_pair(6) == 1
    assert interaction.get_opposite_pair(7) == 1


'''
   (0   1)
7           2
6           3
   (5   4)

1) Find the opposite pairing
2) Find the member of that pair which is on the same side as me
'''
