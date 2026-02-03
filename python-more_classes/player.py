class Player(Unity):
    def __init__(self, name="", health=100, level=1):
        super().__init__(name, health)
        self.level = level

    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self, value):
        if level == 100:
            raise ValueError("Vous avez atteint le niveau max, félicitations")
        else:
            value += 1
        self.level = value

    @property
    def restore_health(self):
        return self.restore_life
    
    @restore_health.setter
    def restore_health(self, value):
        if self.health == 100:
            raise ValueError("Vous ne pouvez pas vous soigner, votre vie est pleine")
        else:
            value += 20
        self.restore_health = value
        super().health(health)
        