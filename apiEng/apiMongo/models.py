from django.db import models
from mongoengine import Document,fields

class Game(Document):
    name = fields.StringField(required=True)
    nameSteam = fields.StringField(required=False)
    price = fields.FloatField(required=True)
    priceSteam = fields.FloatField(required=False)
    link = fields.StringField(required=True)
    linkSteam = fields.StringField(required=False)
    img = fields.StringField(required=True)
    imgSteam = fields.StringField(required=False)



# Create your models here.
# cria as tabelas
# cria modelos de dados