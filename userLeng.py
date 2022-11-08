import datetime
import os
import string
import random

formTemplate = {
    'nama' : 'nama',
    'email' : 'example@tolol.com',
    'nohp' : 0,
    'ttl' : datetime.datetime(1111,1,11)
}
dataUser = {}
while True:
    os.system("clear")
    print(27*"="+'REGISTRASI USER'+'='*27)
    print(f"{'SILAHKAN ISI FORM BERIKUT UNTUK MENDAFTAR':^66}\n\n")

    user = dict.fromkeys(formTemplate.keys()) #mengambil template dictionary
    user['nama'] = input("Nama Lengkap : ")
    user['email'] = input("Alamat Email : ")
    user['nohp'] = int(input("No. Handphone (+62) : "))
    TAHUN_LAHIR = int(input("Tahun Lahir (YYYY) :"))
    BULAN_LAHIR = int(input("Bulan Lahir (MM): "))
    TANGGAL_LAHIR = int(input("Tanggal Lahir (DD): "))
    user['ttl'] = datetime.datetime(TAHUN_LAHIR,BULAN_LAHIR,TANGGAL_LAHIR)

    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6))) #membuat key random 
    dataUser.update({KEY:user})

    print(f"\n{'Key':<6} {'Nama':<12} {'Email':<17} {'No.Hp':<16} {'Tanggal Lahir':<10}")
    print(70*'-')

    for user in dataUser:
        KEY = user
        NAMA = dataUser[KEY]['nama']
        EMAIL = dataUser[KEY]['email']
        NOHP = dataUser[KEY]['nohp']
        TTL = dataUser[KEY]['ttl'].strftime("%x")

        print(f"{KEY:<6} {NAMA:<12} {EMAIL:<17} 0{NOHP:<15} {TTL:<10}")
    
    
    print('\n\n'+70*'=')

    confirm = input("Ingin menambahkan User lain ? (y/n) ")

    if confirm == "n" :
        break
print(29*'='+'TERIMA KASIH'+'='*29)