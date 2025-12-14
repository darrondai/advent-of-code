import cafeteria


def test_example_part_1() -> None:
    fresh_id_ranges = [[3, 5], [10, 14], [16, 20], [12, 18]]
    available_ids = [1, 5, 8, 11, 17, 32]

    merged_ranges = cafeteria.sort_and_merge_ranges(fresh_id_ranges)
    print("fresh id ranges:", fresh_id_ranges)
    print("merged ranges:", merged_ranges)

    assert merged_ranges == [[3, 5], [10, 20]]

    fresh_count = cafeteria.naive_hashset(merged_ranges, available_ids)

    assert fresh_count == 3
