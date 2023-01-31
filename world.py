from arena import *


class World(Serializable):
    m_worldDay = 1
    m_max_days = config_WorldMaxDays

    def __init__(self, m_arenas: list = []):
        self.m_arenas = m_arenas
        self.m_world_name = ""

    def load_object(self, data):
        self.m_world_name = data["m_world_name"]
        self.m_max_days = data["m_max_days"]
        self.m_worldDay = data["m_worldDay"]

        for arenaData in data["m_arenas"]:
            arena = Arena()
            arena.load_object(arenaData)
            self.m_arenas.append(arena)

    def save_object(self):
        data = {
            "m_world_name": self.m_world_name,
            "m_max_days": self.m_max_days,
            "m_worldDay": self.m_worldDay,
            "m_arenas": []
        }
        for arena in self.m_arenas:
            data["m_arenas"].append(arena.save_object())
        return data

    def simulate_day(self):
        if self.m_worldDay >= self.m_max_days:
            print(f"Day: {self.m_worldDay} - maximum days count reached.\n"
                  f"Finishing process...")
            self.save_object()
            quit()
        else:
            print(f"\nDay: {self.m_worldDay}")
            for t in self.m_arenas:
                t.progress_day()

            self.m_worldDay += 1
