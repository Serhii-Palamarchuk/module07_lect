from decimal import Decimal as d, getcontext, ROUND_HALF_EVEN, ROUND_HALF_UP, ROUND_HALF_DOWN


getcontext().prec = 5

f = 0.2 + 0.1 + 0.3 - 0.5
print(f)

f2 = d('0.2') + d('0.1') + d('0.3') - d('0.5')
print(f2)


print(d('3') / d('25'))

num = d('1.45')

print(num.quantize(d('1.0'), rounding=ROUND_HALF_EVEN))
print(num.quantize(d('1.0'), rounding=ROUND_HALF_UP))
print(num.quantize(d('1.0'), rounding=ROUND_HALF_DOWN))


print(d('1.0').compare(d('1.1')))   