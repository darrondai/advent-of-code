from joltage import accumulate_max_voltages, accumulate_max_voltages_part_2


def test_example_part_1():
    battery_banks = [
        "987654321111111",
        "811111111111119",
        "234234234234278",
        "818181911112111",
    ]
    assert accumulate_max_voltages(battery_banks) == 357


def test_example_part_2():
    battery_banks = [
        "987654321111111",
        "811111111111119",
        "234234234234278",
        "818181911112111",
    ]
    assert accumulate_max_voltages_part_2(battery_banks) == 3121910778619
