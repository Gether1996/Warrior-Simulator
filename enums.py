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
    Red = 1
    Blue = 2
    Yellow = 3
    Green = 4
    Cyan = 5
    Magenta = 6
    Light_Cyan = 7
    Light_Red = 8
    Light_Yellow = 9
    Light_Green = 10
