class Unit:

    def __init__(self, name, hp, mp, attack, defence, speed, resistance, skill, lv):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.attack = attack
        self.defence = defence
        self.speed = speed
        self.resistance = resistance
        self.skill = skill
        self.lv = lv
    
    def __str__(self):
        return self.name
    