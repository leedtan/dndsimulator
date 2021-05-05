class PreserveLife:
    def __init__(self):
        self.time = "action"
        pass

    def check_cast(self, allies, enemies):
        num_dead = len([ally for ally in allies if ally.hp == 0])
        return len(num_dead >= 2)

    def cast(self, allies, enemies):
        targets = [ally for ally in allies if ally.hp == 0]
        num_targets = len(targets)
        amount_heal = 15 // num_targets
        for target in targets:
            target.hp += amount_healed
        return True
