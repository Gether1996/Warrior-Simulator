from worldGenerator import *
import time


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

    def get_input_for_menu(self):
        user_input = input("1. Simulate world\n"
                           "2. Save and quit\n"
                           "\n"
                           "Enter your choice: ")

        while user_input not in ["1", "2"]:
            print("\nWrong input! Insert 1 or 2\n")
            return self.get_input_for_menu()
        else:
            return user_input

    def get_input_numOfSimulatedDays(self):
        numOfSimulatedDays = input("Enter number of days to simulate: ")
        if int(numOfSimulatedDays) > (self.world.m_max_days - self.world.m_worldDay):
            print(f"Error, maximum days you can simulate now is {self.world.m_max_days - self.world.m_worldDay}.")
            numOfSimulatedDays = input("Enter number of days to simulate: ")
            if int(numOfSimulatedDays) > (self.world.m_max_days - self.world.m_worldDay):
                print(f"Error, maximum days you can simulate now is {self.world.m_max_days - self.world.m_worldDay}.")
                numOfSimulatedDays = input("Enter number of days to simulate: ")
                if int(numOfSimulatedDays) > (self.world.m_max_days - self.world.m_worldDay):
                    print(f"Error, last chance to input correct number or the world will save and shut down.")
                    numOfSimulatedDays = input("Enter number of days to simulate: ")
                    if int(numOfSimulatedDays) > (self.world.m_max_days - self.world.m_worldDay):
                        self.worldGenerator.save_world(self.world)
                        print("\nClosing game.")
                        quit()
                    else:
                        return numOfSimulatedDays
                else:
                    return numOfSimulatedDays
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
        print(f"\n"
              f"Welcome to world {self.world.m_world_name}!\n"
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
