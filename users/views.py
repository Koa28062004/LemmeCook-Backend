from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
import json
from .models import Users, Profile
from django.contrib import messages, auth
from django.contrib.auth.hashers import make_password

@csrf_exempt
def register(request):
    if request.method == 'POST':
        try:
            # Get form values
            data = json.loads(request.body)
            username = data.get('username')
            email = data.get('email')
            password = data.get('password')

            print(username, email, password)

            # Check if the username already exists
            if Users.objects.filter(username=username).exists():
                return JsonResponse({"status": 'That username is taken'}, status=400)

            # Check if the email already exists
            elif Users.objects.filter(email=email).exists():
                return JsonResponse({"status": 'That email is being used'}, status=400)

            # Register the user
            user = Users.objects.create(username=username, password=password, email=email)
            return JsonResponse({"status": 'success'}, status=201)
        
        except json.JSONDecodeError:
            return JsonResponse({"status": "Invalid JSON"}, status=400)
        except Exception as e:
            print(e)  # Log the exception for debugging purposes
            return JsonResponse({"status": "Internal server error"}, status=500)
    
    return HttpResponse("Method not allowed", status=405)
    
@csrf_exempt
def login(request):
    if request.method == "POST":
        data = json.loads(request.body)
        email = data.get('email')
        password = data.get('password')

        if Users.objects.filter(email=email, password=password).exists():
                return JsonResponse(
                {"status": "success"},
                status=200
            )
        else:
            return JsonResponse(
                {"status": "Invalid credentials"},
                status=403
            )
        
    else: return HttpResponse("Login")

@csrf_exempt
def get_user(request):
    if request.method == "GET":
        users = Users.objects.all()
        return JsonResponse(
            {"users": list(users.values())},
            status=200
        )
    else:
        return HttpResponse("Get User")

@csrf_exempt
def forgetPassword(request):
    if request.method == "POST":
        data = json.loads(request.body)
        email = data.get('email')
        newPassword = data.get('newPassword')
        if Users.objects.filter(email=email).exists():
            user = Users.objects.get(email=email)
            user.password = newPassword
            user.save()
            return JsonResponse(
                {"status": "success"},
                status=200
            )
        else:
            return JsonResponse(
                {"status": "Invalid email"},
                status=403
            )
    else:
        return HttpResponse("Forget Password")