class Animal:
    def __init__(self,name="", health=100, position=0):
        super().__init__(name, health)
        self.position = position
        