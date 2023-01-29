import configparser

config = configparser.ConfigParser()
config.read('config.ini')

# World configurations ###########################
config_WorldMaxDays = int(config['WORLD']["World_Max_Days"])
config_NumOfSimulatedDays = int(config['WORLD']['NumOfSimulatedDays'])

# Arena configurations ################################
arena_names = open('arena_names.txt')
config_ListOfArenaNames = [line.rstrip() for line in set(arena_names)]
config_NumOfArenaSchedules = int(config['ARENA']["Arena_Schedules"])

# Gladiator configurations ##################################
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
