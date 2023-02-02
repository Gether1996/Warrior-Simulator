import math
from config import *


class CombatHelper:

    @classmethod
    def get_damage_reduction(cls, armor_value):
        result = 100 * math.log(armor_value * 0.01 + 1)
        return round(result, 2) if result < config_MaximumArmorReduction else 90
