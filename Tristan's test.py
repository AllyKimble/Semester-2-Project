class Zombie_Boss:
    def __init__(self, hp, speed, damage):
        self.hp = hp
        self.speed = speed
        self.damage = damage
boss = Zombie_Boss(150, 5, 15)
print(boss.hp, boss.speed, boss.damage)