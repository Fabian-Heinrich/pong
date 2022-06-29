from __future__ import annotations

class Position:
    def __init__(self, x, y) -> None:
        self.position = self.x, self.y = x, y

    def __add__(self, other: Position) -> Position:
        return Position(self.x+other.x, self.y+other.y) 
    
    def __mul__(self, other: Position) -> Position:
        return Position(self.x*other.x, self.y*other.y)

    def get_pos(self):
        return (self.x, self.y)
