import os

def header():
    '''Header'''
    os.system("clear")
    print(f"{'PROGRAM PENGHITUNG LUAS':^40}")
    print(f"{'DAN KELILING PERSEGI':^40}")
    print(f"{'-'*40:^40}")

def inputUser():
    '''INPUT USER'''
    lebar = int(input('Masukan Lebar : '))
    panjang = int(input('Masukan Panjang : '))
    return lebar,panjang

def luas(lebar,panjang):
    '''Luas persegi '''
    return lebar*panjang

def kel(lebar,panjang):
    '''Kel Persegi'''
    return 2*(panjang*lebar)

def display(pesan,value):
    '''Display'''
    print(f"Hasil perhitungann {pesan} : {value}")

#PROGRAM UTAMA

while True:
    header()
    choice = input("""
    PILIH PERHITUNGAN : 
    1. Luas
    2. Keliling
    
    """)

    LEBAR,PANJANG = inputUser()
    LUAS = luas(LEBAR,PANJANG)
    KEL = kel(LEBAR,PANJANG)

    if choice == "1" :
        display("luas", LUAS)
    elif choice == "2":
        display("keliling", KEL)
    else:
        print("Harap memilih dengan benar")
   
    confirm = input("Ingin menambahkan User lain ? (y/n) ")

    if confirm == "n" :
        break

print(14*'='+'TERIMA KASIH'+'='*14)


