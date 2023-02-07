from gladiator import *
from arena import *
from enums import Schedule


class Matchmaker:

    def __init__(self, m_gladiators=[]):
        self.m_gladiators = []
        self.m_events = Schedule

    def assemble_teams_for_1v1(self):
        sorted_gladiators_by_total_matches = self.m_gladiators.copy()
        if len(sorted_gladiators_by_total_matches) % 2 != 0:
            sorted_gladiators_by_total_matches.pop(-1)
        sorted_gladiators_by_total_matches.sort(key=lambda x: x.m_GladiatorStatistics.m_total_matches, reverse=True)
        team_pairs = []
        while len(sorted_gladiators_by_total_matches) != 0:
            gladiator1 = sorted_gladiators_by_total_matches[0]
            if len(sorted_gladiators_by_total_matches) > 2:
                gladiator2 = sorted_gladiators_by_total_matches[random.randint(1, 2)]
            else:
                gladiator2 = sorted_gladiators_by_total_matches[1]
            team_pairs.append([gladiator1.m_name, gladiator2.m_name])
            sorted_gladiators_by_total_matches.remove(gladiator1)
            sorted_gladiators_by_total_matches.remove(gladiator2)
        return team_pairs

    def add_gladiators(self):
        for x in range(7):
            gladiator = Gladiator()
            gladiator.generate_default_gladiator()
            gladiator.m_GladiatorStatistics.m_total_matches = random.randint(1, 50)
            self.m_gladiators.append(gladiator)


matchmaker = Matchmaker()
matchmaker.add_gladiators()
print(matchmaker.assemble_teams_for_1v1())
