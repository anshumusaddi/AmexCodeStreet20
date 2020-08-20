from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Transactions(models.Model):
    user = models.ForeignKey(User,related_name='profile',on_delete=models.CASCADE)
    dt = models.DateTimeField(auto_now=True,name="Time")
    ammount = models.BigIntegerField(name="Ammount")
    trans_id = models.CharField(max_length=256,name="Trans_ID")
    trans_type = models.CharField(max_length=2,choices=[('CR','Credit'),('DR','Debit')],name="Transaction")

# class Last_Update(models.Model):
#     user = models.OneToOneField(User,related_name='profile_lst',on_delete=models.CASCADE)
#     dt = models.DateTimeField(name="Time")
