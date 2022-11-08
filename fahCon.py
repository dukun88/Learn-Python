print(10*'=','FAHRENHEIT CONVERTER',10*'=')

fahrenheit = float(input('Masukan Suhu Fahrenheit : '))
print('Suhu = ', fahrenheit,'`F')

celcius = ((5/9)* fahrenheit) + 32
print('Suhu Celcius = ', celcius, '`C')

reamur = ((4/9)* fahrenheit) - 32
print('Suhu Reamue  = ', reamur, ' `R')

kelvin = (((5/9)* fahrenheit) + 32) + 273
print('Suhu Kelvin  = ', kelvin, ' K')