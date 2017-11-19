from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
from Authentication.decorators import required_login
from Authentication.models import Phone
from Authentication import assist
from .models import Bill


