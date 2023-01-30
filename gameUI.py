class RunGame:

    def __init__(self):
        pass


def start_game():
    user_input = input("ßßßßßßßßßßßßßßßßßßßßßßßßßß\n"
                       "    Medieval Simulator \n"
                       "ßßßßßßßßßßßßßßßßßßßßßßßßßß\n"
                       "\n"
                       "1. Generate new world\n"
                       "2. Load world\n"
                       "3. Quit\n"
                       "\n"
                       "Enter your choice: ")

    while user_input not in ["1", "2", "3"]:
        print("Wrong input!")
        return start_game()
    else:
        if int(user_input) == 1:
            pass
        elif int(user_input) == 2:
            pass
        elif int(user_input) == 3:
            pass


rasto = RunGame()
start_game()
