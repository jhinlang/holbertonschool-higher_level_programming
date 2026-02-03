class Unity:
    def __init__(self, name="", health=100):
        self.name = name
        self.health = health

    @property
    def health(self):
        return self._health

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("name must be str")
        self._name = value

    @health.setter
    def health(self, value):
        if not isinstance(value, int):
            raise TypeError("Health must be an integer")
        self._health = value