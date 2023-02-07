from arena import *
from termcolor import colored


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
        lines = [f"                Current world day: {self.m_worldDay}",
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
        print(colored("=====================================================================\n"
                      "\n"
                      "=====                        HALL OF FAME                       =====\n"
                      "\n"
                      "=====================================================================\n",
                      config_ColorOfMenuAndSeparators))
        print(self.print_arena_with_best_fame())
        print(colored("=====================================================================\n",
                      config_ColorOfMenuAndSeparators))
        print(self.print_glad_with_most_matches_from_arena())
        print(colored("=====================================================================\n",
                      config_ColorOfMenuAndSeparators))
        print(self.print_glad_with_most_fame_from_arena())
        print(colored("========================= HONORABLE MENTIONS ========================\n",
                      config_ColorOfMenuAndSeparators))
        print(self.print_glad_with_highest_total_dmg_done())
        print(self.print_glad_with_highest_total_dmg_avoided())
        print(self.print_glad_with_most_finishing_blows())
        print(self.print_glad_with_highest_single_blow_delivered())

    def print_arena_with_best_fame(self):
        best_arena = None
        best_arena_fame = 0
        for arena in self.m_arenas:
            if arena.m_arena_statistics.m_arena_fame > best_arena_fame:
                best_arena = arena
                best_arena_fame = arena.m_arena_statistics.m_arena_fame
        return "                Arena with highest fame: " + colored(best_arena, config_ColorOfArenas) + "!     \n"

    def print_glad_with_most_matches_from_arena(self):
        best_glad = None
        best_glad_total_matches = 0
        best_arena = None
        for arena in self.m_arenas:
            for gladiator in arena.m_arenaGladiators:
                if gladiator.m_GladiatorStatistics.m_total_matches > best_glad_total_matches:
                    best_glad = gladiator
                    best_arena = arena
                    best_glad_total_matches = gladiator.m_GladiatorStatistics.m_total_matches
        return "                Gladiator with most matches: " + colored(best_glad, config_ColorOfGladiators) + "!\n" \
               "                Coming from arena:  " + colored(best_arena, config_ColorOfArenas) + "!\n"

    def print_glad_with_most_fame_from_arena(self):
        best_glad = None
        best_glad_fame = 0
        best_arena = None
        for arena in self.m_arenas:
            for gladiator in arena.m_arenaGladiators:
                if gladiator.m_GladiatorStatistics.m_gladiator_fame > best_glad_fame:
                    best_glad = gladiator
                    best_arena = arena
                    best_glad_fame = gladiator.m_GladiatorStatistics.m_gladiator_fame
        return "                Gladiator with most fame: " + colored(best_glad, config_ColorOfGladiators) + "!\n" \
               "                Coming from arena: " + colored(best_arena, config_ColorOfArenas) + "!\n"

    def print_glad_with_highest_total_dmg_done(self):
        best_glad = None
        best_glad_total_damage_done = 0
        for arena in self.m_arenas:
            for gladiator in arena.m_arenaGladiators:
                if gladiator.m_GladiatorStatistics.m_total_damage_done > best_glad_total_damage_done:
                    best_glad = gladiator
                    best_glad_total_damage_done = gladiator.m_GladiatorStatistics.m_total_damage_done
        return " # Gladiator with the highest total damage done: " + colored(best_glad, config_ColorOfGladiators) + "!"

    def print_glad_with_highest_total_dmg_avoided(self):
        best_glad = None
        best_glad_total_damage_avoided = 0
        for arena in self.m_arenas:
            for gladiator in arena.m_arenaGladiators:
                if gladiator.m_GladiatorStatistics.m_total_damage_avoided > best_glad_total_damage_avoided:
                    best_glad = gladiator
                    best_glad_total_damage_avoided = gladiator.m_GladiatorStatistics.m_total_damage_avoided
        return " # Gladiator with the highest total damage avoided: "+colored(best_glad, config_ColorOfGladiators)+"!"

    def print_glad_with_most_finishing_blows(self):
        best_glad = None
        best_glad_total_finishing_blows = 0
        for arena in self.m_arenas:
            for gladiator in arena.m_arenaGladiators:
                if gladiator.m_GladiatorStatistics.m_total_finishing_blows > best_glad_total_finishing_blows:
                    best_glad = gladiator
                    best_glad_total_finishing_blows = gladiator.m_GladiatorStatistics.m_total_finishing_blows
        return " # Gladiator with the most finishing blows: " + colored(best_glad, config_ColorOfGladiators) + "!"

    def print_glad_with_highest_single_blow_delivered(self):
        best_glad = None
        best_glad_highest_single_blow_damage = 0
        for arena in self.m_arenas:
            for gladiator in arena.m_arenaGladiators:
                if gladiator.m_GladiatorStatistics.m_highest_single_blow_damage > best_glad_highest_single_blow_damage:
                    best_glad = gladiator
                    best_glad_highest_single_blow_damage = gladiator.m_GladiatorStatistics.m_highest_single_blow_damage
        return " # Gladiator with the highest single blow damage delivered: " + colored(best_glad,
                                                                                config_ColorOfGladiators) + "!"

    def print_glad_with_highest_avg_dmg(self):
        pass  # TODO
