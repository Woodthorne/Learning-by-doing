import pymongo

class Player:
    namn: str = ''
    jersey: int = 0

    @classmethod
    def create(cls, in_dict: dict):
        a = cls()
        a.__dict__ = in_dict
        return a


myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['mydatabase']

playersCollection = mydb['players']

while True:
    menu = ['====Spelardatabasen====',
            '1. Skapa spelare',
            '2. Visa alla spelare',
            '3. Tröjsökning',
            '4. Textsökning',
            '0. Avsluta']
    for option in menu:
        print(option)
    opt = input('>>> ')
    if opt == '0':
        break
    elif opt == '1':
        p = Player()
        p.namn = input('Namn: ')
        p.jersey = input('Tröja: ')
        new = playersCollection.insert_one(p.__dict__)
        print(f'Nya spelare fick id: {new.inserted_id}')
    elif opt == '2':
        for x in playersCollection.find():
            player = Player.create(x)
            print(f'{player.namn} {player.jersey}')
    elif opt == '3':
        num = int(input('Ange tröjnummer: '))
        query = {'jersey': num}
        for x in playersCollection.find(query):
            player = Player.create(x)
            print(f'{player.namn} {player.jersey}')
    elif opt =='4':
        words = input('Ange text: ')
        query = {'namn': {'$regex': words + '.*', '$options' :'i'}}
        for x in Player.create(x):
            print(f'{player.namn} {player.jersey}')