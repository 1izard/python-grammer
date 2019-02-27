'''
If express fraction with limitless of precision -> fractions.Fractions
'''
# Calculate precisely and round up
rate = 1.45
seconds = 3*60 + 42
cost = rate * seconds / 60
print('cost =', cost)
print('round(cost, 2) =', round(cost, 2))
# cost = 5.364999999999999
# round(cost, 2) = 5.36

from decimal import Decimal, ROUND_UP
rate = Decimal('1.45')
seconds = 3*60 + 42
seconds = Decimal(str(seconds))
cost = rate * seconds / Decimal('60')
rounded = cost.quantize(Decimal('0.01'), rounding=ROUND_UP)
print('cost =', cost)
print('rounded =', rounded)
# cost = 5.365
# rounded = 5.37



# Round up small value
rate = 0.05
seconds = 5
cost = rate * seconds / 60
print('cost =', cost)
print('round(cost, 2) =', round(cost, 2))
# cost = 0.004166666666666667
# round(cost, 2) = 0.0

from decimal import Decimal, ROUND_UP
rate = Decimal('0.05')
seconds = Decimal('5')
cost = rate * seconds / Decimal('60')
rounded = cost.quantize(Decimal('0.01'), rounding=ROUND_UP)
print('cost =', cost)
print('rounded =', rounded)
# cost = 0.004166666666666666666666666667
# rounded = 0.01
