

class Arena():


    def __init__(self, m_arenaName1:str, m_arenaSchedule2:list):
        self.m_arenaName1 = m_arenaName1
        self.m_arenaSchedule2 = m_arenaSchedule2

    def fill_schedule(self):
        moved_schedule = self.m_arenaSchedule2.pop(0)
        return self.m_arenaSchedule2.append(moved_schedule)

    def progress_day(self):
        print(f"Todays plan of arena {self.m_arenaName1} is {self.m_arenaSchedule2[0]}.")
        Arena.fill_schedule(self)

    def __str__(self):
        return f"Name of this arena: {self.m_arenaName1}"

class World():

    def __init__(self, m_arenaDay1:int, m_arenas2:list):
        self.m_arenaDay1 = m_arenaDay1
        self.m_arenas2 = m_arenas2


    def simulate_day(self):
        self.m_arenaDay1 += 1
        print(f"Day: {self.m_arenaDay1}")
        for x in self.m_arenas2:
            x.progress_day()


arena1 = Arena("Kako", ["freeday", "recruitment", "teamgame", "duel", "freeforall"])
arena2 = Arena("Hell", ["deathmatch", "peace", "training", "RockPaperScizzors", "extinction"])
myWorld = World(0, [arena1, arena2])

while myWorld.m_arenaDay1 <500:
    myWorld.simulate_day()



