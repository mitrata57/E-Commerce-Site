from django.shortcuts import render

from django.contrib.auth.models import User
from django.http import JsonResponse
import json

def register(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user = User.objects.create_user(
            username=data['username'],
            password=data['password']
        )
        return JsonResponse({"message": "User created"})


from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user = authenticate(
            username=data['username'],
            password=data['password']
        )
        if user:
            login(request, user)
            return JsonResponse({"message": "Logged in"})
        return JsonResponse({"error": "Invalid credentials"})