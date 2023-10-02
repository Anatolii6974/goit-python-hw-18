from models import *
from mongoengine import *

connect(db="test", host='mongodb+srv://anatolii:maiden94@cluster0.wgxobak.mongodb.net/?retryWrites=true&w=majority')



if __name__ == '__main__':

    while True:
        action = input('Enter your command:\n').strip()
        if action == 'exit':
            break

        try:
            command, value = action.split(": ")
        except ValueError:
            print("Invalid input format. Please use 'command: value'.")
            continue
        
        if command == 'name':
            au = Author.objects(fullname = value).first()
            for qu in Quote.objects(author = au.id):
                print(qu.quote)

        elif command == 'tag':
            for qu in Quote.objects.all():
                for tg in qu.tags:
                    if tg == value:
                        print(qu.quote)

        elif command == 'tags':
            tgs = action.split(",")
            for qu in Quote.objects.all():
                for tg in qu.tags:
                    if tg in tgs:
                        print(qu.quote)
        
    