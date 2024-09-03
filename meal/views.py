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
def get_dieats(request):
    if request.method == 'GET':
        diets = Diets.objects.all()
        return JsonResponse(
            {"diets": list(diets.values())},
            status=200
       )