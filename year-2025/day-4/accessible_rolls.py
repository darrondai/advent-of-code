from collections import deque
# basically mark all of the rolls of paper as entries into a hashmap/hashset
# create a coordinate mapping
# then for each entry, check the 8 adjacent cells, (can use a default return value to make this easier)


def parse_input_into_list(input_file: str) -> list[str]:
    # this assumes that the grid is a n by m matrix
    # n strings of m length
    with open(input_file) as f:
        return [line.strip() for line in f]


def transform_into_set(paper_roll_grid: list[str]):
    paper_rolls = set()

    for row, line in enumerate(paper_roll_grid):
        for col, char in enumerate(line):
            if char == "@":
                paper_rolls.add((row, col))

    return paper_rolls


def calc_reachable_rolls(paper_rolls: set[tuple[int, int]]) -> int:
    def is_reachable(row: int, col: int) -> bool:
        # reachable if number of adjacent rolls < 4
        adjacent_roll_count = 0
        DIRECTIONS = (
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        )

        for row_offset, col_offset in DIRECTIONS:
            if (row + row_offset, col + col_offset) in paper_rolls:
                adjacent_roll_count += 1

        return adjacent_roll_count < 4

    accessible_roll_count = 0
    for row, col in paper_rolls:
        if is_reachable(row, col):
            accessible_roll_count += 1

    return accessible_roll_count


# for part 2, instead of going through all of the paper rolls, one by one
# can use topological sort, but the threshold to add to queue is 3 or less
# instead of just a hashset, store the indegree of each cell as well
# when a node is accessible, remove it and adjust the indegree of its neighbors
# if any of the neighbors then have an indegree below 3, add the neighbor to the queue
# WE do have to be careful about double counting, so only add to queue when indegree drops below threshold
# or we can just remove from the hashmap (probably the more elegant solution)
# whats great about this is that traversal order doesnt matter

# our initial traversal should do the indegree counting
# then we traverse through the hashmap and queue nodes below the threshold
# from then on, we just continue to remove nodes until the queue is empty (convergence)
# to count the number of removed nodes, just increment a counter each time we process a node


def initialize_indegrees_by_roll(
    paper_roll_grid: list[str],
) -> dict[tuple[int, int], int]:
    indegrees_by_roll: dict[tuple[int, int], int] = {}

    # initial traversal, marking the paper rolls
    for row, s in enumerate(paper_roll_grid):
        for col, char in enumerate(s):
            if char == "@":
                indegrees_by_roll[(row, col)] = 0

    # additional traversal through paper rolls, calc indegree
    def calc_indegree(
        cell: tuple[int, int], indegrees_by_roll: dict[tuple[int, int], int]
    ) -> int:
        indegree = 0
        for neighbor in get_neighbors(cell):
            if neighbor not in indegrees_by_roll:
                continue
            indegree += 1
        return indegree

    for roll in indegrees_by_roll:
        indegrees_by_roll[roll] = calc_indegree(roll, indegrees_by_roll)
    return indegrees_by_roll


def get_neighbors(cell: tuple[int, int]) -> list[tuple[int, int]]:
    DIRECTIONS = (
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    )
    row, col = cell
    neighbors = [
        (row + row_offset, col + col_offset) for row_offset, col_offset in DIRECTIONS
    ]
    return neighbors


def topological_removal(indegrees_by_roll: dict[tuple[int, int], int]) -> int:
    THRESHOLD = 4
    removal_count = 0
    queue = deque()
    # initial traversal for adding to queue
    for roll, indegree in indegrees_by_roll.items():
        if indegree >= THRESHOLD:
            continue

        queue.append(roll)

    # spaghetti bc we have to remove when adding to queue
    # doing it in the initial traversal will cause error bc change during iteration
    # doing it in the topological traversal causes errors bc ...
    # some nodes will be double counted before they are visited
    for cell in queue:
        del indegrees_by_roll[cell]

    while queue:
        curr = queue.popleft()
        removal_count += 1

        for neighbor in get_neighbors(curr):
            if neighbor not in indegrees_by_roll:
                continue

            indegrees_by_roll[neighbor] -= 1
            if indegrees_by_roll[neighbor] >= THRESHOLD:
                continue

            # append and remove neighbor to avoid double counting
            queue.append(neighbor)
            del indegrees_by_roll[neighbor]

    return removal_count


def main() -> None:
    input_grid = parse_input_into_list("input.txt")
    paper_rolls = transform_into_set(input_grid)

    print(calc_reachable_rolls(paper_rolls))

    indegrees = initialize_indegrees_by_roll(input_grid)
    print(topological_removal(indegrees))


if __name__ == "__main__":
    main()
