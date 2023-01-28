from enum import Enum
import random
import config
from serializable import Serializable
import json

Schedule = Enum('Schedule', ['Freeday', 'Recruitment', 'Teamgame', 'Duel', 'Freeforall'])


class Arena(Serializable):

    def __init__(self):
        self.m_arenaSchedule = []
        self.m_arenaName = random.choice(config.ListOfArenaNames)
        for i in range(config.NumOfArenaSchedules):
            self.append_schedule_random()

    def save_object(self):
        return self.m_arenaName

    def load_object(self):
        pass

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


class World(Serializable):
    m_arenaDay = 0
    m_max_days = config.WorldMaxDays

    def __init__(self, m_arenas: list):
        self.m_arenas = m_arenas

    def save_object(self):
        return self.m_max_days

    def load_object(self):
        pass

    def save_to_json_data(self, ):
        data = {
            "MaxDaysOfArena": self.save_object(),
            "ArenasInsideWorld": []
        }
        for x in self.m_arenas:
            data["ArenasInsideWorld"].append(x.save_object())
        json_data = json.dumps(data, indent=3)
        with open("JSON_data.json", "w") as outfile:
            outfile.write(json_data)

    def simulate_day(self):
        self.save_to_json_data()
        self.m_arenaDay += 1
        if self.m_arenaDay == self.m_max_days:
            print(f"Day: {self.m_arenaDay} - maximum days count reached.\n"
                  f"Finishing process...")
            quit()
        else:
            print(f"Day: {self.m_arenaDay}")
            for t in self.m_arenas:
                t.progress_day()


arena1 = Arena()
arena2 = Arena()
arenas = [arena1, arena2]
myWorld = World(arenas)

while True:
    myWorld.simulate_day()
