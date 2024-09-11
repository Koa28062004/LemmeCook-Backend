import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from blog.models import Blog
from meal.models import Meal

@csrf_exempt
def blog_view(request):
  if request.method == 'GET':
    blogs = Blog.objects.all().values('id', 'title', 'body', 'image_link', 'meal_id')
    return JsonResponse({'status': 'success', 'blogs': list(blogs)}, status = 200)
  
  elif request.method == 'POST':
    try:
      data = json.loads(request.body)
      title = data.get('title')
      body = data.get('body')
      image_link = data.get('image_link', '')
      meal_id = data.get('meal_id')
      
      if not all([title, body, meal_id]):
        return JsonResponse({'status': 'error', 'message': 'Title, body and Meal ID are required.'}, status = 400)
      
      meal = get_object_or_404(Meal, id=meal_id)
      blog = Blog.objects.create(title = title, body = body, image_link = image_link, meal_id = meal)
      
      return JsonResponse({'status': 'success', 'message': 'Blog ${blog.title} created successfully'}, status = 200)
    
    except json.JSONDecodeError:
      return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status = 400)
    except Exception as e:
      return JsonResponse({'status': 'error', 'message': str(e)}, status = 500)
      