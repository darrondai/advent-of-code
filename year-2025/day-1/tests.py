from rotation_counting import count_zero_landings, count_zero_passes


def test_part_1():
    pass


def test_part_2():
    INITIAL_POSITION = 50

    dial_rotations = (num for num in [-150])
    zero_passes = count_zero_passes(dial_rotations, INITIAL_POSITION)
    assert zero_passes == 2

    dial_rotations = (num for num in [150])
    zero_passes = count_zero_passes(dial_rotations, INITIAL_POSITION)
    assert zero_passes == 2

    dial_rotations = (num for num in [50, -50])
    zero_passes = count_zero_passes(dial_rotations, INITIAL_POSITION)
    assert zero_passes == 1

    dial_rotations = (num for num in [-50, 50])
    zero_passes = count_zero_passes(dial_rotations, INITIAL_POSITION)
    assert zero_passes == 1

    dial_rotations = (num for num in [50, 50])
    zero_passes = count_zero_passes(dial_rotations, INITIAL_POSITION)
    assert zero_passes == 1

    dial_rotations = (num for num in [-50, -50])
    zero_passes = count_zero_passes(dial_rotations, INITIAL_POSITION)
    assert zero_passes == 1
