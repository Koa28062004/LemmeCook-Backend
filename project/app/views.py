from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *
from datetime import datetime, timedelta
 

def index(request):
    today = datetime.now().date()
    weekly_start_date = today - timedelta(days=today.weekday())
    monthly_start_date = today.replace(day=1)
    yearly_start_date = today.replace(month=1, day=1)

    # Count CustomerSupport objects for current date, weekly, and monthly
    current_date_customer_support_count = Customer.objects.filter(RegisteredDate__date=today).count()
    weekly_customer_support_count = Customer.objects.filter(RegisteredDate__date__gte=weekly_start_date).count()
    monthly_customer_support_count = Customer.objects.filter(RegisteredDate__date__gte=monthly_start_date).count()
    yearly_visited_customers_count = Customer.objects.filter(RegisteredDate__date__gte=yearly_start_date).count()
   
    context = {
        
        'current_date_customer_support_count': current_date_customer_support_count,
        'weekly_customer_support_count': weekly_customer_support_count,
        'monthly_customer_support_count': monthly_customer_support_count,
        'yearly_visited_customers_count': yearly_visited_customers_count,
        
    }
   
    return render(request, 'index.html',context)


class CustomerAndroid(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer