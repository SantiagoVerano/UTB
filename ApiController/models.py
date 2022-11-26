from mongoengine import Document,StringField,IntField

class peopledatabase(Document):
    cedula=StringField()
    nombres=StringField()
    apellidos=StringField()
    edad=IntField()