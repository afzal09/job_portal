from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
# Create your models here.
class user(User):
    acc_email = models.EmailField(unique=True,default="user@mail.com")
    image = models.CharField(max_length=100,null=True)
    designation = models.CharField(max_length=100,null=True)
    mobile = models.IntegerField(null=True)
    def set_password(self, raw_password):
        password = make_password(raw_password)
        return password