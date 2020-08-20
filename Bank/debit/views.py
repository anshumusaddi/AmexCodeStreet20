from django.shortcuts import render
from rest_framework import generics
from .serializers import TransSerializer
import datetime
from .models import Transactions

# Create your views here.
class TransView(generics.ListCreateAPIView):
    serializer_class = TransSerializer
    queryset = Transactions.objects.all()

    def perform_create(self, serializer):
        serializer.save()

class TransViewDate(generics.ListCreateAPIView):
    serializer_class = TransSerializer

    def get_queryset(self):
        dt = self.kwargs['datetime']
        dt = datetime.datetime(dt)
        return Transactions.objects.filter(dt__gt=dt)

    def perform_create(self, serializer):
        serializer.save()