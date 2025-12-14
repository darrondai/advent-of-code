# first intuition is that this is a unionfind / dsu problem
# we want to be able to check if the available ingredient id
# is part of the "fresh" set
# we can model this as a a single set

# actually, we may not even need the union find
# we can minimize storage by just

# instead of storing each individual id, we should store the ranges
# merging overlapping ranges could do something?
# does binary search make a difference

# hmm maybe we sort and merge intervals
# then binary search for the ids?

# don't think about the first part too hard
# (stop trying to predict how it will change the problem)

# lets just do hashsets for now, add each fresh id into the set


def parse_input(input_file: str) -> tuple[list[list[int]], list[int]]:
    fresh_id_ranges = []
    available_ids = []

    with open(input_file) as f:
        for line in f:
            line = line.strip()
            if not line:
                # empty line between ranges and available ids
                continue
            if "-" in line:
                # split line by - character to get the two ints
                fresh_id_ranges.append([int(id) for id in line.split("-")])
            else:
                # otherwise just append the int value of the line (single id)
                available_ids.append(int(line))

    return fresh_id_ranges, available_ids


def sort_and_merge_ranges(fresh_id_ranges: list[list[int]]) -> list[list[int]]:
    # sort in increasing order, start then end hierarchy
    fresh_id_ranges.sort()

    # merge the intervals to avoid going through dupes in the loop
    merged_ranges = []
    merge_start, merge_end = fresh_id_ranges[0]

    for start, end in fresh_id_ranges[1:]:
        # if the start come after curr_end
        # merge the intervals by updating curr_end to max(curr_end, end)

        # otherwise, stop this the current interval and start a new one
        # the new one will be the start, end
        if merge_end < start:
            merged_ranges.append([merge_start, merge_end])
            merge_start, merge_end = start, end
            continue

        merge_end = max(merge_end, end)

    # final range completion
    merged_ranges.append([merge_start, merge_end])

    return merged_ranges


def naive_hashset(fresh_id_ranges: list[list[int]], available_ids: list[int]) -> int:
    fresh_ids = set()
    # go through all ranges, and add every single number between (inclusive) into a hashset
    for start, end in fresh_id_ranges:
        for id in range(start, end + 1):
            fresh_ids.add(id)

    # go through all available ids, and count the number that are in the fresh set
    fresh_count = 0
    for id in available_ids:
        if id in fresh_ids:
            fresh_count += 1

    return fresh_count


def main() -> None:
    INPUT_FILE = "input.txt"
    fresh_id_ranges, available_ids = parse_input(INPUT_FILE)
    merged_id_ranges = sort_and_merge_ranges(fresh_id_ranges)
    print(len(fresh_id_ranges))
    print(len(merged_id_ranges))
    print(len(available_ids))

    # count = naive_hashset(merged_id_ranges, available_ids)
    # print(count)


if __name__ == "__main__":
    main()
