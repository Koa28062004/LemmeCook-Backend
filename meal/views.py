from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
import json
from .models import *

@csrf_exempt
def get_allergies(request):
    if request.method == 'GET':
        allergies = Allergies.objects.all()
        return JsonResponse(
            {"allergies": list(allergies.values())},
            status=200
        )

@csrf_exempt
def get_diets(request):
    if request.method == 'GET':
        diets = Diets.objects.all()
        return JsonResponse(
            {"diets": list(diets.values())},
            status=200
       )
    

@csrf_exempt
def add_user_allergies(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            user_id = data.get("userId")
            allergies = data.get("allergies", [])

            # Debugging log
            print(f"Received userId: {user_id}")
            print(f"Received allergies: {allergies}")

            user = Users.objects.get(id=user_id)

            for allergy_name in allergies:
                allergy = Allergies.objects.get(allergy=allergy_name)
                User_Allergy.objects.create(user_id=user, allergy_id=allergy)
            
            return JsonResponse({"status": "success"}, status=201)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

@csrf_exempt
def add_user_diets(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            user_id = data.get("userId")
            diets = data.get("diets", [])

            # Debugging log
            print(f"Received userId: {user_id}")
            print(f"Received diets: {diets}")

            user = Users.objects.get(id=user_id)

            for diet_name in diets:
                diet = Diets.objects.get(diet=diet_name)
                User_Diet.objects.create(user_id=user, diet_id=diet)
            
            return JsonResponse({"status": "success"}, status=201)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)