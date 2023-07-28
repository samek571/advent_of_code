from fractions import Fraction    
from  decimal import Decimal
from fractions import Fraction

class Solution:

    def irreducible_fraction(self, num):
        frac = Fraction(num).limit_denominator()
        return frac.numerator, frac.denominator



    def fractionAddition(self, expression: str) -> str:
        n, e = self.irreducible_fraction(eval(expression))
        return str(n) + "/" + str(e)
