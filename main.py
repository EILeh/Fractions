"""
Fractions

The program asks the user to input fractions and then prints their simplified
form. By entering an empty line, the program will do the printing.

The program contains an implementation of the class Fraction that represents
one fraction The constructor uses the raise command to raise an exception in
error situations, ie. if the builder is given wrong parameters. The
return_string method works only if the data type of the fraction's numerator and
denominator is integer. The method return_string does not only return a string-
presentation of the fraction. The method also puts the minus character before
the numerator or, if the numerator and the denominator are both negative,
removes the minus characters entirely. A fraction may thus be simplified
slightly. A simplify method simplifies the fraction by dividing the numerator
and the denominator with their greatest common divisor. A function in the file
greatest_common_divisor calculates the greatest common divisor. As the
return_string method ensures that the minus characters are always printed before
the numerators.

What program returns from fraction:
- simplify
- complement
- reciprocal
- multiply
- division
- add
- deduct
- comparison

Writer of the program: EILeh

"""

class Fraction:
    """
    This class represents one single fraction that consists of
    numerator (osoittaja) and denominator (nimittäjä).
    """

    def __init__(self, numerator, denominator):
        """
        Constructor. Checks that the numerator and denominator are of
        correct type and initializes them.

        :param numerator: int, fraction's numerator
        :param denominator: int, fraction's denominator
        """

        # isinstance is a standard function which can be used to check if
        # a value is an object of a certain class.  Remember, in Python
        # all the data types are implemented as classes.
        # ``isinstance(a, b´´) means more or less the same as ``type(a) is b´´
        # So, the following test checks that both parameters are ints as
        # they should be in a valid fraction.
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError

        # Denominator can't be zero, not in mathematics, and not here either.
        elif denominator == 0:
            raise ValueError

        self.__numerator = numerator
        self.__denominator = denominator

    # FI: Käänteisluku
    def reciprocal(self):
        return Fraction(self.__denominator, self.__numerator)

    # FI: Vastaluku
    def complement(self):
        return Fraction(-self.__numerator, self.__denominator)

    def multiply(self, other):

        # Initializes a new variable that stores the information of
        # multiplied numerator.
        new_numerator = self.__numerator * other.__numerator

        # Initializes a new variable that stores the information of
        # multiplied denominator.
        new_denominator = self.__denominator * other.__denominator

        # Returns the new fraction.
        return Fraction(new_numerator, new_denominator)

    def divide(self, other):
        # When dividing fractions, the division can be done by multiplying
        # the first fraction with the second fraction's reciprocal.

        # Initializes a new variable that stores the information of
        # divided numerator.
        new_numerator = self.__numerator * other.__denominator

        # Initializes a new variable that stores the information of
        # divided denominator.
        new_denominator = self.__denominator * other.__numerator

        # Returns the new fraction.
        return Fraction(new_numerator, new_denominator)

    def add(self, other):
        # When adding fractions together, the denominator must be the same
        # and to do that both fractions' denominators and numerators are
        # multiplied with each other denominators.

        # Initializes a new variable that stores the information of
        # multiplied numerator.
        new_numerator = self.__numerator * other.__denominator

        # Initializes a new variable that stores the information of
        # multiplied denominator.
        new_denominator = self.__denominator * other.__denominator

        # Initializes a new variable that stores the information of
        # multiplied numerator of the other fraction.
        new_other_numerator = other.__numerator * self.__denominator

        # Initializes a new variable that stores the information of
        # numerators added together.
        numerator_added = new_numerator + new_other_numerator

        # Returns the new fraction.
        return Fraction(numerator_added, new_denominator)

    def __It__(self, other):
        # When comparing fractions, the denominator must be the same
        # and to do that both fractions' denominators and numerators are
        # multiplied with each other denominators.

        # Initializes a new variable that stores the information of
        # multiplied numerator.
        new_numerator = self.__numerator * other.__denominator

        # Initializes a new variable that stores the information of
        # multiplied numerator of the other fraction.
        new_other_numerator = other.__numerator * self.__denominator

        return new_numerator < new_other_numerator

    def __gt__(self, other):
        # When comparing fractions, the denominator must be the same
        # and to do that both fractions' denominators and numerators are
        # multiplied with each other denominators.

        # Initializes a new variable that stores the information of
        # multiplied numerator.
        new_numerator = self.__numerator * other.__denominator

        # Initializes a new variable that stores the information of
        # multiplied numerator of the other fraction.
        new_other_numerator = other.__numerator * self.__denominator

        return new_numerator > new_other_numerator

    def __str__(self):
        return f"{self.__numerator}/{self.__denominator}"

    def deduct(self, other):
        # When deducting fractions, the denominator must be the same and to do
        # that both fractions' denominators and numerators are multiplied
        # with each other denominators.

        # Initializes a new variable that stores the information of
        # multiplied numerator.
        new_numerator = self.__numerator * other.__denominator

        # Initializes a new variable that stores the information of
        # multiplied denominator.
        new_denominator = self.__denominator * other.__denominator

        # Initializes a new variable that stores the information of
        # multiplied numerator of the other fraction.
        new_other_numerator = other.__numerator * self.__denominator

        # Initializes a new variable that stores the information of deducted
        # numerators.
        numerator_deducted = new_numerator - new_other_numerator

        # Returns the new fraction.
        return Fraction(numerator_deducted, new_denominator)

    def simplify(self):
        # Stores the value of the greatest common divisor in the variable
        # greatest_common.
        greatest_common = greatest_common_divisor(self.__numerator,
                                                  self.__denominator)

        # Stores a new value to the numerator by dividing the numerator by
        # the greatest common divisor.
        self.__numerator = self.__numerator // greatest_common

        # Stores a new value to the denominator by dividing the denominator by
        # the greatest common divisor.
        self.__denominator = self.__denominator // greatest_common

        # Calls the function return_string that prints the fraction in wanted
        # form after new values have been stored to the numerator and
        # denominator.
        return self.return_string()


    def return_string(self):
        """
        :returns: str, a string-presentation of the fraction in the format
                       numerator/denominator.
        """

        if self.__numerator * self.__denominator < 0:
            sign = "-"

        else:
            sign = ""

        return f"{sign}{abs(self.__numerator)}/{abs(self.__denominator)}"


