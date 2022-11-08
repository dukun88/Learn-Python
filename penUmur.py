import datetime as dt

print(10*'='+'PENGHITUNG UMUR'+'='*10)
tdy = dt.date.today()
print(f'Hari ini : {tdy}')
print(f'Masukan Tanggal lahir !')

tgl = int(input('Tanggal \t : '))
bln = int(input('Bulan \t\t : '))
thn = int(input('Tahun \t\t : '))

ttl = dt.date(thn,bln,tgl)
print(f'Tanggal Lahir : {ttl:%A},{ttl}')

umrHari = tdy - ttl
umrThn = umrHari.days // 365
umrBlnSisa = (umrHari.days % 365) // 30

print(f'Umur Anda adalah : \n {umrThn} Tahun, {umrBlnSisa} Bulan.')