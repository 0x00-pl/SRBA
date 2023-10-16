from sbra.state_base import StateBase


class Entity(StateBase):
    def __init__(self):
        pass

    def save_state(self):
        pass

    def load_state(self, state):
        pass

    def tick(self, state, brain):
        pass
