from math import floor
from config import *
from enums import Races, Traits
from items import *
from statistics import GladiatorStatistics


class Gladiator(Serializable):

    def __init__(self):
        self.m_name = ""
        self.m_race = ...
        self.m_traits = []
        self.m_strength = ...
        self.m_agility = ...
        self.m_vitality = ...
        self.m_luck = ...
        self.m_max_health = ...
        self.m_gold = ...
        self.m_current_health = ...
        self.m_armor = None
        self.m_weapon = None
        self.m_GladiatorStatistics = ...

    def pick_random_race(self):
        index = random.randint(1, len(Races))
        self.m_race = Races(index)

    def add_stats_based_on_race(self):
        if self.m_race.value == 1:
            self.m_strength += config_HumanStrengthBonus
            self.m_agility += config_HumanAgilityBonus
            self.m_vitality += config_HumanVitaliyBonus
            self.m_luck += config_HumanLuckBonus
        if self.m_race.value == 2:
            self.m_strength += config_ElfStrengthBonus
            self.m_agility += config_ElfAgilityBonus
            self.m_vitality += config_ElfVitaliyBonus
            self.m_luck += config_ElfLuckBonus
        if self.m_race.value == 3:
            self.m_strength += config_DwarfStrengthBonus
            self.m_agility += config_DwarfAgilityBonus
            self.m_vitality += config_DwarfVitaliyBonus
            self.m_luck += config_DwarfLuckBonus
        if self.m_race.value == 4:
            self.m_strength += config_OrcStrengthBonus
            self.m_agility += config_OrcAgilityBonus
            self.m_vitality += config_OrcVitaliyBonus
            self.m_luck += config_OrcLuckBonus

    def add_traits(self):
        traitPairs = []
        for traitIndex in range(len(Traits)):
            if traitIndex % 2 == 1:
                traitPairs.append(([traitIndex, traitIndex + 1]))

        for traitItemA, traitItemB in traitPairs:
            if random.randint(1, 100) <= config_GladiatorTraitRollChance:
                if random.randint(1, 100) <= 50:
                    self.m_traits.append(Traits(traitItemA))
                else:
                    self.m_traits.append(Traits(traitItemB))

    def add_effects_from_traits(self):
        for trait in self.m_traits:
            if trait.name == "Strong":
                self.m_strength += config_TraitStrengthBonus
            elif trait.name == "Weak":
                self.m_strength += config_TraitStrengthPenalty
            elif trait.name == "Nimble":
                self.m_agility += config_TraitAgilityBonus
            elif trait.name == "Sluggish":
                self.m_agility += config_TraitAgilityPenalty
            elif trait.name == "Vigorous":
                self.m_vitality += config_TraitVitalityBonus
            elif trait.name == "Fragile":
                self.m_vitality += config_TraitVitalityPenalty
            elif trait.name == "Blessed":
                self.m_luck += config_TraitLuckBonus
            elif trait.name == "Unfortunate":
                self.m_luck += config_TraitLuckPenalty

    def generate_default_gladiator(self):
        self.m_name = random.choice(config_GladiatorNames)
        self.m_strength = config_GladiatorBaseStat + random.randint(0, config_GladiatorStatRollRange)
        self.m_agility = config_GladiatorBaseStat + random.randint(0, config_GladiatorStatRollRange)
        self.m_vitality = config_GladiatorBaseStat + random.randint(0, config_GladiatorStatRollRange)
        self.m_luck = config_GladiatorBaseStat + random.randint(0, config_GladiatorStatRollRange)
        self.m_max_health = self.get_max_health()
        self.m_current_health = self.get_max_health()
        self.m_gold = config_Gold

        self.pick_random_race()
        self.add_stats_based_on_race()
        self.add_traits()
        self.add_effects_from_traits()
        gladiatorStatistics = GladiatorStatistics()
        self.m_GladiatorStatistics = gladiatorStatistics

    def save_object(self):
        data = {
            "m_name": self.m_name,
            "m_race": self.m_race.value,
            "m_traits": [],
            "m_armor": ...,
            "m_weapon": ...,
            "m_strength": self.m_strength,
            "m_agility": self.m_agility,
            "m_vitality": self.m_vitality,
            "m_luck": self.m_luck,
            "m_max_health": self.m_max_health,
            "m_current_health": self.m_current_health,
            "m_gold": self.m_gold,
            "m_gladiator_statistics": self.m_GladiatorStatistics.save_object()
        }
        for trait in self.m_traits:
            data["m_traits"].append(trait.value)
        if self.m_armor is None:
            data["m_armor"] = None
        else:
            data["m_armor"] = self.m_armor.save_object()
        if self.m_weapon is None:
            data["m_weapon"] = None
        else:
            data["m_weapon"] = self.m_weapon.save_object()
        return data

    def load_object(self, data):
        self.m_name = data["m_name"]
        for traitData in data["m_traits"]:
            self.m_traits.append(Traits(traitData))
        self.m_strength = data["m_strength"]
        self.m_agility = data["m_agility"]
        self.m_vitality = data["m_vitality"]
        self.m_luck = data["m_luck"]
        self.m_max_health = data["m_max_health"]
        self.m_current_health = data["m_current_health"]
        self.m_gold = data["m_gold"]
        self.m_race = Races(data["m_race"])

        if data["m_armor"] is None:
            self.m_armor = None
        else:
            armor = Armor()
            armor.load_object(data["m_armor"])
            self.m_armor = armor

        if data["m_weapon"] is None:
            self.m_weapon = None
        else:
            weapon = Weapon()
            weapon.load_object(data["m_weapon"])
            self.m_weapon = weapon
        self.m_GladiatorStatistics = GladiatorStatistics()
        self.m_GladiatorStatistics.load_object(data["m_gladiator_statistics"])

    def get_damage_range(self):
        base_damage_lower = floor(self.m_strength * config_GladiatorStrengthLowerDmgRng)
        base_damage_upper = floor(self.m_strength * config_GladiatorStrengthUpperDmgRng)
        weapon_damage_scaled_lower = [1 + self.m_strength * 0.05] * self.m_weapon.m_damage_lower
        weapon_damage_scaled_upper = [1 + self.m_strength * 0.05] * self.m_weapon.m_damage_upper
        lower_total = base_damage_lower + weapon_damage_scaled_lower
        upper_total = base_damage_upper + weapon_damage_scaled_upper
        return (lower_total, upper_total) if upper_total > 1 else (0, 1)

    def get_hit_chance(self):
        x = (config_GladiatorBaseHitChance + self.m_agility) * config_GladiatorAgilityScalingHitChance
        return x if x <= 100 else 100

    def get_max_health(self):
        return round((config_Max_Health + self.m_vitality) * config_GladiatorVitalityScalingHealth)

    def get_crit_chance(self):
        x = (config_GladiatorAgilityScalingCritChance * self.m_agility) \
            + (config_GladiatorLuckScalingCritChance * self.m_luck)
        return round(x, 2) if x <= 100 else 100

    def get_crit_scale(self):
        x = 1 + ((config_GladiatorAgilityScalingCritDmg * self.m_agility)
                 + (config_GladiatorLuckScalingCritDmg * self.m_luck)) * 0.01
        return round(x, 2) if x > 0.01 else 0.01

    def get_dodge_chance(self):
        x = abs((config_GladiatorBaseDodgeChance + self.m_agility) * config_GladiatorAgilityScalingDodgeChance)
        return x if x <= 100 else 100

    def get_armor_value(self):
        return self.m_armor.m_armor_value

    def print_gladiator(self):
        print(f"Stats of Gladiator <> {self.m_name} <>\n"
              f"  Current health {self.m_current_health} of maximum {self.get_max_health()}\n"
              f"    Strength: {self.m_strength}\n"
              f"     Agility: {self.m_agility}\n"
              f"      Vitality: {self.m_vitality}\n"
              f"       Luck: {self.m_luck}\n"
              f"        Gold: {self.m_gold}\n"
              f"         Damage range: {self.get_damage_range()}\n"
              f"          Hit chance: {self.get_hit_chance()}\n"
              f"           Crit chance: {self.get_crit_chance()}\n"
              f"            Crit damage: {self.get_crit_scale()}\n"
              f"             Dodge chance: {self.get_dodge_chance()}\n")
        self.m_GladiatorStatistics.print_gladiator_statistics()
