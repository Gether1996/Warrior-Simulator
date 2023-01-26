import configparser

config = configparser.ConfigParser()
config['World_Default'] = {
    "NumOfSimulatedDays": "500"
    # u can set up number of days which will be simulated in World
}

config['Arena_Default'] = {
    "LengthOfArenaSchedule": "5"
    # set up how many schedules will be generated each day
}

def x():
    return int(config['Arena_Default']['LengthOfArenaSchedule'])

def y():
    return int(config['World_Default']['NumOfSimulatedDays'])