def greatest_common_divisor(a, b):
    """
    Euclidean algorithm. Returns the greatest common
    divisor (suurin yhteinen tekijä).  When both the numerator
    and the denominator is divided by their greatest common divisor,
    the result will be the most reduced version of the fraction in question.
    """

    while b != 0:
        a, b = b, a % b

    return a

def main():
    original = Fraction(2, 3)
    other = Fraction(1, 6)
    complement = original.complement()
    reciprocal = original.reciprocal()
    multiplied = original.multiply(other)
    quotient = original.divide(other)
    sum = original.add(other)
    sum.return_string()
    difference = original.deduct(other)
    compare = original.__It__(other)
    compares = original.__gt__(other)
    difference.return_string()

    list_of_fractions = []
    is_input_empty = False

    print(f"Enter fractions in the format integer/integer.")
    print(f"One fraction per line. Stop by entering an empty line.")

    while not is_input_empty:
        user_input = input()
        stripped_input = user_input.strip()

        if stripped_input == "":
            is_input_empty = True
            break

        split_input = user_input.split("/")

        numerator = int(split_input[0])
        denominator = int(split_input[1])

        fraction = Fraction(numerator, denominator)
        list_of_fractions.append(fraction)

    print(f"The given fractions in their simplified form:")

    for fraction_in_list in list_of_fractions:
        print(f"{fraction_in_list} = {fraction_in_list.simplify()}")

if __name__ == "__main__":
    main()