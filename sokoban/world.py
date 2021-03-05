class WorldObject(object):
    def __init__(self):
        self.is_player = False
        self.is_crate = False
        self.is_wall = False
        self.is_goal = False

    def is_empty(self):
        return (not self.is_player) and (not self.is_crate) and (not self.is_wall) and (not self.is_goal)


class World(object):
    def __init__(self):
        self.height = 0
        self.width = 0
        self.map = []
    
    def has_player_won(self):

        pass

