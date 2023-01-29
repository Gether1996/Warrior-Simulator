import configparser

config = configparser.ConfigParser()
config.read('config.ini')

config_WorldMaxDays = int(config['WORLD']["World_Max_Days"])
config_NumOfArenaSchedules = int(config['ARENA']["Arena_Schedules"])
config_NumOfSimulatedDays = int(config['WORLD']['NumOfSimulatedDays'])

arena_names = open('arena_names.txt')
config_ListOfArenaNames = [line.rstrip() for line in arena_names]
