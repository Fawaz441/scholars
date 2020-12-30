from django.db import models
from django.contrib.auth.models import User
# from phonenumber_field.modelfields import PhoneNumberField


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    uploads = models.IntegerField(default=0,null=True,blank=True)
    phone_number = models.CharField(max_length=14)
    is_seller = models.BooleanField(default=False,null=True,blank=True)



