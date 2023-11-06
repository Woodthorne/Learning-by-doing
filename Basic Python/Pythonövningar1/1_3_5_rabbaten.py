price = float(input('Ange ursprungspriset på varan: '))
discount = int(input('Ange varans rabbat(%): '))
print(f'Rabatten på varan blir {round(price * discount / 100, 2)} kronor')