import os
from worldGenerator import *


class RunGame:

    def __init__(self, world=...):
        self.world = ...

    def print_header(self):
        print("ßßßßßßßßßßßßßßßßßßßßßßßß\n"
              "   Medieval Simulator \n"
              "ßßßßßßßßßßßßßßßßßßßßßßßß\n")

    def start_game(self):
        self.print_header()
        user_input = ""
        self.get_input()
        if user_input == "1":
            yyy = WorldGenerator()
            rastikov_svet = yyy.generate_world()
            self.world = rastikov_svet
            yyy.save_world(rastikov_svet)
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("\nClosing game.")
            quit()

    def get_input(self):
        user_input = input("1. Generate new world\n"
                           "2. Load world\n"
                           "3. Quit\n"
                           "\n"
                           "Enter your choice: ")

        while user_input not in ["1", "2", "3"]:
            print("\nWrong input! Insert 1, 2, or 3\n")
            return self.get_input()
        else:
            return user_input


rasto = RunGame()
rasto.start_game()
