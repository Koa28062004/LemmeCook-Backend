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
      
      goal = Goal.objects.get(user_id = user_id)
      
      if calories is not None:
        goal.calories = calories
      if fat is not None:
        goal.fat = fat
      if protein is not None:
        goal.protein = protein
      if carb is not None:
        goal.carb = carb
        
      goal.save()
      
      return JsonResponse({'status': 'success', 'message': 'Goal updated successfully'}, status = 200)
    
    except Goal.DoesNotExist:
      return JsonResponse({'status': 'error', 'message': 'Goal not found'}, status = 404)
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

      # Retrieve or create the user's progress for the given date
      progress, created = TodayProgress.objects.get_or_create(user_id=user_id, date=date)

      # Update the progress fields
      if calories is not None:
          progress.calories = calories
      if fat is not None:
          progress.fat = fat
      if protein is not None:
          progress.protein = protein
      if carb is not None:
          progress.carb = carb

      # Save the updated progress
      progress.save()

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

      # Retrieve the user's progress for the given date
      progress = TodayProgress.objects.get(user_id=user_id, date=date)

      # Return the progress as a JSON response
      progress_data = {
          'user_id': progress.user_id.id,
          'date': progress.date,
          'calories': progress.calories,
          'fat': progress.fat,
          'protein': progress.protein,
          'carb': progress.carb
      }

      return JsonResponse({'status': 'success', 'progress': progress_data}, status=200)

    except TodayProgress.DoesNotExist:
      return JsonResponse({'status': 'error', 'message': 'Progress not found'}, status=404)
    except Exception as e:
      return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

  else:
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)
