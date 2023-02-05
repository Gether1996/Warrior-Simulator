from serializable import Serializable


class GladiatorStatistics(Serializable):

    def __init__(self):
        self.m_fame = 0
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

    def save_object(self):
        data = {
            "m_fame": self.m_fame,
            "m_num_of_1v1_victories": self.m_num_of_1v1_victories,
            "m_num_of_1v1_matches": self.m_num_of_1v1_matches,
            "m_num_of_FFA_victories": self.m_num_of_FFA_victories,
            "m_num_of_FFA_matches": self.m_num_of_FFA_matches,
            "m_num_of_team_victories": self.m_num_of_team_victories,
            "m_num_of_team_matches": self.m_num_of_team_matches,
            "m_total_damage_done": self.m_total_damage_done,
            "m_total_damage_avoided": self.m_total_damage_avoided,
            "m_highest_single_blow_damage": self.m_highest_single_blow_damage,
            "m_total_finishing_blows": self.m_total_finishing_blows
        }
        return data

    def load_object(self, data):
        self.m_fame = data["m_fame"]
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

