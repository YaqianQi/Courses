import math
class Complex:
    # Part 1
    def __init__(self, re=0, im=0):
        if isinstance(re, (float, int)) and isinstance(im, (float, int)):
            self.re = re
            self.im = im
        else:
            raise TypeError

    def __str__(self):
        return f'{self.re}{"+" if self.im >= 0 else ""}{self.im}i'
    # Part 2
    def __add__(self, other):
        if isinstance(other, Complex):
            new_re = self.re + other.re
            new_im = self.im + other.im
        elif isinstance(other, (float, int)):
            new_re = self.re + other
            new_im = self.im
        else:
            raise TypeError

        return Complex(new_re, new_im)
    
    def __sub__(self, other):
        if isinstance(other, Complex):
            new_re = self.re - other.re
            new_im = self.im - other.im
        elif isinstance(other, (float, int)):
            new_re = self.re - other
            new_im = self.im
        else:
            raise TypeError

        return Complex(new_re, new_im)

    # Part 3
    
    def __mul__(self, other):
        if isinstance(other, Complex):
            new_re = self.re * other.re - self.im * other.im
            new_im = self.re * other.im + self.im * other.re
        elif isinstance(other, (float, int)):
            new_re = self.re * other
            new_im = self.im * other
        else:
            raise TypeError

        return Complex(new_re, new_im)
    
    def __truediv__(self, other):
        if isinstance(other, Complex):
            denominator = other.re ** 2 + other.im ** 2
            new_re = (self.re * other.re + self.im * other.im) / denominator
            new_im = (-self.re * other.im + self.im * other.re) / denominator
        elif isinstance(other, (float, int)):
            new_re = self.re / other
            new_im = self.im / other
        else:
            raise TypeError

        return Complex(new_re, new_im)

    # Part 4
    def __eq__(self, other):
        return self.re == other.re and self.im == other.im

    def __abs__(self):
        return math.sqrt(self.re ** 2 + self.im ** 2)

