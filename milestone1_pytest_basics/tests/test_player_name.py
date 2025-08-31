from milestone1_pytest_basics.player import player_name_count, return_player_name_for_input_check


def test_player_name_max_characters():
    count = player_name_count("Tester7")  # change name_character argument to test names, 8 character max
    print(f"The count is: {count}")
    assert count <= 8


def test_player_name_required_characters():
    name_count = 0
    name = return_player_name_for_input_check("One")  # change name_character argument must have name, fails when no named entered.

    for char in name:
        name_count += 1
        print(f"Required Test: The count is: {name_count}")

    assert name_count > 0