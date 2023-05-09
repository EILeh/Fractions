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
