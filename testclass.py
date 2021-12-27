from  calc_class import calculator 
from  calc_class import calculatorfix
from  calc_class import calc_input


calcfix = calculatorfix()
calc = calculator()
calcinput = calc_input(9,5)



print(calc.zarb(5,6))
print("This is output of calculator fix {}".format(calcfix.zarb()))
print("This is calc_input result {}".format(calcinput.jam()))