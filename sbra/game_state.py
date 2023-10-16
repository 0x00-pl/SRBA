

class GameState:
    def __init__(self, tick=0):
        self.version = 0
        self.tick = tick
        self.entity_list = []

    def from_json(self, json_data):
        pass

    def to_json(self):
        return {
            "version": self.version,
            "tick": self.tick,
            "entity_list": [entity.to_json() for entity in self.entity_list]
        }

