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