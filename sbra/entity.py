from enum import Enum

from sbra.state_base import StateBase


class Team(Enum):
    enemy = 'enemy'
    player = 'player'


class Entity(StateBase):
    def __init__(self):
        self.team: Team = Team.enemy

    def save_state(self):
        pass

    def load_state(self, state):
        pass

    def tick(self, state, brain):
        pass
