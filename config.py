import configparser

config = configparser.ConfigParser()
config.read('config.ini')

########################### World configurations #################################
world_names = open('world_names.txt')
config_ListOfWorldNames = [line.rstrip() for line in set(world_names)]
config_WorldMaxDays = int(config['WORLD']["World_Max_Days"])
config_NumOfSimulatedDays = int(config['WORLD']['NumOfSimulatedDays'])

################################ Arena configurations #############################
arena_names = open('arena_names.txt')
config_ListOfArenaNames = [line.rstrip() for line in set(arena_names)]
config_NumOfArenasGenerated = int(config['ARENA']["NumOfArenasGenerated"])
config_NumOfArenaSchedules = int(config['ARENA']["Arena_Schedules"])
config_NumOfArenaGladiators = int(config['ARENA']['NumOfArenaGladiators'])

################################## Gladiator configurations #############################
gladiator_names = open('gladiator_names.txt')
config_GladiatorNames = [line.rstrip() for line in set(gladiator_names)]

config_Gold = int(config['GLADIATOR']['Gold'])
config_GladiatorBaseStat = int(config['GLADIATOR']['Base_Stat'])
config_GladiatorStatRollRange = int(config['GLADIATOR']['Roll_Range'])
config_Max_Health = int(config['GLADIATOR']['Max_Health'])

config_GladiatorStrengthLowerDmgRng = 0.25
config_GladiatorStrengthUpperDmgRng = 0.5
config_GladiatorBaseHitChance = 10
config_GladiatorAgilityScalingHitChance = 4
config_GladiatorAgilityScalingCritChance = 0.25
config_GladiatorLuckScalingCritChance = 0.5
config_GladiatorAgilityScalingCritDmg = 1
config_GladiatorLuckScalingCritDmg = 0.25
config_GladiatorBaseDodgeChance = 5
config_GladiatorAgilityScalingDodgeChance = 1
config_GladiatorVitalityScalingHealth = 0.8

################################# RACES #####################################
################################# Human #####################################
config_HumanStrengthBonus = int(config['HUMAN']['Strength'])
config_HumanAgilityBonus = int(config['HUMAN']['Agility'])
config_HumanVitaliyBonus = int(config['HUMAN']['Vitality'])
config_HumanLuckBonus = int(config['HUMAN']['Luck'])

################################# Elf #####################################
config_ElfStrengthBonus = int(config['ELF']['Strength'])
config_ElfAgilityBonus = int(config['ELF']['Agility'])
config_ElfVitaliyBonus = int(config['ELF']['Vitality'])
config_ElfLuckBonus = int(config['ELF']['Luck'])

################################# Dwarf #####################################
config_DwarfStrengthBonus = int(config['DWARF']['Strength'])
config_DwarfAgilityBonus = int(config['DWARF']['Agility'])
config_DwarfVitaliyBonus = int(config['DWARF']['Vitality'])
config_DwarfLuckBonus = int(config['DWARF']['Luck'])

################################# Orc #####################################
config_OrcStrengthBonus = int(config['ORC']['Strength'])
config_OrcAgilityBonus = int(config['ORC']['Agility'])
config_OrcVitaliyBonus = int(config['ORC']['Vitality'])
config_OrcLuckBonus = int(config['ORC']['Luck'])

################################## TRAITS #####################################
config_GladiatorTraitRollChance = int(config['TRAITS']['Roll_chance'])

config_TraitStrengthBonus = int(config['TRAITS']['Strong_effect'])
config_TraitStrengthPenalty = int(config['TRAITS']['Weak_effect'])
config_TraitAgilityBonus = int(config['TRAITS']['Nimble_effect'])
config_TraitAgilityPenalty = int(config['TRAITS']['Sluggish_effect'])
config_TraitVitalityBonus = int(config['TRAITS']['Vigorous_effect'])
config_TraitVitalityPenalty = int(config['TRAITS']['Fragile_effect'])
config_TraitLuckBonus = int(config['TRAITS']['Blessed_effect'])
config_TraitLuckPenalty = int(config['TRAITS']['Unfortunate_effect'])

################################## ITEMS #####################################
config_MaximumArmorReduction = int(config['ITEMS']['Maximum_armor_reduction'])
