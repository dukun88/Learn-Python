print(10*'=','APAKAH BERAT BADANMU IDEAL ?',10*'=')

inputUser = float(input('Masukan Berat Badan : '))
print('Berat Badan = ', inputUser)

if inputUser < 38 : 
    print('Kamu Kurus')
    print('Ayo Makan yg Banyak')
elif inputUser > 49 :
    print('Kamu Gendut')
    print('Ayo Diet dan banyak Berolahraga')
elif inputUser > 38 < 49 :
    print('Kamu ideal')
    print('Pertahankan Hidup Sehatmu')
else:
    print('Kamu belum Memasukan Berat Badan mu !')
