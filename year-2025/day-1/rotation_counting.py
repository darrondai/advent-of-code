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


def count_zero_points(dial_rotations: Generator[int]) -> int:
    # the password is the number of times the dial is left pointing at 0 after any rotation in the sequence

    # initial position of 50
    INITIAL_POSITION = 50
    position = INITIAL_POSITION
    zero_count = 0

    # for each rotation, we add it to the position
    # left rotations are counted as negative, right as positive
    # whenever position % 100 == 0, add 1 to count
    for rotation in dial_rotations:
        position = (position + rotation) % 100
        if position == 0:
            zero_count += 1

    return zero_count


def main(input_file: str) -> None:
    dial_rotations = generate_rotations(input_file)
    zero_points = count_zero_points(dial_rotations)
    print(zero_points)


if __name__ == "__main__":
    main("input.txt")
