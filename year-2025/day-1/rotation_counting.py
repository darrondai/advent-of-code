from collections.abc import Generator


def generate_rotations(input_file: str) -> Generator[int]:
    with open(input_file) as f:
        for line in f:
            # each line is of format [LR]d+\n
            stripped_line = line.strip()

            # first char is the direction
            direction = -1 if stripped_line[0] == "L" else 1
            # second and onwards is the number
            magnitude = int(stripped_line[1:])
            yield direction * magnitude


def count_zero_landings(dial_rotations: Generator[int], initial_position: int) -> int:
    # the password is the number of times the dial is left pointing at 0 after any rotation in the sequence

    position = initial_position
    zero_landings = 0

    # for each rotation, we add it to the position
    # left rotations are counted as negative, right as positive
    # whenever position % 100 == 0, add 1 to count
    for rotation in dial_rotations:
        position = (position + rotation) % 100
        if position == 0:
            zero_landings += 1

    return zero_landings


def count_zero_passes(dial_rotations: Generator[int], initial_position: int) -> int:
    # instead of only counting when the rotation finishes
    # count whenever we pass/land on 0
    # so we have to divide in addition to mod
    # when magnitude is greater than 100, just add magnitude/100 passes
    # but the edge case is when they are less than 100 and cause a 0 pass
    # this only occurs when we wrap around
    # i.e. the new position is lesser than the previous, given a right/positive rotation
    # or the new position > prev, given a left/negative rotation

    # -960 vs +960, initial position of 50
    # 90, 9 + 1 passes (have to deal with negative mod)
    # 10, 9 + 1 passes (easy division/mod)
    # i think we can use division for number of passes
    # and then use mod to get the final 0-99 positive adjustment
    # this final adjustment is then subject to the rule outlined above
    # negative rotation causing an increase means +1
    # positive rotation causing a decrease means +1

    position = initial_position
    zero_passes = 0

    for rotation in dial_rotations:
        prev_position = position
        # calc full rotations with division
        # AHAHAHAHAHAHAH FLOOR DIVISION WITH NEGATIVE NUMBERS DOESNT GO TOWARDS 0
        full_rotations = abs(rotation) // 100
        zero_passes += full_rotations

        # calc new position
        position = (prev_position + rotation) % 100
        # edge cases of landing on 0 exactly
        # starting at 0 causes the left check to be double counted, so skip it
        if prev_position == 0:
            continue
        # ending at 0 counts as a pass, so count it
        elif position == 0:
            zero_passes += 1
        # any other possibility means we can check normally
        elif rotation < 0 and position > prev_position:
            zero_passes += 1
        elif rotation > 0 and position < prev_position:
            zero_passes += 1
        # the case of a 0 rotation is covered by the full_rotations calc, and is ignored

    return zero_passes


def main() -> None:
    input_file = "input.txt"

    # initial position of 50
    INITIAL_POSITION = 50

    # part 1
    dial_rotations = generate_rotations(input_file)
    zero_landings = count_zero_landings(dial_rotations, INITIAL_POSITION)
    print("part-1:", zero_landings)

    # part 2
    dial_rotations = generate_rotations(input_file)
    zero_passes = count_zero_passes(dial_rotations, INITIAL_POSITION)
    print("part-2:", zero_passes)


if __name__ == "__main__":
    main()
