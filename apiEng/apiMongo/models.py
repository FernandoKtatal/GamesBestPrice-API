from django.db import models
from mongoengine import Document,fields

class Game(Document):
    official = fields.StringField(required=False)
    name = fields.StringField(required=False)

    priceNu = fields.FloatField(required=False)
    priceSteam = fields.FloatField(required=False)
    priceG2a = fields.FloatField(required=False)

    linkNu = fields.StringField(required=False)
    linkSteam = fields.StringField(required=False)
    linkG2a = fields.StringField(required=False)
    
    img = fields.StringField(required=False)


# Create your models here.
# cria as tabelas
# cria modelos de dados