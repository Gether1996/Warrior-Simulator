from enum import Enum


class Races(Enum):
    Human = 1
    Elf = 2
    Dwarf = 3
    Orc = 4


class Schedule(Enum):
    Freeday = 1
    Recruitment = 2
    Teamgame = 3
    Duel = 4
    Freeforall = 5


class Traits(Enum):
    Strong = 1
    Weak = 2
    Nimble = 3
    Sluggish = 4
    Vigorous = 5
    Fragile = 6
    Blessed = 7
    Unfortunate = 8


class Colors(Enum):
    red = 1
    blue = 2
    yellow = 3
    green = 4
    cyan = 5
    magenta = 6
    light_cyan = 7
    light_red = 8
    light_yellow = 9
    light_green = 10
