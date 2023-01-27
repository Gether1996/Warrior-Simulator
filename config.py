import configparser

config = configparser.ConfigParser()
config.read('config.ini')

WorldMaxDays = int(config['WORLD']["World_Max_Days"])
NumOfArenaSchedules = int(config['ARENA']["Arena_Schedules"])

arena_names = open('arena_names.txt')
ListOfArenaNames = lines = [line.rstrip() for line in arena_names]


