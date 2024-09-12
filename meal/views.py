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
        
@csrf_exempt
def favorites_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_id = data.get('user_id')
            meal_id = data.get('meal_id')

            # Create a new User_Meal entry
            user_meal, created = User_Meal.objects.get_or_create(user_id=user_id, meal_id=meal_id)

            message = 'Favorite meal added successfully' if created else 'Favorite meal already exists'
            return JsonResponse({'status': 'success', 'message': message}, status=200)

        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

    elif request.method == 'GET':
        try:
            # Extract the user_id from query parameters
            user_id = request.GET.get('user_id')

            if not user_id:
                return JsonResponse({'status': 'error', 'message': 'user_id is required'}, status=400)

            # Retrieve all favorite meals for the given user
            user_meals = User_Meal.objects.filter(user_id=user_id)
            meal_list = [um.meal_id.id for um in user_meals]

            return JsonResponse({'status': 'success', 'favorites': meal_list}, status=200)

        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)
    
@csrf_exempt
def delete_favorite(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_id = data.get('userId')
            meal_id = data.get('meal_id')

            # Check if the User_Meal entry exists
            user_meal = User_Meal.objects.filter(user_id=user_id, meal_id=meal_id)

            if user_meal.exists():
                user_meal.delete()
                return JsonResponse({'status': 'success', 'message': 'Favorite meal removed successfully'}, status=200)
            else:
                return JsonResponse({'status': 'error', 'message': 'Favorite meal does not exist'}, status=404)

        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)