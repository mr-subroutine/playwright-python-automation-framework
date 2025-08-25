from milestone1_pytest_basics.player import name_character

def test_player_name():
    count = name_character("Tester18")
    print(f"The count is: {count}")
    assert count <= 8