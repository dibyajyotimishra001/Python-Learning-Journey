class CursedSpirit:
    def __init__(self, name, health_points = 100):
        self.name = name
        self.health_points = health_points

    def take_damage(self, damage_amount):
        self.health_points -= damage_amount
        if self.health_points < 0:
            self.health_points = 0
# Damage values
cleve = 120
dismental = 1200
fuga = 10000
molevorent_shrine = 100000

sukuna = CursedSpirit("Jogo")
sukuna.take_damage(cleve)
print(f"Remaining Health: {sukuna.health_points}")      