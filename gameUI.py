from worldGenerator import *
import time
import pyinputplus as pyip
from termcolor import colored
import battlefield


class RunGame:
    worldGenerator = WorldGenerator()

    def __init__(self, world=...):
        self.world = ...

    def print_header(self):
        print(colored("\n"
                      "==============================\n"
                      "      Medieval Simulator \n"
                      "==============================\n", config_ColorOfMenuAndSeparators))

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

    def get_input_for_menu(self):
        user_input = input("1. Simulate world\n"
                           "2. Save and quit\n"
                           "3. Show statistics\n"
                           "4. Battlefield\n"
                           "\n"
                           "Enter your choice: ")

        while user_input not in ["1", "2", "3", "4"]:
            print("\nWrong input! Insert 1, 2, 3 or 4\n")
            return self.get_input_for_menu()
        else:
            return user_input

    def get_input_numOfSimulatedDays(self):
        numOfSimulatedDays = pyip.inputNum("Enter number of days to simulate(3 attempts, default 1): ",
                                           limit=3, default=1)
        if int(numOfSimulatedDays) > (self.world.m_max_days - self.world.m_worldDay):
            print(f"Error, maximum days you can simulate now is {self.world.m_max_days - self.world.m_worldDay}.")
            numOfSimulatedDays = pyip.inputNum("Make sure to input correct number(else save and quit the game): ")
            if int(numOfSimulatedDays) > (self.world.m_max_days - self.world.m_worldDay):
                self.worldGenerator.save_world(self.world)
                print("\nClosing game.")
                quit()
            else:
                return numOfSimulatedDays
        else:
            return numOfSimulatedDays

    def start_game(self):
        self.print_header()
        user_input = self.get_input_for_start()
        if user_input == "1":
            myWorld = self.worldGenerator.generate_world()
            os.system('cls')
            self.world = myWorld
            self.world_menu()
        elif user_input == "2":
            self.world = self.worldGenerator.load_world()
            os.system('cls')
            self.world_menu()
        elif user_input == "3":
            print("\nClosing game.")
            quit()

    def world_menu(self):
        self.print_header()
        print("Welcome to world " + colored(self.world.m_world_name, config_ColorOfWorld) + "!\n" 
              f"Current day is {self.world.m_worldDay} out of {self.world.m_max_days}.\n")
        user_input = self.get_input_for_menu()
        if user_input == "1":
            numOfSimulatedDays = self.get_input_numOfSimulatedDays()
            os.system('cls')
            current_day = 0
            while int(numOfSimulatedDays) > current_day:
                self.world.simulate_day()
                current_day += 1
            input("\nPress Enter to run World Menu again...")
            os.system('cls')
            if self.world.m_worldDay == self.world.m_max_days:
                print(f"You have simulated all possible days({self.world.m_max_days}).")
                time.sleep(3)
                print("saving game.... BYE BITCH")
                self.worldGenerator.save_world(self.world)
                quit()
            self.world_menu()

        elif user_input == "2":
            self.worldGenerator.save_world(self.world)
            print("\nClosing game.")
            quit()

        elif user_input == "3":
            os.system('cls')
            self.world.print_world_statistics()
            self.world.save_stats_into_txt()
            input("\nPress Enter to run World Menu again...")
            os.system('cls')
            self.world_menu()

        elif user_input == "4":
            os.system('cls')
            self.print_header()
            event = battlefield.get_event_for_battlefield()
            os.system('cls')
            battlefield.draw_areas(event)
            input("\nPress Enter to run World Menu again...")
            os.system('cls')
            self.world_menu()
