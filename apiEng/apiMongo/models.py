from django.db import models
from mongoengine import Document,fields

class Game(Document):
    name = fields.StringField(required=True)
    price = fields.StringField(required=True)
    link = fields.StringField(required=True)



# Create your models here.
# cria as tabelas
# cria modelos de dados