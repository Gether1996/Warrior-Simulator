from enum import Enum
from serializable import *
import random
from config import *

Schedule = Enum('Schedule', ['Freeday', 'Recruitment', 'Teamgame', 'Duel', 'Freeforall'])


class Arena(Serializable):

    def __init__(self):
        self.m_arenaSchedule = []
        self.m_arenaName = ""

    def generate_default_arena(self):
        self.m_arenaSchedule = []
        self.m_arenaName = random.choice(config_ListOfArenaNames)
        for i in range(config_NumOfArenaSchedules):
            self.append_schedule_random()

    def save_object(self):
        data = {
            "m_arenaName": self.m_arenaName,
            "m_arenaSchedule": []
        }
        for x in self.m_arenaSchedule:
            data["m_arenaSchedule"].append(x.value)
        return data

    def load_object(self, data):
        self.m_arenaName = data["m_arenaName"]
        for scheduleData in data["m_arenaSchedule"]:
            self.m_arenaSchedule.append(Schedule(scheduleData))

    def fill_schedule(self):
        self.m_arenaSchedule.pop(0)
        self.append_schedule_random()

    def progress_day(self):

        self.fill_schedule()
        print(f"# Arena {self.m_arenaName.upper()} planned schedule:")

        i = 0
        for day in self.m_arenaSchedule:
            i += 1
            print(f"<[{i}]> {day.name}")

    def append_schedule_random(self):
        index = random.randint(1, len(Schedule))
        self.m_arenaSchedule.append(Schedule(index))

    def __str__(self):
        return f"Name of this arena: {self.m_arenaName}"
