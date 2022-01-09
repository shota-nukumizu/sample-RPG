class Unit:

    def __init__(self, name, hp, mp, attack, defence, speed, resistance, skill, lv, job):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.attack = attack
        self.defence = defence
        self.speed = speed
        self.resistance = resistance
        self.skill = skill
        self.lv = lv
        self.job = job
    
    def __str__(self):
        return self.name
    
    def show_status(self):
        return f'{self.name} | HP: {self.hp}, MP: {self.mp}, LEVEL: {self.lv}, JOB: {self.job}'
    
    def show_more_status(self):
        return f'''
        Name: {self.name}
        HP: {self.hp}
        MP: {self.mp}
        LEVEL: {self.lv}
        JOB: {self.job}
        ATK: {self.attack}
        DEF: {self.defence}
        RES: {self.resistance}
        SKILL: {self.skill}
        '''