import math

if __name__ == '__main__':

    class Fraction:
        def __init__(self, numerator, denominator):
            self.numerator = numerator
            if denominator:
                self.denominator = denominator
            else:
                raise ZeroDivisionError

        def __str__(self):
            return f"{self.numerator}/{self.denominator}"

        def __add__(self, other):
            # new_numerator = (self.numerator * other.denominator) + (self.denominator * other.denominator)
            # new_denominator = self.denominator * other.denominator
            new_denominator = (self.denominator * other.denominator) // math.gcd(self.denominator, other.denominator)
            new_numerator = self.numerator * (new_denominator // self.denominator) + other.numerator * (new_denominator // other.denominator)

            gcd = math.gcd(new_numerator, new_denominator)

            simplified_num = new_numerator // gcd
            simplified_denom = new_denominator // gcd

            return f"{simplified_num}/{simplified_denom}"

        def __sub__(self, other):
            new_denominator = (self.denominator * other.denominator) // math.gcd(self.denominator, other.denominator)
            new_numerator = self.numerator * (new_denominator // self.denominator) - other.numerator * (
                        new_denominator // other.denominator)

            gcd = math.gcd(new_numerator, new_denominator)

            simplified_num = new_numerator // gcd
            simplified_denom = new_denominator // gcd

            return f"{simplified_num}/{simplified_denom}"

        def inverse(self):
            return f"{self.denominator}/{self.numerator}"


    first_fraction = Fraction(8, 6)
    second_fraction = Fraction(5, 3)
    print(first_fraction + second_fraction)
    print(first_fraction - second_fraction)
    print(first_fraction.inverse())