class Fractional():
    
    x: int
    y: int

    def __init__(self, x:int, y:int = 1):
        self.x = x
        if y == 0:
            raise ValueError("Y value of fractional cannoot be zero!")
        self.y = y

    
    def __str__(self):
        return f"{self.x}/{self.y}"
    
    def __repr__(self):
        return f"Fractional({self.x}, {self.y})"
    
    def __add__(self, fract):
        if type(fract) == int:
            fract = Fractional(fract,1)
        x_n = self.x * fract.y + self.y * fract.x
        y_n = self.y * fract.y
        return Fractional(x_n, y_n)
    
    def __radd__(self, another_val):
        if type(another_val) == int:
            fract = Fractional(another_val,1)
            x_n = self.x * fract.y + self.y * fract.x
            y_n = self.y * fract.y
            return Fractional(x_n, y_n)

        elif type(another_val)== float:
            decx = self.to_decimal()
            return another_val + decx 
        
    def __mul__(self, fract):
        x_n = self.x * fract.x
        y_n = self.y * fract.y
        return Fractional(x_n, y_n)
    
    def __sub__(self, fract):
        x_n = self.x * fract.y - self.y * fract.x
        y_n = self.y * fract.y
        return Fractional(x_n, y_n)
    
    def __truediv__(self, fract):
        x_n = self.x * fract.y
        y_n = self.y * fract.x
        return Fractional(x_n, y_n)
    
    def to_decimal(self):
        return self.x / self.y
    
    def __lt__(self, fract):
        verify = self.to_decimal() < fract.to_decimal()
        return verify
    
    def __gt__(self, fract):
        verify = self.to_decimal() > fract.to_decimal()
        return verify
    
    def __le__(self, fract):
        verify = self.to_decimal() <= fract.to_decimal()
        return verify
    
    def __ge__(self, fract):
        verify = self.to_decimal() >= fract.to_decimal()
        return verify
    
    def __eq__(self, fract):
        verify = self.to_decimal() == fract.to_decimal()
        return verify

if __name__ == '__main__':
    print("Ran. You can use this py file in other projects.")