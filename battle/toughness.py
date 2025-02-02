class Toughness:
    """
    韧性条系统
    """

    def __init__(self, length):
        self.length = length
        self.current_length = length

    def recover(self):
        self.current_length = self.length

    def damage(self, toughness_damage):
        self.current_length = max(0, self.current_length - toughness_damage)
        if self.current_length == 0:
            return True
        return False
