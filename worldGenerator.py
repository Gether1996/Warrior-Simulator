from world import *
import os
import json
from datetime import *

class WorldGenerator:

    def __init__(self):
        self.m_world_version = 2

    def save_world(self, world):
        now = datetime.now()
        data = {
            "m_world_version": self.m_world_version,
            "m_save_date_time": now.strftime("%m/%d/%Y, %H:%M:%S"),
            "m_world": world.save_object()
        }
        json_data = json.dumps(data, indent=3)
        with open("JSON_data.json", "w") as outfile:
            outfile.write(json_data)

    def generate_world(self):
        arenas = []
        for x in range(1, 10):
            arena = Arena()
            arena.generate_default_arena()
            arenas.append(arena)

        myWorld = World()
        myWorld.m_arenas = arenas
        return myWorld

    def load_world(self):
        if os.path.exists('JSON_data.json') and (os.stat("JSON_data.json").st_size != 0):
            f = open('JSON_data.json')
            data_from_json = json.loads(f.read())
            if data_from_json["m_world_version"] == self.m_world_version:
                world = World()
                world.load_object(data_from_json["m_world"])
                return world
        return self.generate_world()
