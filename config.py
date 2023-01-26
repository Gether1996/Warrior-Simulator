import configparser

config = configparser.ConfigParser()
config.read('config.ini')

WorldMaxDays = int(config['WORLD']["World_Max_Days"])
NumOfArenaSchedules = int(config['ARENA']["Arena_Schedules"])
