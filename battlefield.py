from matchmaker import *

char_colors = {'O': 'white', '#': 'light_magenta'}

matrix = [['#' for _ in range(12)] for _ in range(12)]
for i in range(1, 11):
    for j in range(1, 11):
        matrix[i][j] = 'O'


def draw_area():
    for row in matrix:
        colored_row = [colored(c, char_colors[c]) for c in row]
        print(' '.join(colored_row))


def get_teams_and_event():
    matchmaker = Matchmaker()
    for x in range(6):
        gladiator = Gladiator()
        gladiator.generate_default_gladiator()
        gladiator.m_GladiatorStatistics.m_total_matches = random.randint(1, 400)
        matchmaker.m_gladiators.append(gladiator)
    team_pairs = matchmaker.assemble_teams_for_1v1()
    for team_pair in team_pairs:
        char_colors["X"] = team_pair[0].m_team_color.name
        char_colors["Y"] = team_pair[1].m_team_color.name
        matrix[1][1] = "X"
        matrix[-2][-2] = "Y"
        draw_area()

