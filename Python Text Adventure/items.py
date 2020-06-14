
class Weapon:
    def __init__(self):
        raise NotImplementedError("Do not create raw Weapon objects.")

    def __str__(self):
        return self.name

class Rock(Weapon):
    def __init__(self):
        self.name = "Rock"
        self.description = "A fist sized rock, suitable for bludgeoning."
        self.damage = 5
        self.value = 1

class Dagger(Weapon):
    def __init__(self):
        self.name = "Dagger"
        self.description = "A small dagger with some rust. Somewhat more dangerous than a rock."
        self.damage = 10
        self.value = 20

class RustySword(Weapon):
    def __init__(self):
        self.name = "Rusty Sword"
        self.description = "This sword is showing it's age, but it's still got some fight left in it."
        self.damage = 20
        self.value = 50

class Consumables:
    def __init__(self):
        raise NotImplementedError("Do not create raw Consumable objects.")


    def __str__(self):
        return "{} (+{} HP)".format(self.name, self.healing_value)

class CrustyBread(Consumables):
    def __init__(self):
        self.name = "Crusty Bread"
        self.healing_value = 10
        self.value = 12

class HealingPotion(Consumables):
    def __init__(self):
        self.name = "Healing Potion"
        self.healing_value = "50"
        self.value = 30
