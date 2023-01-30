from arena import *


class World(Serializable):
    m_arenaDay = 1
    m_max_days = config_WorldMaxDays

    def __init__(self, m_arenas: list = []):
        self.m_arenas = m_arenas
        self.m_world_name = random.choice(config_ListOfWorldNames)

    def load_object(self, data):
        self.m_world_name = data["m_world_name"]
        self.m_max_days = data["m_max_days"]
        self.m_arenaDay = data["m_arenaDay"]

        for arenaData in data["m_arenas"]:
            arena = Arena()
            arena.load_object(arenaData)
            self.m_arenas.append(arena)

    def save_object(self):
        data = {
            "m_world_name": self.m_world_name,
            "m_max_days": self.m_max_days,
            "m_arenaDay": self.m_arenaDay,
            "m_arenas": []
        }
        for arena in self.m_arenas:
            data["m_arenas"].append(arena.save_object())
        return data

    def simulate_day(self):
        if self.m_arenaDay >= self.m_max_days:
            print(f"Day: {self.m_arenaDay} - maximum days count reached.\n"
                  f"Finishing process...")
            self.save_object()
            quit()
        else:
            print(f"Day: {self.m_arenaDay}")
            for t in self.m_arenas:
                t.progress_day()

            self.m_arenaDay += 1
