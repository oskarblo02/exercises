binary_number = list(input('Skriv ett binärt tal: '))
value = 0

for i in range(len(binary_number)):
    digit = binary_number.pop()
    if digit == '1':
        value = value + pow(2, i)
print('ditt nummer i bas tio är: ', value)