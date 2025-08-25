from milestone1_pytest_basics.player import name_character

def test_player_name():
    count = name_character("Tester18")  # change name_character argument to test names, 8 character max
    print(f"The count is: {count}")
    assert count <= 8