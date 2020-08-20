"""Bank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from debit.views import TransView,TransViewDate

urlpatterns = [
    path('admin/', admin.site.urls,name="Admin"),
    path('trans/',TransView.as_view(),name="Transactions"),
    path(r'^transdate/(?P<datetime>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z)/$',TransViewDate.as_view(),name="TransactionsDate"),
    path("o/", include('oauth2_provider.urls', namespace='oauth2_provider')),
]
