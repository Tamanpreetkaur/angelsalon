from django.db import models


class Service(models.Model):
    name=models.CharField(max_length=50)
    img=models.ImageField(upload_to='images')
    def __str__(self):
        return self.name
class Product(models.Model):
    img=models.ImageField(upload_to='images')
class Contacts(models.Model):
    msg_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50,default="")
    phone=models.CharField(max_length=50,default="")
    desc=models.CharField(max_length=50,default="")
    def __str__(self):
        return self.name


