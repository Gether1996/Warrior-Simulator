import os
from worldGenerator import *


class RunGame:

    worldGenerator = WorldGenerator()
    def __init__(self, world=...):
        self.world = ...

    def print_header(self):
        print("\n"
              "ßßßßßßßßßßßßßßßßßßßßßßßß\n"
              "   Medieval Simulator \n"
              "ßßßßßßßßßßßßßßßßßßßßßßßß\n")

    def get_input_for_start(self):
        user_input = input("1. Generate new world\n"
                           "2. Load world\n"
                           "3. Quit\n"
                           "\n"
                           "Enter your choice: ")

        while user_input not in ["1", "2", "3"]:
            print("\nWrong input! Insert 1, 2, or 3\n")
            return self.get_input_for_start()
        else:
            return user_input

    def get_input_for_second(self):
        user_input = input("1. Simulate world\n"
                           "2. Save and quit\n"
                           "\n"
                           "Enter your choice: ")

        while user_input not in ["1", "2"]:
            print("\nWrong input! Insert 1 or 2\n")
            return self.get_input_for_second()
        else:
            return user_input

    def start_game(self):
        self.print_header()
        user_input = self.get_input_for_start()
        if user_input == "1":
            myWorld = self.worldGenerator.generate_world()
            myWorld.m_world_name = input("Enter world name: ")
            os.system('cls')
            self.world = myWorld
            self.worldGenerator.save_world(myWorld)
            self.second_step()
        elif user_input == "2":
            self.world = self.worldGenerator.load_world()
            os.system('cls')
            self.second_step()
        elif user_input == "3":
            print("\nClosing game.")
            quit()

    def second_step(self):
        self.print_header()
        print(f"\n"
              f"Welcome to world {self.world.m_world_name}!\n"
              f"Current day is {self.world.m_worldDay}.\n")
        user_input = self.get_input_for_second()
        if user_input == "1":
            numOfSimulatedDays = input("Enter number of days to simulate: ")
            os.system('cls')
            current_day = 0
            while int(numOfSimulatedDays) > current_day:
                self.world.simulate_day()
                current_day += 1
            self.worldGenerator.save_world(self.world)
            self.second_step()

        elif user_input == "2":
            self.worldGenerator.save_world(self.world)
            print("\nClosing game.")
            quit()
