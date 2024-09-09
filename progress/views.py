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