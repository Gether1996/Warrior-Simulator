from matchmaker import *
import copy
from enums import Schedule

char_colors = {'*': 'white', '#': 'light_magenta'}

matrix = [['#' for _ in range(12)] for _ in range(12)]
for i in range(1, 11):
    for j in range(1, 11):
        matrix[i][j] = '*'

matrix_copy = copy.deepcopy(matrix)


class Battlefield:

    def __init__(self, field, glad_teams, event):
        self.field = field
        self.glad_teams = glad_teams
        self.event = event
        self.generated_fields = []

    def draw_areas(self):
        for field in self.generated_fields:
            print(field)

    def generate_fields(self):
        if self.event == Schedule.Duel:
            for team_pair in self.glad_teams:
                updated_field = copy.deepcopy(self.field)
                char1 = team_pair[0].m_team_name[0]
                char2 = team_pair[1].m_team_name[0]
                char_colors[char1] = team_pair[0].m_team_color.name
                char_colors[char2] = team_pair[1].m_team_color.name
                updated_field[1][1] = char1
                updated_field[len(updated_field)-2][len(updated_field)-2] = char2
                team_pair[0].m_gladiators[0].m_position = (1, 1)
                team_pair[1].m_gladiators[0].m_position = (len(self.field)-2, len(self.field)-2)
                self.generated_fields.append(updated_field)

        elif self.event == Schedule.Teamgame:
            for team_pair in self.glad_teams:
                updated_field = copy.deepcopy(self.field)
                char1 = team_pair[0].m_team_name[0]
                char2 = team_pair[1].m_team_name[0]
                char_colors[char1] = team_pair[0].m_team_color.name
                char_colors[char2] = team_pair[1].m_team_color.name
                updated_field[1] = "#" + char1 * len(team_pair[0].m_gladiators) + "*" * (10 - len(team_pair[0].m_gladiators)) + "#"
                updated_field[len(updated_field)-2] = "#" + char2 * len(team_pair[1].m_gladiators) + "*" * (10 - len(team_pair[1].m_gladiators)) + "#"
                matrix[len(updated_field)-2] = matrix[len(updated_field)-2][::-1]
                for index, gladi in enumerate(team_pair[0].m_gladiators):
                    gladi.m_position = (1, index)
                for index, gladi in enumerate(team_pair[1].m_gladiators):
                    gladi.m_position = (len(updated_field)-2, (len(updated_field)-1)-index)
                self.generated_fields.append(updated_field)

        elif self.event == Schedule.Freeforall:
            coordinates = [(x, y) for x in range(1, len(self.field)) for y in range(1, len(self.field))]
            for teams in self.glad_teams:
                updated_field = copy.deepcopy(self.field)
                for team in teams:
                    char = team.m_team_name[0]
                    char_colors[char] = team.m_team_color.name
                    team_random_coord = random.choice(coordinates)
                    updated_field[team_random_coord[0]][team_random_coord[1]] = char
                    team.m_gladiators[0].m_position = team_random_coord
                    coordinates.remove(team_random_coord)
                self.generated_fields.append(updated_field)
                coordinates = [(x, y) for x in range(1, len(self.field)) for y in range(1, len(self.field))]  # reset coordinates




# def print_matrix(counter):
#     print(f"        # {counter} #")
#     for row in matrix:
#         colored_row = [colored(c, char_colors[c]) for c in row]
#         print(' '.join(colored_row))
#     print()
#
#
# def get_event_for_battlefield():
#     user_input = input("1. Duel\n"
#                        "2. Team game\n"
#                        "3. Free for all\n"
#                        "\n"
#                        "Enter your choice: ")
#
#     while user_input not in ["1", "2", "3"]:
#         print("\nWrong input! Insert 1, 2 or 3\n")
#         return get_event_for_battlefield()
#     else:
#         return user_input
#
#
# def draw_areas(event):
#     global matrix
#     coordinates = [(x, y) for x in range(1, 11) for y in range(1, 11)]
#     matchmaker = Matchmaker()
#     counter = 0
#     for x in range(46):
#         gladiator = Gladiator()
#         gladiator.generate_default_gladiator()
#         gladiator.m_GladiatorStatistics.m_gladiator_fame = random.randint(1, 300)
#         matchmaker.m_gladiators.append(gladiator)
#
#     if event == "1":
#         team_pairs = matchmaker.assemble_teams_for_1v1()
#         for team_pair in team_pairs:
#             char1 = team_pair[0].m_team_name[0]
#             char2 = team_pair[1].m_team_name[0]
#             char_colors[char1] = team_pair[0].m_team_color.name
#             char_colors[char2] = team_pair[1].m_team_color.name
#             matrix[1][1] = char1
#             matrix[10][10] = char2
#             team_pair[0].m_gladiators[0].m_position = (1, 1)
#             team_pair[1].m_gladiators[0].m_position = (10, 10)
#             counter += 1
#             print_matrix(counter)
#             matrix = copy.deepcopy(matrix_copy)
#
#     elif event == "2":
#         list_of_team_pairs = matchmaker.assemble_teams_for_team_matches()
#         for team_pair in list_of_team_pairs:
#             char1 = team_pair[0].m_team_name[0]
#             char2 = team_pair[1].m_team_name[0]
#             char_colors[char1] = team_pair[0].m_team_color.name
#             char_colors[char2] = team_pair[1].m_team_color.name
#             matrix[1] = "#" + char1 * len(team_pair[0].m_gladiators) + "*" * (10 - len(team_pair[0].m_gladiators)) + "#"
#             matrix[10] = "#" + char2 * len(team_pair[1].m_gladiators) + "*" * (10 - len(team_pair[1].m_gladiators)) + "#"
#             matrix[10] = matrix[10][::-1]
#             for index, gladi in enumerate(team_pair[0].m_gladiators):
#                 gladi.m_position = (1, index)
#             for index, gladi in enumerate(team_pair[1].m_gladiators):
#                 gladi.m_position = (10, 11-index)
#             counter += 1
#             print_matrix(counter)
#             matrix = copy.deepcopy(matrix_copy)
#
#     elif event == "3":
#         list_of_teams = matchmaker.assemble_teams_for_FFA()
#         for teams in list_of_teams:
#             for team in teams:
#                 char = team.m_team_name[0]
#                 char_colors[char] = team.m_team_color.name
#                 team_random_coord = random.choice(coordinates)
#                 matrix[team_random_coord[0]][team_random_coord[1]] = char
#                 team.m_gladiators[0].m_position = team_random_coord
#                 coordinates.remove(team_random_coord)
#
#             counter += 1
#             print_matrix(counter)
#             matrix = copy.deepcopy(matrix_copy)
#             coordinates = [(x, y) for x in range(1, 11) for y in range(1, 11)]
#
#
#
#
#
