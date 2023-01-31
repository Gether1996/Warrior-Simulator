import os
from worldGenerator import *


class RunGame:

    def __init__(self, world=...):
        self.world = ...

    def print_header(self):
        print("\n"
              "ßßßßßßßßßßßßßßßßßßßßßßßß\n"
              "   Medieval Simulator \n"
              "ßßßßßßßßßßßßßßßßßßßßßßßß\n")

    def start_game(self):
        self.print_header()
        user_input = self.get_input1()
        if user_input == "1":
            yyy = WorldGenerator()
            rastikov_svet = yyy.generate_world()
            self.world = rastikov_svet
            yyy.save_world(rastikov_svet)
            self.second_step()
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("\nClosing game.")
            quit()

    def get_input1(self):
        user_input = input("1. Generate new world\n"
                           "2. Load world\n"
                           "3. Quit\n"
                           "\n"
                           "Enter your choice: ")

        while user_input not in ["1", "2", "3"]:
            print("\nWrong input! Insert 1, 2, or 3\n")
            return self.get_input1()
        else:
            return user_input

    def get_input2(self):
        user_input = input("1. Simulate world\n"
                           "2. Save and quit\n"
                           "\n"
                           "Enter your choice: ")

        while user_input not in ["1", "2"]:
            print("\nWrong input! Insert 1 or 2\n")
            return self.get_input2()
        else:
            return user_input

    def second_step(self):
        rasto1 = WorldGenerator()
        self.print_header()
        print(f"\n"
              f"Welcome to world {self.world.m_world_name}!\n"
              f"Current day is {self.world.m_worldDay}.\n")
        user_input = self.get_input2()
        if user_input == "1":
            numOfSimulatedDays = int(input("Enter number of days to simulate: "))
            current_day = 0
            while numOfSimulatedDays > current_day:
                self.world.simulate_day()
                current_day += 1
            rasto1.save_world(self.world)
            self.second_step()

        elif user_input == "2":
            rasto1.save_world(self.world)
            print("\nClosing game.")
            quit()
