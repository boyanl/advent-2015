class Pos:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self, other):
        return Pos(self.x + other.x, self.y + other.y)
        
    def __sub__(self, other):
        return Pos(self.x - other.x, self.y - other.y)
      
    def __rmul__(self, other):
        return Pos(self.x * other, self.y * other)

    def __mul__(self, other):
        return Pos(self.x * other, self.y * other)
        
    def __eq__(self, other):
        if other == None:
            return False
        return self.y == other.y and self.x == other.x

    def __lt__(self, other):
        if self.y != other.y:
            return self.y < other.y
        return self.x < other.x
    
    def __hash__(self):
        return hash((self.x, self.y))
        
    def __str__(self):
        return f'(x={self.x}, y={self.y})'

    def __repr__(self):
        return f'(x={self.x}, y={self.y})'
    
    def __copy__(self):
        return Pos(self.x, self.y)
        
    def rotate_right(self):
        return Pos(-self.y, self.x)
    
UP = Pos(0, -1)
DOWN = Pos(0, 1)
LEFT = Pos(-1, 0)
RIGHT = Pos(1, 0)

DIRS_MAP = {'^': UP, '<': LEFT, '>': RIGHT,'v': DOWN}