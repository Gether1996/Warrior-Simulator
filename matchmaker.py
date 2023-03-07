import random

from arena import *
from enums import Schedule, Colors


class Team:

    def __init__(self, gladiators, team_color):
        self.m_gladiators = gladiators
        self.m_team_color = Colors(team_color)
        self.m_team_name = random.choice(config_ListOfTeamNames)

    def __str__(self):
        return self.m_team_name

    def generate_name_for_team(self):
        if len(self.m_gladiators) > 1:
            self.m_team_name = random.choice(config_ListOfTeamNames)
        else:
            for glad in self.m_gladiators:
                self.m_team_name = glad.m_name


class Matchmaker:

    def __init__(self, gladiators=[]):
        self.m_gladiators = []
        self.m_events = Schedule

    def assemble_teams(self, event):
        if event == Schedule.Duel:
            return self.assemble_teams_for_1v1()
        if event == Schedule.Teamgame:
            return self.assemble_teams_for_team_matches()
        if event == Schedule.Freeforall:
            return self.assemble_teams_for_FFA()

    def assemble_teams_for_1v1(self):
        sorted_gladiators_by_total_matches = self.m_gladiators
        sorted_gladiators_by_total_matches.sort(key=lambda x: x.m_GladiatorStatistics.m_total_matches, reverse=True)
        team_pairs_to_return = []

        while len(sorted_gladiators_by_total_matches) != 0:
            gladiator1 = sorted_gladiators_by_total_matches[0]
            random_numbers_for_color = [x for x in range(1, (config_NumOfColors + 1))]
            randomly_chosen_color = random.choice(random_numbers_for_color)
            team1 = Team([gladiator1], randomly_chosen_color)
            team1.generate_name_for_team()
            random_numbers_for_color.remove(randomly_chosen_color)

            if len(sorted_gladiators_by_total_matches) > 2:
                gladiator2 = sorted_gladiators_by_total_matches[random.randint(1, 2)]
                randomly_chosen_second_color = random.choice(random_numbers_for_color)
                team2 = Team([gladiator2], randomly_chosen_second_color)
                team2.generate_name_for_team()

            elif len(sorted_gladiators_by_total_matches) == 2:
                gladiator2 = sorted_gladiators_by_total_matches[1]
                randomly_chosen_second_color = random.choice(random_numbers_for_color)
                team2 = Team([gladiator2], randomly_chosen_second_color)
                team2.generate_name_for_team()

            else:
                break

            team_pairs_to_return.append([team1, team2])
            sorted_gladiators_by_total_matches.remove(gladiator1)
            sorted_gladiators_by_total_matches.remove(gladiator2)
        return team_pairs_to_return

    def assemble_teams_for_team_matches(self):
        sorted_gladiators_by_fame = self.m_gladiators
        sorted_gladiators_by_fame.sort(key=lambda x: x.m_GladiatorStatistics.m_gladiator_fame, reverse=True)
        glads_for_team1, glads_for_team2 = [], []
        team_pair = []
        team_pairs_to_return = []
        team1_fame, team2_fame = 0, 0
        color_pool = list(range(1, config_NumOfColors + 1))

        if len(sorted_gladiators_by_fame) < 4:
            return []
        else:
            while len(sorted_gladiators_by_fame) != 0:
                while (len(glads_for_team1) + len(glads_for_team2)) != config_NumOfColors:
                    if len(sorted_gladiators_by_fame) != 0:
                        glad_to_append = sorted_gladiators_by_fame[0]
                        if team2_fame >= team1_fame:
                            glads_for_team1.append(glad_to_append)
                            team1_fame += glad_to_append.m_GladiatorStatistics.m_gladiator_fame
                        else:
                            glads_for_team2.append(glad_to_append)
                            team2_fame += glad_to_append.m_GladiatorStatistics.m_gladiator_fame
                        sorted_gladiators_by_fame.remove(glad_to_append)
                    else:
                        break
                else:
                    team1 = Team([glads_for_team1], random.choice(color_pool))
                    color_pool.remove(team1.m_team_color.value)
                    team2 = Team([glads_for_team2], random.choice(color_pool))

                    team_pair.append([team1, team2])
                    glads_for_team1.clear()
                    glads_for_team2.clear()
                    team1_fame, team2_fame = 0, 0
                    color_pool = list(range(1, config_NumOfColors + 1))
            else:
                team1 = Team([glads_for_team1], random.choice(color_pool))
                color_pool.remove(team1.m_team_color.value)
                team2 = Team([glads_for_team2], random.choice(color_pool))

                team_pair.append([team1, team2])
                team_pairs_to_return.append(team_pair)
        return team_pairs_to_return

    def assemble_teams_for_FFA(self):
        gladiators = self.m_gladiators
        gladiators.sort(key=lambda x: x.m_GladiatorStatistics.m_gladiator_fame)
        result = []
        group = [gladiators[0]]
        color_pool = list(range(1, config_NumOfColors + 1))
        for i in range(1, len(gladiators)):
            if abs(gladiators[i].m_GladiatorStatistics.m_gladiator_fame -
                   group[0].m_GladiatorStatistics.m_gladiator_fame) <= config_MaximumDifferenceInFame \
                    and len(group) < 10:
                group.append(gladiators[i])
            else:
                list_of_teams = []
                for gladi in group:
                    team_to_append = Team(gladi, random.choice(color_pool))
                    color_pool.remove(team_to_append.m_team_color.value)
                    list_of_teams.append(team_to_append)
                result.append(list_of_teams)
                group = [gladiators[i]]
                color_pool = list(range(1, config_NumOfColors + 1))   #resets color pool
        list_of_teams = []
        for gladi in group:
            team_to_append = Team(gladi, random.choice(color_pool))
            color_pool.remove(team_to_append.m_team_color.value)
            list_of_teams.append(team_to_append)
        result.append(list_of_teams)
        final_result = [res for res in result if len(res) > 2]
        return final_result

#     def add_gladiators(self):
#         for x in range(10):
#             gladiator = Gladiator()
#             gladiator.generate_default_gladiator()
#             gladiator.m_GladiatorStatistics.m_gladiator_fame = random.randint(1, 400)
#             self.m_gladiators.append(gladiator)
#
#
# matchmaker = Matchmaker()
# matchmaker.add_gladiators()
# for gladiator in matchmaker.m_gladiators:
#     print(gladiator.m_name, gladiator.m_GladiatorStatistics.m_gladiator_fame)
# print(matchmaker.assemble_teams_for_FFA())

# fame_list = [g.m_GladiatorStatistics.m_gladiator_fame for g in group]
# result.append(fame_list)                                   ---- toto prehodit za result.append(list_of_teams) na lepsi print famu
#
