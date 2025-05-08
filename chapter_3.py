
# Chapter 3: Django Fundamentals Refresher

# Example of a Django view and model usage
from django.http import HttpResponse
from .models import User

def hello_world(request):
    users = User.objects.all()
    return HttpResponse(f"Hello World! We have {users.count()} users.")
    