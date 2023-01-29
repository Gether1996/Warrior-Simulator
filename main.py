from worldGenerator import WorldGenerator
from config import *

numOfSimulatedDays = config_NumOfSimulatedDays

rasto = WorldGenerator()
myWorld = rasto.load_world()

current_day = 0
while numOfSimulatedDays > current_day:
    myWorld.simulate_day()
    current_day +=1
rasto.save_world(myWorld)