from milestone1_pytest_basics.test_rpg_calculator import take_damage, remove_damage, critical_hit, missed_hit, attack


def test_take_damage_pass():
    assert take_damage(5, 5) == 10
    print("Player lost 10 HP.}.  Test Passed.")


def test_remove_damage():
    assert remove_damage(5, 1) == 4
    print("Player was healed.  Test Passed.")


def test_critical_hit():
    assert critical_hit(5, 5) == 25
    print("Player got a critical hit!  Test Passed.")


def test_missed_hit():
    assert missed_hit(25) == 0
    print("The enemy has missed a hit.  Test Passed.")


def test_attack():
    assert attack(10, 8) == 18
    print("Player attacks for 18 damage.  Test Passed.")