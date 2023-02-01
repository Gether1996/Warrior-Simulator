from math import floor
from serializable import Serializable
import random
from config import *
from enum import Enum

Races = Enum('Races', ['Human', 'Elf', 'Dwarf', 'Orc'])
Traits = [["Strong", "Weak"], ["Nimble", "Sluggish"], ["Vigorous", "Fragile"], ["Blessed", "Unfortunate"]]


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

    def pick_random_race(self):
        index = random.randint(1, len(Races))
        self.m_race = Races(index).value

    def generate_default_gladiator(self):
        self.m_name = random.choice(config_GladiatorNames)
        self.pick_random_race()
        if self.m_race == 1:
            self.generate_human()
        if self.m_race == 2:
            self.generate_elf()
        if self.m_race == 3:
            self.generate_dwarf()
        if self.m_race == 4:
            self.generate_orc()
        self.m_max_health = self.get_max_health()
        self.m_current_health = self.get_max_health()
        self.m_gold = config_Gold
        self.add_strength_trait()
        self.add_agility_trait()
        self.add_vitality_trait()
        self.add_luck_trait()

    def generate_human(self):
        self.m_strength = config_GladiatorBaseStat + random.randint(0, config_GladiatorStatRollRange) \
                          + config_HumanStrengthBonus
        self.m_agility = config_GladiatorBaseStat + random.randint(0, config_GladiatorStatRollRange) \
                         + config_HumanAgilityBonus
        self.m_vitality = config_GladiatorBaseStat + random.randint(0, config_GladiatorStatRollRange) \
                          + config_HumanVitaliyBonus
        self.m_luck = config_GladiatorBaseStat + random.randint(0, config_GladiatorStatRollRange) \
                      + config_HumanLuckBonus

    def generate_elf(self):
        self.m_strength = config_GladiatorBaseStat + random.randint(0, config_GladiatorStatRollRange) \
                          + config_ElfStrengthBonus
        self.m_agility = config_GladiatorBaseStat + random.randint(0, config_GladiatorStatRollRange) \
                         + config_ElfAgilityBonus
        self.m_vitality = config_GladiatorBaseStat + random.randint(0, config_GladiatorStatRollRange) \
                          + config_ElfVitaliyBonus
        self.m_luck = config_GladiatorBaseStat + random.randint(0, config_GladiatorStatRollRange) \
                      + config_ElfLuckBonus

    def generate_dwarf(self):
        self.m_strength = config_GladiatorBaseStat + random.randint(0, config_GladiatorStatRollRange) \
                          + config_DwarfStrengthBonus
        self.m_agility = config_GladiatorBaseStat + random.randint(0, config_GladiatorStatRollRange) \
                         + config_DwarfAgilityBonus
        self.m_vitality = config_GladiatorBaseStat + random.randint(0, config_GladiatorStatRollRange) \
                          + config_DwarfVitaliyBonus
        self.m_luck = config_GladiatorBaseStat + random.randint(0, config_GladiatorStatRollRange) \
                      + config_DwarfLuckBonus

    def generate_orc(self):
        self.m_strength = config_GladiatorBaseStat + random.randint(0, config_GladiatorStatRollRange) \
                          + config_OrcStrengthBonus
        self.m_agility = config_GladiatorBaseStat + random.randint(0, config_GladiatorStatRollRange) \
                         + config_OrcAgilityBonus
        self.m_vitality = config_GladiatorBaseStat + random.randint(0, config_GladiatorStatRollRange) \
                          + config_OrcVitaliyBonus
        self.m_luck = config_GladiatorBaseStat + random.randint(0, config_GladiatorStatRollRange) \
                      + config_OrcLuckBonus

    def add_strength_trait(self):
        if random.randint(1, 100) <= config_GladiatorTraitRollChance:
            pos_or_neg_trait = random.choice(Traits[0])
            self.m_traits.append(pos_or_neg_trait)
            if pos_or_neg_trait == "Strong":
                self.m_strength += config_TraitStrengthBonus
            else:
                self.m_strength += config_TraitStrengthPenalty

    def add_agility_trait(self):
        if random.randint(1, 100) <= config_GladiatorTraitRollChance:
            pos_or_neg_trait = random.choice(Traits[1])
            self.m_traits.append(pos_or_neg_trait)
            if pos_or_neg_trait == "Nimble":
                self.m_agility += config_TraitAgilityBonus
            else:
                self.m_agility += config_TraitAgilityPenalty

    def add_vitality_trait(self):
        if random.randint(1, 100) <= config_GladiatorTraitRollChance:
            pos_or_neg_trait = random.choice(Traits[2])
            self.m_traits.append(pos_or_neg_trait)
            if pos_or_neg_trait == "Vigorous":
                self.m_vitality += config_TraitVitalityBonus
            else:
                self.m_vitality += config_TraitVitalityPenalty

    def add_luck_trait(self):
        if random.randint(1, 100) <= config_GladiatorTraitRollChance:
            pos_or_neg_trait = random.choice(Traits[3])
            self.m_traits.append(pos_or_neg_trait)
            if pos_or_neg_trait == "Blessed":
                self.m_luck += config_TraitLuckBonus
            else:
                self.m_luck += config_TraitLuckPenalty

    def save_object(self):
        data = {
            "m_name": self.m_name,
            "m_race": self.m_race,
            "m_traits": self.m_traits,
            "m_strength": self.m_strength,
            "m_agility": self.m_agility,
            "m_vitality": self.m_vitality,
            "m_luck": self.m_luck,
            "m_max_health": self.m_max_health,
            "m_current_health": self.m_current_health,
            "m_gold": self.m_gold
        }
        return data

    def load_object(self, data):
        self.m_name = data["m_name"]
        self.m_race = data["m_race"]
        self.m_traits = data["m_traits"]
        self.m_strength = data["m_strength"]
        self.m_agility = data["m_agility"]
        self.m_vitality = data["m_vitality"]
        self.m_luck = data["m_luck"]
        self.m_max_health = data["m_max_health"]
        self.m_current_health = data["m_current_health"]
        self.m_gold = data["m_gold"]

    def get_damage_range(self):
        low = floor(self.m_strength * config_GladiatorStrengthLowerDmgRng)
        top = floor(self.m_strength * config_GladiatorStrengthUpperDmgRng)
        return (low, top) if top > 1 else (0, 1)

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

    def print_stats(self):
        return print(f"Stats of Gladiator <> {self.m_name} <>\n"
                     f"  Current health {self.m_current_health} of maximum {self.get_max_health()}\n"
                     f"    Strength: {self.m_strength}\n"
                     f"     Agility: {self.m_agility}\n"
                     f"      Vitality: {self.m_vitality}\n"
                     f"       Luck: {self.m_luck}\n"
                     f"        Gold: {self.m_gold}\n"
                     f"         Damage range: {self.get_damage_range()}\n"
                     f"        Hit chance: {self.get_hit_chance()}\n"
                     f"       Crit chance: {self.get_crit_chance()}\n"
                     f"      Crit damage: {self.get_crit_scale()}\n"
                     f"     Dodge chance: {self.get_dodge_chance()}\n")
