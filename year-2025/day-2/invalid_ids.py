import math
from time import perf_counter_ns


def parse_input(input_file: str) -> list[list[int]]:
    ranges = []
    with open(input_file) as f:
        ranges_string = f.readline().strip()

        for range in ranges_string.split(","):
            start, end = range.split("-")
            ranges.append([int(start), int(end)])

    return ranges


# naive solution is just to iterate through the range, and check if each number is a repeated sequence
def is_repeated_sequence(id_number: int) -> bool:
    digits = str(id_number)
    n = len(digits)
    # return true if both:
    # 1. even number of digits
    # 2. first half matches second half
    return n % 2 == 0 and digits[: n // 2] == digits[n // 2 :]


def calc_sum_invalid_ids(ranges: list[list[int]]) -> int:
    sum = 0

    for start, end in ranges:
        for id_number in range(start, end + 1):
            if is_repeated_sequence(id_number):
                # print(id_number)
                sum += id_number

    return sum


# IS THERE A BETTER WAY???
# HOW CAN WE GENERATE THE INVALID IDS WITHIN A RANGE
def get_digit_count(number: int) -> int:
    # the number of digits = floor(log10(number)) + 1
    return math.floor(math.log10(number)) + 1


def sum_invalid_ids_in_range(start: int, end: int) -> int:
    # our goal is to find repeated sequences
    # so just try building sequences from the first half
    # sequence length is maxed /out at len(number) // 2
    # add 1 at a time to the sequence (so we traverse all valid numbers)
    # return sum as soon as we hit a number too big AKA the number is > the end
    total = 0

    # get the first half of start, that is the starting sequence
    # as soon as we get to a number that is greater than end, return
    # edge case of start being less that 2 digits long, auto to 1

    digits = str(start)
    if len(digits) < 2:
        sequence = 1
    else:
        sequence = int(digits[: len(digits) // 2])

    id_number = sequence * (10 ** get_digit_count(sequence)) + sequence

    # need to add to sequence when the start is too small as well
    # basically we take the max of the two halves of the start number as the starting sequence
    # will only happen max one time bc adding 1 to the last digit in sequence will allow next
    # ACTUALLY MAY HAPPEN MORE THAN ONCE
    while id_number < start:
        sequence += 1
        id_number = sequence * (10 ** get_digit_count(sequence)) + sequence

    # add 1 to the sequence until the repeated sequence is > end
    while id_number < end:
        total += id_number
        # iterate and calc next repeated sequence number
        sequence += 1
        id_number = sequence * (10 ** get_digit_count(sequence)) + sequence

    return total


def calc_sum_invalid_ids_smart(ranges: list[list[int]]) -> int:
    total = 0
    for start, end in ranges:
        total += sum_invalid_ids_in_range(start, end)

    return total


def main() -> None:
    INPUT_FILE = "input.txt"
    ranges = parse_input(INPUT_FILE)

    print(ranges)

    # print("sum of invalid ids:", calc_sum_invalid_ids(ranges))
    start_time = perf_counter_ns()
    naive = calc_sum_invalid_ids(ranges)
    end_time = perf_counter_ns()
    print("naive approach finished in: ", end_time - start_time, "ns")
    print(naive)

    # print("smarter way:", calc_sum_invalid_ids_smart(ranges))
    start_time = perf_counter_ns()
    smart = calc_sum_invalid_ids_smart(ranges)
    end_time = perf_counter_ns()
    print("smart approach finished in: ", end_time - start_time, "ns")
    print(smart)


if __name__ == "__main__":
    main()
