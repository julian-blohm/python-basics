## arithmetic operators https://www.w3schools.com/python/python_operators.asp 
# exponential
print(2 ** 3) # = 8
print(2. ** 3.) # = 8.0
print(2 ** 3.) # = 8.0
print(2. ** 3) # = 8.0
print("")

# multiplication
print(2 * 3) # = 6
print(2. * 3.) # = 6.0
print(2 * 3.) # = 6.0
print(2. * 3) # = 6.0
print("")

# division
print(10 / 2) # = 5.0
print(10. / 2.) # = 5.0
print(10 / 2.) # = 5.0
print(10. / 2) # = 5.0
print("")

# floor division
print(10 // 2) # = 5
print(10. // 2.) # = 5.0
print(10 // 2.) # = 5.0
print(10. // 2) # = 5.0
print(6. / 4) # = 1.5
print(6. // 4) # = 1.0
print(6. / -4) # = -1.5
print(6. // -4) # = -2.0
print("")

# modulo
print(4 % 2) # = 0 (übrig)
print(5 % 2) # = 1

# addition
print(6 + 4) # = 10
print(6. + 4) # = 10.0
print(6. + 4.) # = 10.0

# subtraction
print(6 - 4) # = 2
print(6. - 4) # = 2.0
print(6. - 4.) # = 2.0

# priority
## 1: '+' '-' als vorzeichen
## 2: '**'
## 3: '*' '/' '//' '%'
## 4: '+' '-'

print(10 - 6 ** 2 / 9 * 10 + 1) # 1: **
print(10 - 36 / 9 * 10 + 1) # 2: / (weil weiter links) 
print(10 - 4 * 10 + 1) # 3: *
print(10 - 40 + 1) # 4: - (von links)
print(-30 + 1) 

# mit klammern kann reihenfolge definiert werden
print((10 - 6) ** 2 / (9 * 10) + 1)
