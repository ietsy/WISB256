from math import sqrt

class Vector:
    """Represents a vector
    """
    
    
    
    def __init__(self, n=3, value=0):
        if type(value) is list:
            self.Value = value
        else:
            self.Value = n * [value]
    
    def __str__(self):
        result = ""
        for i in range(len(self.Value)):
            result = result + "%.6f\n" % (self.Value[i])
        result = result[0:len(result)-1]
        return result
        
    def lincomb(self, other, alpha, beta):
        result = len(self.Value) * [0]
        for i in range(len(self.Value)):
            result[i] = alpha * self.Value[i] + beta * other.Value[i]
        vector = Vector(len(self.Value), result)
        return vector
    
    def scalar(self, alpha):
        other = Vector(len(self.Value))
        result = self.lincomb(other, alpha, 0)
        return result
    
    def inner(self, other):
        result = 0
        for i in range(len(self.Value)):
            result = result + self.Value[i] * other.Value[i]
        return result
        
    def norm(self):
        return sqrt(self.inner(self))
        