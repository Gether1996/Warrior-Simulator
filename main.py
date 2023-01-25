from enum import Enum
import random

Schedule = Enum('Schedule', ['Freeday', 'Recruitment', 'Teamgame', 'Duel', 'Freeforall', 'NONE'])

class Arena():

    def __init__(self, m_arenaName:str, m_arenaSchedule=[]):
        self.m_arenaSchedule = []
        self.m_arenaName = m_arenaName
        for i in range(0,5):
            self.append_schedule_random()

    def fill_schedule(self):
        self.m_arenaSchedule.pop(0)
        self.append_schedule_random()

    def progress_day(self):

        self.fill_schedule()
        print(f"# Arena {self.m_arenaName} planned schedule:")

        i = 0
        for day in self.m_arenaSchedule:
            i += 1
            print(f"[{i}] {day.name}")

    def append_schedule_random(self):
        index = random.randint(1, len(Schedule) - 1)
        self.m_arenaSchedule.append(Schedule(index))

    def __str__(self):
        return f"Name of this arena: {self.m_arenaName}"


class World():

    m_arenaDay = 0
    m_max_days = 500

    def __init__(self, m_arenas:list):
        self.m_arenas = m_arenas

    def simulate_day(self):
        self.m_arenaDay += 1
        if self.m_arenaDay == self.m_max_days:
            print(f"Day: {self.m_arenaDay} - maximum days count reached.\n"
                  f"Finishing process...")
            quit()
        else:
            print(f"Day: {self.m_arenaDay}")
            for x in self.m_arenas:
                x.progress_day()


arenas = []
arenas.append(Arena("Kako"))
arenas.append(Arena("Hell"))

myWorld = World(arenas)

while True:
    myWorld.simulate_day()




