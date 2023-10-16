from typing import List

from sbra.entity import Entity
from sbra.state_base import StateBase
from sbra.game_state import GameState


class Game(StateBase):
    def __init__(self):
        self.tick = 0
        self.entity_list: List[Entity] = []

    def save_state(self) -> GameState:
        state = GameState(
            tick=self.tick
        )
        return state

    def load_state(self, state: GameState):
        pass

    def get_brain(self, entity: Entity):
        return None

    def tick(self):
        for entity in self.entity_list:
            entity.tick(self, self.get_brain(entity))
        self.tick += 1
