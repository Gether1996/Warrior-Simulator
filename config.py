import configparser

config = configparser.ConfigParser()
config.read('config.ini')

WorldMaxDays = int(config['DEFAULT']["World_Max_Days"])
NumOfArenaSchedules = int(config['DEFAULT']["Arena_Schedules"])
