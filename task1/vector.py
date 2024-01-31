import math

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __add__(self, other):
        if isinstance (other, Vector):
            return Vector (self.x + other.x, self.y + other.y)
        raise ValueError("nejde o vektor")
    
    def __sub__(self, other):
        if isinstance (other, Vector):
            return Vector (self.x - other.x, self.y - other.y)
        raise ValueError("nejde o vektor")
    
    def __mul__(self, other):
        if isinstance (other, (int, float)):
            return Vector (self.x * other, self.y * other)
        raise ValueError("nejde o float ani int")
    


