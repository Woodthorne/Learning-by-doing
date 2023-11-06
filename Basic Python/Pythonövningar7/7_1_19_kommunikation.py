import os, random

if not os.path.exists('message.txt'):
    with open('message.txt','x'):
        pass

def main():
    user_id = str(random.randint(1000,9999))
    print(f'Ditt ID är {user_id}')
    read_id = input('Mata in ID för den andra parten: ')
    while True:
        opt = input('Tryck RETUR för att läsa in meddelande: ')
        if opt == 'q':
            quit()
        if os.path.getsize('message.txt') > 0:
            with open('message.txt','r+',encoding='utf-8') as f:
                message = f.readlines()
                
                if read_id + user_id in message[0]:
                    pass
                elif user_id + read_id in message[0]:
                    print('Ditt meddelande har inte lästs ännu.')
                    continue
                else:
                    print('Felaktig ID')
                    quit()
            with open('message.txt','w',encoding='utf-8') as f:
                pass
            for line in message:
                print(line.strip('\n'))
        with open('message.txt','w',encoding='utf-8') as f:
            message = input('Mata in ditt meddelande: ') + '\n'
            f.write(user_id + read_id + '\n')
            f.write(message)

    




if __name__ == '__main__':
    main()