from django.db import models

type=[('clothing','clothing'),('footwear','footwear'),('electronics','electroincs'),('home','home')]

class Products(models.Model):
    pid=models.AutoField(primary_key=True)
    datetime=models.DateTimeField(auto_now_add=True)
    pname=models.CharField(max_length=50)
    price=models.IntegerField()
    desc=models.TextField()
    ptype=models.CharField(max_length=50,choices=type)