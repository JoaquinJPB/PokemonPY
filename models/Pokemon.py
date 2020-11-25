from constants import *
class Pokemon:

    def __init__(self, name, level, type1, type2):
        self.name = name
        self.level = level
        self.type1 = type1
        self.type2 = type2
        self.attacks = [] # Vector de ataques
        self.baseStats = {}
        self.stats = {}
        self.ev = {}
        self.iv = {}
        self.current_status = 0
        self.current_hp = 0
        self.nature = 0

    def compute_stats(self):
        self.stats = {
            HP: self.compute_hp_stat(),
            ATTACK: self.compute_standard_stat(ATTACK),
            DEFENSE: self.compute_standard_stat(DEFENSE),
            SPATK: self.compute_standard_stat(SPATK),
            SPDEF: self.compute_standard_stat(SPDEF),
            SPEED: self.compute_standard_stat(SPEED)
        }
        pass

    def compute_standard_stat(self, stat):
        value1 = (2 * self.baseStats[stat] + self.iv[stat] + int(self.ev[stat] / 4)) * self.level
        return (int(value1 / 100) + 5) * NATURE_MATRIX[self.nature][stat]
        pass

    def compute_hp_stat(self):
        value1 = (2 * self.baseStats["HP"] + self.iv["HP"] + int(self.ev["HP"] / 4)) * self.level
        return int(value1 / 100) + self.level + 10
        pass

class Attack:

    def __init__(self, name, t, category, pp, power, accuracy):
        self.name = name
        self.type = t
        self.category = category
        self.pp = pp
        self.power = power
        self.accuracy = accuracy