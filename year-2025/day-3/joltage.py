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


def smart(digits: str, num_digits: int) -> int:
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


# the basic idea is to take the first n digits from the right
# once we have the first n digits, we can start deciding what to do with the incoming numbers from the left side
# essentially at time we add a digit, we want to make sure that once the digits shift over, that the new starting digit is greater or equal to the previous
# the rest of the digits behind it dont really matter? THEY DO.....

# track the thing we want to remove (they are save to remove once we find an element greater than the left side head?)
# deque plus stack?
# fill deque initially
# once it is full, decide whether or not to add to it by checking if the new element is greater than the left most element in the deque
# if it is, we then remove elements from the dq into the stack (for sure taken if there an)
# thus rightmost element in the dq is the element that we pop and decide if it stays valuable or not

# at the end we just pop from the deque until empty, then pop from the stack until we have enough digits
# the deque should be monotonic decreasing from left to right i.e. [8, 8, 3, 2, 1]
# the stack should be

# if the next element is lesser than the top of the dq, process the dq basically, and push the digits to the stack only if they are greater than the stack top

# maybe the deque gets filled to the max first (may not necessarily be monotonic)
# then at the end, we do a final processing that pops the smaller of the dq.right and stack.top

# stack is monotonic non decreasing left to right?
# whenever we want to insert into it, pop from top until the inserted element is <= stack.top

# the deque should always stay at max capacity, but when we see an element we want to add (aka greater than deque.left), popright and then process into the stack


# at the end, pop from dq left and process into stack until the combined dq and stack length = digits
def scuffed(digits: str, num_digits: int) -> int:
    queue = deque()
    # represents elements that are guaranteed to be taken
    dq = deque()

    # for digit in digits:
    #     if not queue or queue[0] <= digit:
    #         queue.append(digit)

    # if too big, pop and try adding to stack
    #

    # wait... does a single monotonic increasing deque work?
    # we want to replace the right most element that we are greater than
    # no it breaks when the window is too big i.e 5 digits "599411816"
    # we solve this by only popping from stack while dq + stack len is greater than num_digits (though we only pop from stack while dq.left > stack.top)
    # the stack is monotonically increasing at all times
    # the deque is monotonically increasing at most times, except for

    # lets say stack always is monotonically increasing

    # do we just pop the smaller of queue.right and stack.left?
    # no. instead, just insert into stack when queue.right is >= stack
    # and when stack is too big, pop from the end of it??? so its a deque
    # rather than popping from the stack, pop from the queue
    # we basically want the stack to always be taken from that point on
    # queue may not be monotonic, but we can ensure that the elements that we insert are

    # so...
    # regular queue and a monotonic nondecreasing deque (insert if >= leftmost element)
    # the queue is just to contain all of the digits that are being held back by a single digit
    # elements get inserted into the queue, and once it hits capacity, we keep popping the left most element and trying to add insert it into the stack, stopping once we find another element that is smaller than the stack top
    for digit in digits:
        # if len(queue) + len(dq) > num_digits:
        #     queue.append(digit)
        queue.append(digit)

        # while queue isnt empty, insert as many elements from queue into the guaranteed dq
        while queue and (not dq or queue[0] >= dq[-1]):
            dq.append(queue.popleft())
            # if dq is too big, popleft from it (removing smallest element)
            # if len(dq) >

        # once we know that we have enough digits to construct a number, we can start doing interesting things (treating insertion like a monotonic non decreasing queue)
        # if the number is smaller than the first digit in the queue, ignore it

    # final processing of queue elements
    # read left to right (queue + stack) and cast into a integer
    return 0


# we want to ensure that we only remove the smallest digit possible
# within the digits we already have in the dq, we want to remove the first element that is smaller than


# intuition is that we want to get rid of the left most digit that is smaller than its right neighbor (guarantees an increase)
# the neighbors should update after removal
# basically we go through the string repeated remove the left most digit that is smaller than its right neighbor

# what if we just started from the left side and used a monotonic nonincreasing stack? EERRRR pop from stack until the stack[-1] >= curr digit
# BUT we want to make sure that we have enought digits to make a number, so once we have popped the max amount of numbers (total batteries in bank = batteries popped + batteries in stack + batteries left) we just default to the stack + remaining batteries


def calc_max_voltage_part_2(battery_bank: str, num_digits: int) -> int:
    max_voltage = []
    batteries_left = len(battery_bank)
    for digit in battery_bank:
        while max_voltage and digit > max_voltage[-1] and batteries_left > num_digits:
            max_voltage.pop()
            batteries_left -= 1
        if len(max_voltage) == num_digits:
            batteries_left -= 1
            continue
        max_voltage.append(digit)
        print("".join(max_voltage))

    # 4589185, 4 digits
    # 4 -> 5 -> 8 -> 9 -> 9185
    # 3826134, 4 digits
    # 3 -> 8 -> 82 -> 86 -> 861 -> 8634
    # 123123123, 2 digits
    # 1 -> 2 -> 3 -> 31 -> 32 -> 33 -> 33 -> 33 -> 333????
    # edge case of thing being too full, solve by just taking the not adding if the voltage is full

    # max_voltage.extend()
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


if __name__ == "__main__":
    main()
