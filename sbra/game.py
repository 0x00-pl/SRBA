from typing import List

from sbra.brain.enemy_brain import EnemyBrain
from sbra.entity import Entity, Team
from sbra.state_base import StateBase
from sbra.game_state import GameState


class Game(StateBase):
    def __init__(self):
        self.tick = 0
        self.entity_list: List[Entity] = []
        self.enemy_brain = EnemyBrain()

    def save_state(self) -> GameState:
        state = GameState(
            tick=self.tick
        )
        return state

    def load_state(self, state: GameState):
        pass

    def get_brain(self, entity: Entity):
        if entity.team == Team.enemy:
            return self.enemy_brain
        else:
            return None

    def tick(self):
        for entity in self.entity_list:
            entity.tick(self, self.get_brain(entity))
        self.tick += 1
