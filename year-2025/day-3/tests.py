from joltage import (
    accumulate_max_voltages,
    accumulate_max_voltages_part_2,
    naive,
    calc_max_voltage_part_2,
)


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

    expected_voltages = [987654321111, 811111111119, 434234234278, 888911112111]

    for bank, expected in zip(battery_banks, expected_voltages):
        assert calc_max_voltage_part_2(bank, 12) == expected

    assert accumulate_max_voltages_part_2(battery_banks, 12) == 3121910778619


def test_battery_logic():
    battery_bank = "123123123"
    num_digits = 2
    assert calc_max_voltage_part_2(battery_bank, num_digits) == 33

    battery_bank = "123123123"
    # queue: ... [2,3,1,2,3] -> [2,3,1,2,3] -> [3,3,1,2,3]
    # stack: ... [] -> [] -> [3] -> [3] -> [3] -> [3]
    num_digits = 5
    assert calc_max_voltage_part_2(battery_bank, num_digits) == 33123
