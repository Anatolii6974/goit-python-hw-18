from mongoengine import *

connect(db="test", host='mongodb+srv://anatolii:maiden94@cluster0.wgxobak.mongodb.net/?retryWrites=true&w=majority')

class Task(Document):
    fullname = StringField(max_length=80, required=True)
    email = StringField(max_length=80, required=True)
    completed = BooleanField(default=False)
    meta = {"collection": 'tasks'}

