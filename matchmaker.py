from arena import *
from enums import Schedule, Colors


class Matchmaker:

    def __init__(self, m_gladiators=[]):
        self.m_gladiators = []
        self.m_events = Schedule

    def assemble_teams(self, event):
        if event == self.m_events.Duel:
            self.assemble_teams_for_1v1()
        if event == self.m_events.Teamgame:
            self.assemble_teams_for_team_matches()
        if event == self.m_events.Freeforall:
            self.assemble_teams_for_FFA()

    def assemble_teams_for_1v1(self):
        sorted_gladiators_by_total_matches = self.m_gladiators
        sorted_gladiators_by_total_matches.sort(key=lambda x: x.m_GladiatorStatistics.m_total_matches, reverse=True)
        team_pairs = []
        while len(sorted_gladiators_by_total_matches) != 0:
            gladiator1 = sorted_gladiators_by_total_matches[0]
            if len(sorted_gladiators_by_total_matches) > 2:
                gladiator2 = sorted_gladiators_by_total_matches[random.randint(1, 2)]
            elif len(sorted_gladiators_by_total_matches) == 2:
                gladiator2 = sorted_gladiators_by_total_matches[1]
            else:
                break
            team_pairs.append([gladiator1, gladiator2])
            sorted_gladiators_by_total_matches.remove(gladiator1)
            sorted_gladiators_by_total_matches.remove(gladiator2)
        return team_pairs

    def assemble_teams_for_team_matches(self):
        sorted_gladiators_by_fame = self.m_gladiators
        sorted_gladiators_by_fame.sort(key=lambda x: x.m_GladiatorStatistics.m_gladiator_fame, reverse=True)
        team1, team2 = [], []
        team_pair = []
        while len(sorted_gladiators_by_fame) != 0:
            gladiator1 = sorted_gladiators_by_fame[0]
            if len(sorted_gladiators_by_fame) > 1:
                gladiator2 = sorted_gladiators_by_fame[1]
                team1.append(gladiator1)
                team2.append(gladiator2)
                sorted_gladiators_by_fame.remove(gladiator1)
                sorted_gladiators_by_fame.remove(gladiator2)
            else:
                team2.append(gladiator1)
                sorted_gladiators_by_fame.remove(gladiator1)
        team_pair.append(team1)
        team_pair.append(team2)
        return team_pair

    def assemble_teams_for_FFA(self):
        sorted_gladiators_by_fame = self.m_gladiators
        sorted_gladiators_by_fame.sort(key=lambda x: x.m_GladiatorStatistics.m_gladiator_fame)
        top_gladiator = sorted_gladiators_by_fame[-1]
        sorted_gladiators_by_fame.remove(top_gladiator)
        FFA_team = [top_gladiator]
        for gladiator in sorted_gladiators_by_fame:
            if (gladiator.m_GladiatorStatistics.m_gladiator_fame + config_MaximumDifferenceInFame) > \
                    top_gladiator.m_GladiatorStatistics.m_gladiator_fame:
                FFA_team.append(gladiator)
        if len(FFA_team) > 2:
            return FFA_team
        else:
            return []


class Team:

    def __init__(self, gladiators, team_color):
        self.m_gladiators = gladiators
        self.m_team_color = team_color
        self.m_team_name = ...

    def __str__(self):
        return self.m_team_name

    def generate_name_for_team(self):
        if len(self.m_gladiators) > 1:
            self.m_team_name = random.choice(config_ListOfTeamNames)
        else:
            for gladiator in self.m_gladiators:
                self.m_team_name = gladiator.m_name

    def assign_color(self):
        team_color = Colors(self.m_team_color)
        pass


#
#     def add_gladiators(self):
#         for x in range(8):
#             gladiator = Gladiator()
#             gladiator.generate_default_gladiator()
#             gladiator.m_GladiatorStatistics.m_gladiator_fame = random.randint(1, 50)
#             self.m_gladiators.append(gladiator)
#
#
# matchmaker = Matchmaker()
# matchmaker.add_gladiators()
# for gladiator in matchmaker.m_gladiators:
#     print(gladiator.m_name, gladiator.m_GladiatorStatistics.m_gladiator_fame)
# print(matchmaker.assemble_teams_for_FFA())
#
