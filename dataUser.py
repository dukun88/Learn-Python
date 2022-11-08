listUser=[]
while True:
    print("Isi Data berikut :")
    nama = input("Nama lengkap\t : ")
    user = input("Username\t : ")

    dataUser = [nama,user]
    listUser.append(dataUser)

    print(30*'='+'\n')

    print("No.\t| Nama \t\t| Username")
    for index,user in enumerate(listUser):
        print(f"{index+1}\t| {user[0]} \t| {user[1]}")

    print('\n\n'+30*'=')

    confirm = input("Ingin menambahkan User lain ? (y/n) ")

    if confirm == "n" :
        break
print(10*'='+'TERIMA KASIH'+'='*10)



