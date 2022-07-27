choice = input('''
Silakan pilih jenis operasi yang ingin Anda lakukan:
+ untuk penambahan
- untuk pengurangan
* untuk perkalian
/ untuk pembagian
''')

num_1 = int(input('Masukkan angka pertama: '))
num_2 = int(input('Masukkan angka kedua: '))

if choice == '+':
    print('{} + {} = '.format(num_1, num_2))
    print(num_1 + num_2)

elif choice == '-':
    print('{} - {} = '.format(num_1, num_2))
    print(num_1 - num_2)

elif choice == '*':
    print('{} * {} = '.format(num_1, num_2))
    print(num_1 * num_2)

elif choice == '/':
    print('{} / {} = '.format(num_1, num_2))
    print(num_1 / num_2)

else:
    print('Masukkan operator yang valid, jalankan kembali programnya.')
