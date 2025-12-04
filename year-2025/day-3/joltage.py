from collections import deque


def parse_input(input_file: str) -> list[str]:
    with open(input_file) as f:
        return [line.strip() for line in f]


def naive(digits: str) -> int:
    # naive way is to try all possible combos within the bank
    max_voltage = ""

    n = len(digits)
    for i in range(n):
        for j in range(i + 1, n):
            max_voltage = max(max_voltage, digits[i] + digits[j])

    return int(max_voltage)


def accumulate_max_voltages(battery_banks: list[str]) -> int:
    total_voltage = 0

    for bank in battery_banks:
        total_voltage += naive(bank)

    return total_voltage


# TEST CASES
# 4589185, 4 digits
# 4 -> 5 -> 8 -> 9 -> 9185
# 3826134, 4 digits
# 3 -> 8 -> 82 -> 86 -> 861 -> 8634
# 123123123, 2 digits
# 1 -> 2 -> 3 -> 31 -> 32 -> 33 -> 33 -> 33 -> 333????
# edge case of thing being too full, solve by just taking the not adding if the voltage is full


def calc_max_voltage_part_2(battery_bank: str, num_digits: int) -> int:
    # intuition is that we want to get rid of the left most digit that is smaller than its right neighbor (guarantees an increase)
    # the neighbors should update after removal
    # basically we go through the string repeated remove the left most digit that is smaller than its right neighbor

    # what if we just started from the left side and used a monotonic nonincreasing stack? EERRRR pop from stack until the stack[-1] >= curr digit
    # BUT we want to make sure that we have enought digits to make a number, so once we have popped the max amount of numbers (total batteries in bank = batteries popped + batteries in stack + batteries left) we just default to the stack + remaining batteries

    max_voltage = []
    batteries_left = len(battery_bank)

    for digit in battery_bank:
        # pop until top of stack is greater or equal to current digit,
        # OR until popping batteries would make us not be able to formulate a voltage of the proper length
        while (
            max_voltage
            and digit > max_voltage[-1]
            and len(max_voltage) + batteries_left > num_digits
        ):
            max_voltage.pop()

        batteries_left -= 1
        # need this to avoid adding dupes when the voltage stack is already full
        if len(max_voltage) == num_digits:
            continue
        max_voltage.append(digit)

    return int("".join(max_voltage))


def accumulate_max_voltages_part_2(battery_banks: list[str], num_digits: int) -> int:
    total_voltage = 0

    for bank in battery_banks:
        total_voltage += calc_max_voltage_part_2(bank, num_digits)

    return total_voltage


def main() -> None:
    INPUT_FILE = "input.txt"
    battery_banks = parse_input(INPUT_FILE)

    print(accumulate_max_voltages(battery_banks))

    NUM_DIGITS = 12
    print(accumulate_max_voltages_part_2(battery_banks, 12))


if __name__ == "__main__":
    main()
