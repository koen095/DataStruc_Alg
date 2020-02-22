# GCD function
def gcd(m, n):
    while m % n != 0:
        old_m = m
        old_n = n

        m = old_n
        n = old_m % old_n
    return n 

# Fraction class
# Implements: addition, equality, multiplication
# TO DO: division, subtraction and comparison operators (<, >)
class Fraction:

    def __init__(self, top, bottom):
        try:
            self.num = int(top) 
            self.den = abs(int(bottom))
        except ValueError:
            print("both numerator and denominator must be integers") 


    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def show(self):
        print(self.num, "/", self.den)

    def get_num(self):
        print(self.num)

    def get_den(self):
        print(self.den) 

    def __add__(self, other_fraction):
        new_num = self.num * other_fraction.den + \
                  self.den * other_fraction.den
        new_den = self.den * other_fraction.den
        common = gcd(new_num, new_den)
        return Fraction(new_num // common, new_den // common)

    def __eq__(self, other):
        first_num = self.num * other.den
        second_num = other.num * self.den

        return first_num == second_num

    def __mul__(self, other_fraction):
        new_num = self.num * other_fraction.num 
        new_den = self.den * other_fraction.den
        common = gcd(new_num, new_den)

        return Fraction(new_num // common, new_den // common)

    def __truediv__(self, other_fraction):
        new_num = self.num * other_fraction.den
        new_den = self.den * other_fraction.num
        common = gcd(new_num, new_den)

        return Fraction(new_num // common, new_den // common)
    
    def __sub__(self, other_fraction):
        new_num = self.num * other_fraction.den - \
                  self.den * other_fraction.num
        new_den = self.den * other_fraction.den 
        common = gcd(new_num, new_den)

        return Fraction(new_num // common, new_den // common)

    def __lt__(self, other):
        first_num = self.num * other.den
        second_num = other.num * self.den

        return first_num < second_num

    def __gt__(self, other):
        first_num = self.num * other.den
        second_num = other.num * self.den

        return first_num > second_num

    def __le__(self, other):
        first_num = self.num * other.den
        second_num = other.num * self.den

        return first_num <= second_num

    def __ge__(self, other):
        first_num = self.num * other.den
        second_num = other.num * self.den

        return first_num >= second_num

    def __ne__(self, other):
        first_num = self.num * other.den
        second_num = other.num * self.den

        return first_num != second_num

x = Fraction(1, 2)
y = Fraction(2, 3)

print(x + y)
print(x == y)
print(x * y)
print(x / y)
print(x - y)
print(x < y)
print(x > y)
x.get_num()
x.get_den()
print(x <= y)
print(x >= y)
print(x != y)