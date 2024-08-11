
# bitwise operators allow to manipulate single bits of data, 
# and return 0 or 1 based on the value of the bits that are used
# https://www.geeksforgeeks.org/python-bitwise-operators/
# & - conjunction
# | - disjunction
# ~ - negation
# ^ - exlusive or

# print as binary
print(bin(15)) # 00001111
print(bin(22)) # 00010110 

# calculate using conjunction
print(15 & 22) # 00000110 => 6 als integer

# calculate using disjunction
print(15 | 22) # 00011111 => 31 als integer

# calculate using exlusive or
print(15 ^ 22) # 000011001 => 31 als integer

# calculate using negation
print(~22) # 11101001 => -23 als integer

## bit shifting
# bit shift right >>
print(22 >> 1) # shift all bits to right by 1 => from 00010110 to 00001011 (= 11 als int)

# bit shift left <<
print(22 << 1) # shift all bits to left by 1 => from 00010110 to 00101100 (= 44 als int)