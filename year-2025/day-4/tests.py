from accessible_rolls import (
    transform_into_set,
    calc_reachable_rolls,
    initialize_indegrees_by_roll,
    topological_removal,
)


def test_example_part_1():
    grid = [
        "..@@.@@@@.",
        "@@@.@.@.@@",
        "@@@@@.@.@@",
        "@.@@@@..@.",
        "@@.@@@@.@@",
        ".@@@@@@@.@",
        ".@.@.@.@@@",
        "@.@@@.@@@@",
        ".@@@@@@@@.",
        "@.@.@@@.@.",
    ]

    paper_rolls = transform_into_set(grid)

    result = calc_reachable_rolls(paper_rolls)

    assert result == 13


def test_example_part_2():
    grid = [
        "..@@.@@@@.",
        "@@@.@.@.@@",
        "@@@@@.@.@@",
        "@.@@@@..@.",
        "@@.@@@@.@@",
        ".@@@@@@@.@",
        ".@.@.@.@@@",
        "@.@@@.@@@@",
        ".@@@@@@@@.",
        "@.@.@@@.@.",
    ]

    indegrees = initialize_indegrees_by_roll(grid)

    result = topological_removal(indegrees)

    assert result == 43
