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
            fullName = data.get('fullName')

            print(username, email, password, fullName)

            # Check if the username already exists
            if Users.objects.filter(username=username).exists():
                return JsonResponse({"status": 'That username is taken'}, status=200)

            # Register the user
            profile = Profile.objects.create(fullName=fullName)
            user = Users.objects.create(username=username, password=password, email=email, profile_id=profile)
            return JsonResponse({"status": 'success', "userId": str(user.id)}, status=200)
        
        except json.JSONDecodeError:
            return JsonResponse({"status": "Invalid JSON"}, status=200)
        except Exception as e:
            print(e)  # Log the exception for debugging purposes
            return JsonResponse({"status": "Internal server error"}, status=200)
    
    return HttpResponse("Method not allowed", status=405)

@csrf_exempt
def check_email(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            email = data.get('email')

            if Users.objects.filter(email=email).exists():
                return JsonResponse({"status": 'Email already exists'}, status=200)
            else:
                return JsonResponse({"status": 'success'}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({"status": 'Invalid JSON'}, status=400)
    return JsonResponse({"status": 'Method not allowed'}, status=405)
    
@csrf_exempt
def login(request):
    if request.method == "POST":
        data = json.loads(request.body)
        email = data.get('email')
        password = data.get('password')

        user = Users.objects.filter(email=email, password=password)

        if user.exists():
            return JsonResponse(
                {"status": "success", "userId": str(user.id)},
                status=200
            )
        elif not Users.objects.filter(email=email).exists():
            return JsonResponse(
                {"status": "Wrong email"},
                status=200
            )
        elif Users.objects.filter(email=email).exists() and not Users.objects.filter(password=password).exists() :
            return JsonResponse(
                {"status": "Wrong Password"},
                status=200
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