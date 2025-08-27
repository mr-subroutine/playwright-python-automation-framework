

def player_name_count(name: str):
    count = 0
    for char in name:
        count += 1
    return count

def return_player_name_for_input_check(name: str):
    name = name.strip()
    return name