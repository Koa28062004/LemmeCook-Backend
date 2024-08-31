from django.contrib import admin
from meal.models import *

admin.site.register(Meal)
admin.site.register(User_Meal)
admin.site.register(Schedule)
admin.site.register(Schedule_Meal)
admin.site.register(Allergies)
admin.site.register(User_Allergy)
admin.site.register(Diets)
admin.site.register(User_Diet)