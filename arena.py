from enums import Schedule
import random
from config import *
from gladiator import Gladiator
from serializable import Serializable
from items import ItemManager
from statistics import ArenaStatistics


class Arena(Serializable):

    def __init__(self):
        self.m_arenaSchedule = []
        self.m_arenaName = ""
        self.m_arenaGladiators = []
        self.m_item_manager = ItemManager()
        self.m_arena_statistics = ArenaStatistics()

    def generate_default_arena(self):
        self.m_item_manager.load_items_from_json()
        self.m_arenaGladiators = []
        self.m_arenaSchedule = []
        self.m_arenaName = random.choice(config_ListOfArenaNames)
        for i in range(config_NumOfArenaSchedules):
            self.append_schedule_random()
        for y in range(config_NumOfArenaGladiators):
            gladiator = Gladiator()
            gladiator.generate_default_gladiator()
            gladiator.m_armor = self.m_item_manager.generate_spawning_armor_wooden()
            gladiator.m_weapon = self.m_item_manager.generate_spawning_weapon_falchion()
            self.m_arenaGladiators.append(gladiator)
        arena_fame = 0
        for gladiator in self.m_arenaGladiators:
            arena_fame += gladiator.m_GladiatorStatistics.m_gladiator_fame
        self.m_arena_statistics.m_arena_fame = arena_fame

    def save_object(self):
        data = {
            "m_arenaName": self.m_arenaName,
            "m_arenaSchedule": [],
            "m_arena_statistics": self.m_arena_statistics.save_object(),
            "m_arenaGladiators": []
        }
        for x in self.m_arenaSchedule:
            data["m_arenaSchedule"].append(x.value)
        for gladiator in self.m_arenaGladiators:
            data["m_arenaGladiators"].append(gladiator.save_object())
        return data

    def load_object(self, data):
        self.m_arenaName = data["m_arenaName"]
        for scheduleData in data["m_arenaSchedule"]:
            self.m_arenaSchedule.append(Schedule(scheduleData))
        for gladiatorData in data["m_arenaGladiators"]:
            gladiator = Gladiator()
            gladiator.load_object(gladiatorData)
            self.m_arenaGladiators.append(gladiator)
        self.m_arena_statistics = ArenaStatistics()
        self.m_arena_statistics.load_object(data["m_arena_statistics"])

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
        return f"{self.m_arenaName}"

    def glad_with_most_fame(self):
        glad = Gladiator()
        for gladiator in self.m_arenaGladiators:
            if gladiator.m_GladiatorStatistics.m_gladiator_fame > glad.m_GladiatorStatistics.m_gladiator_fame:
                glad = gladiator
        return glad

    def glad_with_most_matches(self):
        glad = Gladiator()
        glad.m_GladiatorStatistics.m_total_matches = 0
        for gladiator in self.m_arenaGladiators:
            if gladiator.m_GladiatorStatistics.m_total_matches > \
                    glad.m_GladiatorStatistics.m_total_matches:
                glad = gladiator
        return glad

    def current_num_of_gladiators_in_arena(self):
        return len(self.m_arenaGladiators)

    def sum_of_gladiators_fame_in_arena(self):
        summary = 0
        for gladiator in self.m_arenaGladiators:
            summary += gladiator.m_GladiatorStatistics.m_gladiator_fame
        return summary
