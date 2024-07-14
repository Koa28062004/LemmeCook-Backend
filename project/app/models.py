from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

#chagua aina ya kikao kazi
TYPE_CHOICES = [
        ('Monthly', 'Monthly'),
        ('Weekly', 'Weekly'),
        ('Annually', 'Annually'),
        ('Daily', 'Daily'),
        ('Other', 'Other'),
]
#add wadhifa 
class Domain(models.Model):
 DomainName = models.CharField(max_length=255,primary_key=True)
 RegisteredDate = models.DateTimeField(auto_now_add=True)
 class Meta:
  verbose_name = "Employee Role"
  verbose_name_plural = "Employee Role"
 def __str__(self):
        return self.DomainName
 
class EmployeeRole(models.Model):
 RoleName = models.CharField(max_length=30,primary_key=True)
 RegisteredDate = models.DateTimeField(auto_now_add=True)
 class Meta:
  verbose_name = "Employee Department"
  verbose_name_plural = "Employee Department"
 def __str__(self):
        return self.RoleName
 

#Affliction kwa wanachama
class AfflictionType(models.Model):
 AfflictionType = models.CharField(max_length=255,primary_key=True)
 RegisteredDate = models.DateTimeField(auto_now_add=True)
 LastUpdated = models.DateTimeField(auto_now=True)
 class Meta:
  verbose_name = "AfflictionType"
  verbose_name_plural = "AfflictionType"
 def __str__(self):
        return self.AfflictionType



#Location/Department/Unit anayotokea mteja
class Unit(models.Model):
 UnitName = models.CharField(max_length=255,primary_key=True)
 RegisteredDate = models.DateTimeField(auto_now_add=True)
 class Meta:
  verbose_name = "Customer Location"
  verbose_name_plural = "Customer Location"
 def __str__(self):
        return self.UnitName
    


#namba za simu 
class PhoneBook(models.Model):
    Position=models.CharField(max_length=250)
    Phone1=models.CharField(max_length=12,null=True)
    Phone2=models.CharField(max_length=12,null=True)
    Station=models.ForeignKey(Domain, on_delete=models.CASCADE, null=True)
    RegisteredDate = models.DateTimeField(auto_now_add=True)
    LastUpdated = models.DateTimeField(auto_now=True)
    class Meta:
     verbose_name = "PhoneBook"
     verbose_name_plural = "PhoneBook"
    def __str__(self):
        return self.Position


 
    
class Customer(models.Model):
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    PhoneNumber = models.CharField(max_length=15)
    Email = models.CharField(max_length=150)
    AddressedTo = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    RegisteredDate = models.DateTimeField(auto_now_add=True,null=True)
    LastUpdated = models.DateTimeField(auto_now=True,null=True)
    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("In Progress", "In Progress"),
        ("Resolved", "Resolved"),
    ]
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default="Pending",null=True)
    class Meta:
     verbose_name = "Android Customer Care"
     verbose_name_plural = "Android Customer Care"
    def __str__(self):
        return self.LastName
  
#Pole mbalimbali /record wanachama waliopewa pole
class Affliction(models.Model):
    Firstname= models.CharField(max_length=50)
    Middlename= models.CharField(max_length=50)
    Fullname= models.CharField(max_length=50)
    Incident =models.ForeignKey(AfflictionType, on_delete=models.CASCADE)
    Amount= models.CharField(max_length=7)
    RegisteredDate = models.DateTimeField(auto_now_add=True)
    Date = models.DateField(auto_now_add=False)
    Report=models.FileField(upload_to='Affliction/',null=True)
    class Meta:
     verbose_name = "Affliction"
     verbose_name_plural = "Affliction"

#Vikao kazi
class WorkMeeting(models.Model):
    DateTime = models.DateTimeField(auto_now_add=False)
    ChairMan=models.ForeignKey(User, on_delete=models.CASCADE)
    Type = models.CharField(max_length=250, choices=TYPE_CHOICES)
    Report=models.FileField(upload_to='Meatings/')
    RegisteredDate = models.DateTimeField(auto_now_add=True)
    LastUpdated = models.DateTimeField(auto_now=True)
    class Meta:
     verbose_name = "Work Meeting"
     verbose_name_plural = "Work Meeting"

class Type(models.Model):
    MeetType = models.CharField(max_length=250,primary_key=True)
    RegisteredDate = models.DateTimeField(auto_now_add=True)
    class Meta:
     verbose_name = "Meeting Type"
     verbose_name_plural = "Meeting Type"
    def __str__(self):
        return self.MeetType

class Mahudhurio(models.Model):
    CheckNumber = models.CharField(max_length=250)
    MeetingDate = models.DateField(auto_now_add=False)
    Firstname = models.CharField(max_length=250)
    MiddleName = models.CharField(max_length=250)
    MeetingType=models.ForeignKey(Type, on_delete=models.CASCADE)
    LastName = models.CharField(max_length=250)
    Unit =models.ForeignKey(Unit,on_delete=models.CASCADE)
    PhoneNumber = models.CharField(max_length=250)
    RegisteredDate = models.DateTimeField(auto_now_add=True)
    LastUpdated = models.DateTimeField(auto_now=True)
    class Meta:
     verbose_name = "Members Meeting"
     verbose_name_plural = "Members Meeting"
   

    def __str__(self):
        return self.Firstname