import random

student = {'daalD1993':'A'}
# random.choice(['A','B','C','E','F'])

name = input('Ange elevens för och efternamn: ').lower().split(' ')
date_of_birth = input('Ange elevens födelseår: ')
if not date_of_birth.isnumeric():
    print('Födelseår måste vara positivt heltal.')
    quit()
student_key = input('Ange elevennyckel: ').capitalize()
if student_key not in ['A','D','E','I','L','O','P']:
    print('Ogilltig elevnyckel.')
    quit()
print(name)
student_id = name[0][0:2] + name[1][0:2] + student_key + date_of_birth
print(student[student_id])