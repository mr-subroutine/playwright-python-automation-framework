total_health = 12
is_dead = False

def take_damage(a, b, hit_points=None):
    damage_given = a + b
    hit_points -= damage_given
    return a + b

def remove_damage(a, b):
    return a - b

def critical_hit(a, b):
    return a * b

def blocked(a, b):
    return a / b

def missed_hit(a):
    a = 0
    return 0

def attack(a, b):
    return a + b

def health(total_player_health, damage):
    if damage > total_player_health:
        return True
    else:
        return False
