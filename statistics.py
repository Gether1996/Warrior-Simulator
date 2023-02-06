from gladiator import *


class GladiatorStatistics(Serializable):

    def __init__(self):
        self.m_gladiator_fame = 5
        self.m_num_of_1v1_victories = 0
        self.m_num_of_1v1_matches = 0
        self.m_num_of_FFA_victories = 0
        self.m_num_of_FFA_matches = 0
        self.m_num_of_team_victories = 0
        self.m_num_of_team_matches = 0
        self.m_total_damage_done = 0
        self.m_total_damage_avoided = 0
        self.m_highest_single_blow_damage = 0
        self.m_total_finishing_blows = 0
        self.m_total_matches = self.sum_of_all_gladiator_matches()

    def save_object(self):
        data = {
            "m_gladiator_fame": self.m_gladiator_fame,
            "m_num_of_1v1_victories": self.m_num_of_1v1_victories,
            "m_num_of_1v1_matches": self.m_num_of_1v1_matches,
            "m_num_of_FFA_victories": self.m_num_of_FFA_victories,
            "m_num_of_FFA_matches": self.m_num_of_FFA_matches,
            "m_num_of_team_victories": self.m_num_of_team_victories,
            "m_num_of_team_matches": self.m_num_of_team_matches,
            "m_total_damage_done": self.m_total_damage_done,
            "m_total_damage_avoided": self.m_total_damage_avoided,
            "m_highest_single_blow_damage": self.m_highest_single_blow_damage,
            "m_total_finishing_blows": self.m_total_finishing_blows,
            "m_total_matches": self.m_total_matches
        }
        return data

    def load_object(self, data):
        self.m_gladiator_fame = data["m_gladiator_fame"]
        self.m_num_of_1v1_victories = data["m_num_of_1v1_victories"]
        self.m_num_of_1v1_matches = data["m_num_of_1v1_matches"]
        self.m_num_of_FFA_victories = data["m_num_of_FFA_victories"]
        self.m_num_of_FFA_matches = data["m_num_of_FFA_matches"]
        self.m_num_of_team_victories = data["m_num_of_team_victories"]
        self.m_num_of_team_matches = data["m_num_of_team_matches"]
        self.m_total_damage_done = data["m_total_damage_done"]
        self.m_total_damage_avoided = data["m_total_damage_avoided"]
        self.m_highest_single_blow_damage = data["m_highest_single_blow_damage"]
        self.m_total_finishing_blows = data["m_total_finishing_blows"]
        self.m_total_matches = data["m_num_of_1v1_matches"] + data["m_num_of_FFA_matches"] \
                               + data["m_num_of_team_matches"]

    def sum_of_all_gladiator_matches(self):
        summary = self.m_num_of_1v1_matches + self.m_num_of_FFA_matches + self.m_num_of_team_matches
        return summary

    def print_gladiator_statistics(self):
        print(f"FAME: {self.m_gladiator_fame}\n"
              f" 1v1 victories: {self.m_num_of_1v1_victories}\n"
              f"  1v1 matches: {self.m_num_of_1v1_matches}\n"
              f"   FFA victories: {self.m_num_of_FFA_victories}\n"
              f"    FFA matches: {self.m_num_of_FFA_matches}\n"
              f"     Team victories: {self.m_num_of_team_victories}\n"
              f"      Team matches: {self.m_num_of_team_matches}\n"
              f"       Total damage done: {self.m_total_damage_done}\n"
              f"        Total damage avoided: {self.m_total_damage_avoided}\n"
              f"         Total finishing blows: {self.m_total_finishing_blows}\n"
              f"          Highest single blow: {self.m_highest_single_blow_damage}\n"
              f"           Total matches played: {self.m_total_matches}")


class ArenaStatistics(Serializable):

    def __init__(self):
        self.m_arena_fame = 0
        self.m_num_of_FFA_matches = 0
        self.m_num_of_1v1_matches = 0
        self.m_num_of_team_matches = 0
        self.m_num_of_gladiators_that_died = 0
        self.m_num_of_gladiators_that_were_accepted_into_arena = 0

    def save_object(self):
        data = {
            "m_arena_fame": self.m_arena_fame,
            "m_num_of_1v1_matches": self.m_num_of_1v1_matches,
            "m_num_of_FFA_matches": self.m_num_of_FFA_matches,
            "m_num_of_team_matches": self.m_num_of_team_matches,
            "m_num_of_gladiators_that_died": self.m_num_of_gladiators_that_died,
            "m_num_of_gladiators_that_were_accepted_into_arena": self.m_num_of_gladiators_that_were_accepted_into_arena
        }
        return data

    def load_object(self, data):
        self.m_arena_fame = data["m_arena_fame"]
        self.m_num_of_1v1_matches = data["m_num_of_1v1_matches"]
        self.m_num_of_FFA_matches = data["m_num_of_FFA_matches"]
        self.m_num_of_team_matches = data["m_num_of_team_matches"]
        self.m_num_of_gladiators_that_died = data["m_num_of_gladiators_that_died"]
        self.m_num_of_gladiators_that_were_accepted_into_arena = \
            data["m_num_of_gladiators_that_were_accepted_into_arena"]

    def print_arena_statistics(self):
        print(f"Arena fame: {self.m_arena_fame}\n"
              f"FFA matches: {self.m_num_of_FFA_matches}\n"
              f"1v1 matches: {self.m_num_of_1v1_matches}\n"
              f"Team matches: {self.m_num_of_team_matches}\n"
              f"Gladiator accepted into arena: {self.m_num_of_gladiators_that_were_accepted_into_arena}\n"
              f"Dead gladiators: {self.m_num_of_gladiators_that_died}")
