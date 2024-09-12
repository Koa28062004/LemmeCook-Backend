from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
import json
from .models import *

@csrf_exempt
def goal_view(request):
  if request.method == 'POST':
    try:
      data = json.loads(request.body)
      user_id = data.get('user_id')
      calories = data.get('calories')
      fat = data.get('fat')
      protein = data.get('protein')
      carb = data.get('carb')
      
      # Use update_or_create to either update or create a Goal object
      goal, created = Goal.objects.update_or_create(
        user_id=user_id,  # This is the condition to find the goal
        defaults={
          'calories': calories,
          'fat': fat,
          'protein': protein,
          'carb': carb,
        }
      )

      message = 'Goal created successfully' if created else 'Goal updated successfully'
      return JsonResponse({'status': 'success', 'message': message}, status=200)
    
    except json.JSONDecodeError:
      return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status = 400)
    except Exception as e:
      return JsonResponse({'status': 'error', 'message': str(e)}, status = 500)
    
  elif request.method == 'GET':
    try:
      user_id = request.GET.get('user_id')
      
      if not user_id:
        return JsonResponse({'status': 'error', 'message': 'user_id is required'}, status = 400)
      
      goal = Goal.objects.get(user_id = user_id)
      
      goal_data = {
        'user_id': goal.user_id.id,
        'calories': goal.calories,
        'fat': goal.fat,
        'protein': goal.protein,
        'carb': goal.carb
      }
      
      return JsonResponse({'status': 'success', 'goal': goal_data}, status = 200)
    
    except Goal.DoesNotExist:
      return JsonResponse({'status': 'error', 'message': 'Goal not found'}, status=404)
    except Exception as e:
      return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
  
  else:
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status = 405)

@csrf_exempt
def progress_view(request):
	if request.method == 'POST':
		try:
			data = json.loads(request.body)
			user_id = data.get('user_id')
			date = data.get('date')
			calories = data.get('calories')
			fat = data.get('fat')
			protein = data.get('protein')
			carb = data.get('carb')

			# Update or create the user's progress for the given date
			progress, created = TodayProgress.objects.update_or_create(
        user_id=user_id, 
        date=date,
        defaults={
          'calories': calories,
          'fat': fat,
          'protein': protein,
          'carb': carb
        }
      )

			message = 'Progress created successfully' if created else 'Progress updated successfully'
			return JsonResponse({'status': 'success', 'message': message}, status=200)

		except json.JSONDecodeError:
			return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)
		except Exception as e:
			return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

	elif request.method == 'GET':
		try:
			# Extract the user_id and date from query parameters
			user_id = request.GET.get('user_id')
			date = request.GET.get('date')

			if not user_id or not date:
				return JsonResponse({'status': 'error', 'message': 'user_id and date are required'}, status=400)

			# Check if the user exists
			if not Users.objects.filter(id=user_id).exists():
				return JsonResponse({'status': 'error', 'message': 'User not found'}, status=404)

			# Retrieve the user's progress for the given date
			try:
				progress = TodayProgress.objects.get(user_id=user_id, date=date)
				progress_data = {
						'user_id': progress.user_id.id,
						'date': progress.date,
						'calories': progress.calories,
						'fat': progress.fat,
						'protein': progress.protein,
						'carb': progress.carb
				}
			except TodayProgress.DoesNotExist:
				# If no progress entry found, return an object with all zeroes
				progress_data = {
						'user_id': user_id,
						'date': date,
						'calories': 0,
						'fat': 0,
						'protein': 0,
						'carb': 0
				}

			return JsonResponse({'status': 'success', 'progress': progress_data}, status=200)

		except Exception as e:
			return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

	else:
		return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)
