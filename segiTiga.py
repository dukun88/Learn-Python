sisi = int(input('Segitiga berapa sisi :'))

print(10*'='+'SEGITIGA SATUSISI'+10*'=')

count = 1
for  i in range(sisi):
    print("*"*count)
    count += 1

print(10*'='+'SEGITIGA SAMA SISI'+10*'=')

count = 1
space = int(sisi/2)

while True:
    if (count%2):
        print(" "*space,"+"*count)
        space -= 1
        count += 1
    else:
        count += 1
        continue

    if count > sisi:
        break

print('\n*Segitiga sama sisi akan dibagi dua sisinya\n\n')

print(10*'='+'LAYANG-LAYANG'+10*'=')

count = 1
space = int(sisi/2)

while True:
    if (count%2):
        print(" "*space,"+"*count)
        space -= 1
        count += 1
    else:
        count += 1
        continue

    if count > sisi:
        break
while True:
    if (count%2):
        space += 1
        print(" "*space,"+"*count)
        count -= 1
    else:
        count -= 1
        continue

    if count == 0:
        break