

class Warrior:
    AVAILABLE_RANKS = ["Pushover", "Novice", "Fighter", "Warrior", "Veteran", "Sage", "Elite",
                       "Conqueror", "Champion", "Master", "Greatest"]

    def __init__(self, experience, achievements):
        self.experience = experience
        self.achievements = achievements

    def battle(self, opponent_level: int):
        if opponent_level < 1 or opponent_level > 100:
            return "Invalid level!"
        elif self.level == opponent_level:
            self.experience += 10
            return "A good fight"
        elif self.level - opponent_level == 1:
            self.experience += 5
            return "A good fight",
        elif self.level - opponent_level > 1:
            return "Easy fight"
        elif 1 <= opponent_level - self.level <= 9:
            self.experience += 20 * (opponent_level - self.level) ** 2
            return "An intense fight"
        elif opponent_level - self.level > 4 and opponent_level // 10 > self.level // 10:
            return "You've been defeated"

    @property
    def level(self):
        return self.experience // 100

    @property
    def rank(self):
        return self.AVAILABLE_RANKS[self.level // 10]

    def training(self, training_name: str, exp_cost: int, necessary_lvl: int):
        if self.level >= necessary_lvl:
            self.experience += exp_cost
            self.achievements.append(training_name)
            return training_name
        else:
            return "Not strong enough"


if __name__ == "__main__":
    warrior = Warrior(100, [])
    print(warrior.training("Defeated Jackie Chan with chair", 1000, 1))
    print("rank =", warrior.rank, "experience =", warrior.experience, "level = ", warrior.level)
    print(warrior.battle(8))
    print("rank =", warrior.rank, "experience =", warrior.experience, "level = ", warrior.level)
    print(warrior.battle(8))
    print("rank =", warrior.rank, "experience =", warrior.experience, "level = ", warrior.level)
    print(warrior.battle(20))
    print("rank =", warrior.rank, "experience =", warrior.experience, "level = ", warrior.level)
    print(warrior.battle(30))
    print("rank =", warrior.rank, "experience =", warrior.experience, "level = ", warrior.level)
    print(warrior.battle(40))
    print("rank =", warrior.rank, "experience =", warrior.experience, "level = ", warrior.level)
    print(warrior.battle(99))
    print("rank =", warrior.rank, "experience =", warrior.experience, "level = ", warrior.level)
    print(warrior.battle(30))
    print(warrior.training("Defeated Jackie Chan with chair", 1000, 1))
    print(warrior.training("Defeated Jackie Chan with chair", 1000, 1))
    print(warrior.battle(40))
    print("rank =", warrior.rank, "experience =", warrior.experience, "level = ", warrior.level, warrior.achievements)


