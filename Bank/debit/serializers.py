# from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Transactions

class TransSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = ('dt','ammount','trans_id','trans_type')