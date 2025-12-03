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


def smart(digits: str) -> int:
    # better way is to use a monotonic nonincreasing deque?
    # OR just use two pointers
    # but i will use deque just in case part 2 fucks me (3 digits+)

    # start from the back
    # push into the deque
    # technically we can just use the string digits, and then cast at the end

    # hmm maybe two parts
    # basically we always want to take the largest number from the right
    # the numbers will always be taken ASSUMING we have enough digits in the dq
    # but as soon as we find a number that is lesser than the

    # maybe we use two deques
    # the first one is the guaranteed

    # maybe not monotonic, but same idea
    # fill the dq until full
    # pop from right side of dq when it is full and new digit > left

    # IT IS ONLY WORTH REPLACING A DIGIT FROM THE RIGHT
    # IF IT IS GREATER THAN THE LEFTMOST RIGHT DIGIT
    # 53723413
    # 13 -> 43 -> 74 two digits
    # 413 -> 741 three digits

    # 534116
    # 16 -> 46 -> 54 (SHOULD BE 56, so we need to split the things)
    # basically we always add the larger number to the right side
    # so there is a monotonic decreasing queue on the right side, with a max size of digits
    # if we hit a number lesser than the right side, we have a second buffer
    # this dq buffer can be used when size of right queue is less than capacity
    # dq and q lengths should add up to digits number
    # we always insert into left side of dq
    # then if the q is empty or dq right is greater than q top, pop dq right and add to q left
    # when dq + q are full
    # pop elements from dq.right until dq.right >= q.left, then insert as many as possible into q
    # if q is too big, can safely pop from right side of q, since we know it is monotonic descreasing
    # once dq.right < q.left again OR dq is empty

    # everytime there is a decrease going left, start of a new stack

    # dq = deque()
    # buffer = deque()
    # right_taken = deque()
    # num_digits = 2
    # for digit in reversed(digits):
    #     if not buffer or digit > buffer[0]:
    #         buffer.appendleft(digit)

    #     if len(buffer) + len(right_taken) > num_digits:
    #         #

    #     # while not right_taken or adf

    # max_voltage = int()
    # return max_voltage
    return 0


def accumulate_max_voltages_part_2(battery_banks: list[str]) -> int:
    total_voltage = 0

    for bank in battery_banks:
        total_voltage += smart(bank)

    return total_voltage


def main() -> None:
    INPUT_FILE = "input.txt"
    battery_banks = parse_input(INPUT_FILE)

    print(accumulate_max_voltages(battery_banks))


if __name__ == "__main__":
    main()
