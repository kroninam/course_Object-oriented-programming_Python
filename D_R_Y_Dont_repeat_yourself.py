#D.R.Y = Don't repeat yourself

# Compare:
#1
class Point:
    def __init__(self, coord_x, coord_y):
        self.x = coord_x
        self.y = coord_y

    def move_to(self, move_to_x, move_to_y):
        self.x = move_to_x
        self.y = move_to_y

    def go_home(self, home_x = 0, home_y = 0):
        self.x = home_x
        self.y = home_y

#2
class Point:
    def __init__(self, coord_x, coord_y):
        self.move_to(coord_x, coord_y)

    def move_to(self, move_to_x, move_to_y):
        self.x = move_to_x
        self.y = move_to_y

    def go_home(self, home_x=0, home_y=0):
        self.move_to(0, 0)
