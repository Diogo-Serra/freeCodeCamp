#!/usr/bin/env python3
full_dot = '●'
empty_dot = '○'


def create_character(name, strenght, intelligence, charisma):
    if not isinstance(name, str):
        return 'The character name should be a string'
    if not name:
        return 'The character should have a name'
    if len(name) > 10:
        return 'The character name is too long'
    if ' ' in name:
        return 'The character name should not contain spaces'
    if not all(isinstance(stats, int) for stats in (strenght, intelligence, charisma)):
        return 'All stats should be integers'
    if any(stats < 1 for stats in (strenght, intelligence, charisma)):
        return 'All stats should be no less than 1'
    if any(stats > 4 for stats in (strenght, intelligence, charisma)):
        return 'All stats should be no more than 4'
    if sum((strenght, intelligence, charisma)) != 7:
        return 'The character should start with 7 points'
    return (
        f'{name}\n'
        f'STR {full_dot * strenght}{empty_dot * (10 - strenght)}\n'
        f'INT {full_dot * intelligence}{empty_dot * (10 - intelligence)}\n'
        f'CHA {full_dot * charisma}{empty_dot * (10 - charisma)}'
    )


char1 = create_character("Ren", 4, 2, 1)
print(char1)
