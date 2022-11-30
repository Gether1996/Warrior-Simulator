from enum import Enum

class Schedule1(Enum):
    freeday = 1
    recruitment = 2
    teamgame = 3
    duel = 4
    freeforall = 5
    none = 6

class Schedule2(Enum):
    deathmatch = 1
    peace = 2
    brawl = 3
    raidboss = 4
    training = 5
    none = 6


class Arena():


    def __init__(self, m_arenaName:str, m_arenaSchedule):
        self.m_arenaName = m_arenaName
        self.m_arenaSchedule = m_arenaSchedule

    def fill_schedule(self):
        moved_schedule = self.m_arenaSchedule.pop(0)
        return self.m_arenaSchedule.append(moved_schedule)

    def progress_day(self):
        print(f"Tomorrows plan of arena {self.m_arenaName} is {self.m_arenaSchedule[1]}.")
        Arena.fill_schedule(self)

    def __str__(self):
        return f"Name of this arena: {self.m_arenaName}"


class World():

    m_arenaDay = 0
    m_max_days = 500


    def __init__(self, m_arenas:list):
        self.m_arenas = m_arenas


    def simulate_day(self):
        self.m_arenaDay += 1
        if self.m_arenaDay == self.m_max_days:
            print(f"Day: {self.m_arenaDay} - maximum days count reached.\n"
                  f"Finishing process...")
            quit()
        else:
            print(f"Day: {self.m_arenaDay}")
            for x in self.m_arenas:
                x.progress_day()



schedule1 = enumerate(("freeday", "recruitment", "teamgame", "duel", "freeforall", "none"), 0)
schedule2 = enumerate(["deathmatch", "peace", "training", "RockPaperScizzors", "extinction", "none"],0)


arena1 = Arena("Kako", ["freeday", "recruitment", "teamgame", "duel", "freeforall", "none"])
arena2 = Arena("Hell", ["deathmatch", "peace", "training", "RockPaperScizzors", "extinction"])
myWorld = World([arena1, arena2])

while True:
    myWorld.simulate_day()




