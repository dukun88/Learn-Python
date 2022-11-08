print(20*'=')
print('KALKULATOR SEDERHANA')
print(20*'=')

num1 = float(input('Angka Pertama: '))
opr = input('(+)(x)(-)(/) :')
num2 = float(input('Angka Kedua: '))

if opr == '+':
    hasil = num1 + num2
    print(hasil)
elif opr == '-':
    hasil = num1 - num2
    print(hasil)
elif opr == 'x':
    hasil = num1 * num2
    print(hasil)
elif opr == '/':
    hasil = num1 / num2
    print(hasil)
else:
    print('Harap masukan Dengan benar !')