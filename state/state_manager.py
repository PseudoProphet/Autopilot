class StateManager:
    def __init__(self):
        self.state = {}

    def update_state(self, key, value):
        self.state[key] = value

    def get_state(self, key):
        return self.state.get(key, None)

    def clear_state(self):
        self.state = {}
