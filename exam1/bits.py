import math

# print base 2 logarithm of pi and e to 5 digits of precision
# separate values with a tab
# use math.log2(), math.pi, and math.e

log2pi = math.log2(math.pi)
log2e  = math.log2(math.e)

print(f'{log2pi:.5f}\t{log2e:.5f}')