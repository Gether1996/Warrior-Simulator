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

    def save_stats_into_txt(self):
        lines = [f"Current world day: {self.m_worldDay}",
                 self.print_arena_with_best_fame(),
                 self.print_glad_with_most_matches_from_arena(),
                 self.print_glad_with_most_fame_from_arena(),
                 self.print_glad_with_highest_total_dmg_done(),
                 self.print_glad_with_highest_total_dmg_avoided(),
                 self.print_glad_with_most_finishing_blows(),
                 self.print_glad_with_highest_single_blow_delivered()]
        with open('STATISTICS.txt', 'w') as f:
            for line in lines:
                f.write(line)
                f.write('\n')

    def print_world_statistics(self):
        print("=====================================================================\n"
              "\n"
              "=====                        HALL OF FAME                       =====\n"
              "\n"
              "=====================================================================\n"
              "\n"
              "")
        print(self.print_arena_with_best_fame())
        print("\n")
        print(self.print_glad_with_most_matches_from_arena())
        print("\n")
        print(self.print_glad_with_most_fame_from_arena())
        print("\n"
              "####################### HONORABLE MENTIONS ############################\n")
        print(self.print_glad_with_highest_total_dmg_done())
        print(self.print_glad_with_highest_total_dmg_avoided())
        print(self.print_glad_with_most_finishing_blows())
        print(self.print_glad_with_highest_single_blow_delivered())

    def print_arena_with_best_fame(self):
        best_arena = Arena()
        best_arena.m_arena_statistics.m_arena_fame = 0
        for arena in self.m_arenas:
            if arena.m_arena_statistics.m_arena_fame > best_arena.m_arena_statistics.m_arena_fame:
                best_arena = arena
        return f">>>>>>>>>>      Arena with highest fame: {best_arena}      \n"

    def print_glad_with_most_matches_from_arena(self):
        best_glad = Gladiator()
        best_glad.m_GladiatorStatistics.m_total_matches = 0
        best_arena = Arena()
        for arena in self.m_arenas:
            for gladiator in arena.m_arenaGladiators:
                if gladiator.m_GladiatorStatistics.m_total_matches > \
                        best_glad.m_GladiatorStatistics.m_total_matches:
                    best_glad = gladiator
                    best_arena = arena
        return f">>>>>>>>>>      Gladiator with most matches: {best_glad} !\n" \
               f">>>>>>>>>>      Coming from arena: {best_arena} !\n"

    def print_glad_with_most_fame_from_arena(self):
        best_glad = Gladiator()
        best_glad.m_GladiatorStatistics.m_gladiator_fame = 0
        best_arena = Arena()
        for arena in self.m_arenas:
            for gladiator in arena.m_arenaGladiators:
                if gladiator.m_GladiatorStatistics.m_gladiator_fame > best_glad.m_GladiatorStatistics.m_gladiator_fame:
                    best_glad = gladiator
                    best_arena = arena
        return f">>>>>>>>>>      Gladiator with most fame: {best_glad} !\n" \
               f">>>>>>>>>>      Coming from arena: {best_arena} !\n"

    def print_glad_with_highest_total_dmg_done(self):
        best_glad = Gladiator()
        best_glad.m_GladiatorStatistics.m_total_damage_done = 0
        for arena in self.m_arenas:
            for gladiator in arena.m_arenaGladiators:
                if gladiator.m_GladiatorStatistics.m_total_damage_done > \
                        best_glad.m_GladiatorStatistics.m_total_damage_done:
                    best_glad = gladiator
        return f"Gladiator with the highest total damage done: {best_glad} !"

    def print_glad_with_highest_total_dmg_avoided(self):
        best_glad = Gladiator()
        best_glad.m_GladiatorStatistics.m_total_damage_avoided = 0
        for arena in self.m_arenas:
            for gladiator in arena.m_arenaGladiators:
                if gladiator.m_GladiatorStatistics.m_total_damage_avoided > \
                        best_glad.m_GladiatorStatistics.m_total_damage_avoided:
                    best_glad = gladiator
        return f"Gladiator with the highest total damage avoided: {best_glad} !"

    def print_glad_with_most_finishing_blows(self):
        best_glad = Gladiator()
        best_glad.m_GladiatorStatistics.m_total_finishing_blows = 0
        for arena in self.m_arenas:
            for gladiator in arena.m_arenaGladiators:
                if gladiator.m_GladiatorStatistics.m_total_finishing_blows > \
                        best_glad.m_GladiatorStatistics.m_total_finishing_blows:
                    best_glad = gladiator
        return f"Gladiator with the most finishing blows: {best_glad} !"

    def print_glad_with_highest_single_blow_delivered(self):
        best_glad = Gladiator()
        best_glad.m_GladiatorStatistics.m_highest_single_blow_damage = 0
        for arena in self.m_arenas:
            for gladiator in arena.m_arenaGladiators:
                if gladiator.m_GladiatorStatistics.m_highest_single_blow_damage > \
                        best_glad.m_GladiatorStatistics.m_highest_single_blow_damage:
                    best_glad = gladiator
        return f"Gladiator with the highest single blow damage delivered: {best_glad} !"

    def print_glad_with_highest_avg_dmg(self):
        pass  # TODO
