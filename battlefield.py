from matchmaker import *
import copy

char_colors = {'*': 'white', '#': 'light_magenta'}

matrix = [['#' for _ in range(12)] for _ in range(12)]
for i in range(1, 11):
    for j in range(1, 11):
        matrix[i][j] = '*'

matrix_copy = copy.deepcopy(matrix)


def print_matrix(counter):
    print(f"        # {counter} #")
    for row in matrix:
        colored_row = [colored(c, char_colors[c]) for c in row]
        print(' '.join(colored_row))
    print()


def get_event_for_battlefield():
    user_input = input("1. Duel\n"
                       "2. Team game\n"
                       "3. Free for all\n"
                       "\n"
                       "Enter your choice: ")

    while user_input not in ["1", "2", "3"]:
        print("\nWrong input! Insert 1, 2 or 3\n")
        return get_event_for_battlefield()
    else:
        return user_input


def draw_areas(event):
    global matrix
    coordinates = [(x, y) for x in range(1, 11) for y in range(1, 11)]
    matchmaker = Matchmaker()
    counter = 0
    for x in range(5):
        gladiator = Gladiator()
        gladiator.generate_default_gladiator()
        gladiator.m_GladiatorStatistics.m_gladiator_fame = random.randint(1, 300)
        matchmaker.m_gladiators.append(gladiator)

    if event == "1":
        team_pairs = matchmaker.assemble_teams_for_1v1()
        for team_pair in team_pairs:
            char1 = team_pair[0].m_team_name[0]
            char2 = team_pair[1].m_team_name[0]
            char_colors[char1] = team_pair[0].m_team_color.name
            char_colors[char2] = team_pair[1].m_team_color.name
            matrix[1][1] = char1
            matrix[-2][-2] = char2
            counter += 1
            print_matrix(counter)
            matrix = copy.deepcopy(matrix_copy)

    elif event == "2":
        list_of_team_pairs = matchmaker.assemble_teams_for_team_matches()
        for team_pair in list_of_team_pairs:
            char1 = team_pair[0].m_team_name[0]
            char2 = team_pair[1].m_team_name[0]
            char_colors[char1] = team_pair[0].m_team_color.name
            char_colors[char2] = team_pair[1].m_team_color.name
            matrix[1] = "#" + char1 * len(team_pair[0].m_gladiators) + "*" * (10 - len(team_pair[0].m_gladiators)) + "#"
            matrix[10] = "#" + char2 * len(team_pair[1].m_gladiators) + "*" * (10 - len(team_pair[1].m_gladiators)) + "#"
            counter += 1
            print_matrix(counter)
            matrix = copy.deepcopy(matrix_copy)

    elif event == "3":
        list_of_teams = matchmaker.assemble_teams_for_FFA()
        for teams in list_of_teams:
            for team in teams:
                char = team.m_team_name[0]
                char_colors[char] = team.m_team_color.name
                team_random_coord = random.choice(coordinates)
                matrix[team_random_coord[0]][team_random_coord[1]] = char
                coordinates.remove(team_random_coord)
            counter += 1
            print_matrix(counter)
            matrix = copy.deepcopy(matrix_copy)
            coordinates = [(x, y) for x in range(1, 11) for y in range(1, 11)]





