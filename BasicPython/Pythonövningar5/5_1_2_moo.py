my_dict = {'ko':'mu',
           'katt':'mjau',
           'hund':'voff'}

animal = input('Välj ett djur: ').lower()
if animal in my_dict.keys():
    print(f'En {animal} säger {my_dict[animal]}')
else:
    print(f'Ursäkt, jag känner inte till det djuer! {animal.capitalize()} måste komma från en annan planet!')