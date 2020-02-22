# GCD function
def gcd(m, n):
    while m % n != 0:
        old_m = m
        old_n = n

        m = old_n
        n = old_m % old_n
    return n 

# Fraction class
# Implements: addition and equality
# TO DO: multiplication, division, subtraction and comparison operators (<, >)
class Fraction:

    def __init__(self, top, bottom):
        self.num = top 
        self.den = bottom 

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def show(self):
        print(self.num, "/", self.den)

x = Fraction(1, 2)
y = Fraction(2, 3)
print(x + y)