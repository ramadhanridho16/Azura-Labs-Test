'''
Urutkan array di atas dengan prioritas sebagai berikut
harga terendah
jika harga sama maka urutkan berdasarkan rating tertinggi
jika rating sama maka urutkan berdasarkan likes terbanyak. 
Pastikan program yang anda buat dapat menghandle sekitar ratusan data.
'''

# Variabel = ["harga", "rating", "likes"]
Indomie = [3000, 5, 150]
Laptop = [4000000, 4.5, 123]
Aqua = [3000, 4, 250]
Smart_TV = [4000000, 4.5, 42]
Headphone = [4000000, 3.5, 90]
Very_Smart_TV = [4000000, 3.5, 87]

# Using sort function
arr = [Indomie, Laptop, Aqua, Smart_TV, Headphone, Very_Smart_TV]
arr.sort()
print(arr)
