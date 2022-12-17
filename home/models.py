from distutils.command.upload import upload
from time import time
from unicodedata import name
from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from datetime import datetime
import uuid

User = get_user_model()

# Create your models here.

class Register(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio = models.TextField(blank= True)
    profile_pic = models.ImageField(upload_to = 'profile_pic', default="tom-morbey-Ke_bXG4dc2w-unsplash.jpg")
    location = models.CharField(max_length=100, blank= True)
#   to make the name in database visible
    def __str__(self):
        return f'User name : {self.user.username}.  User Id : {self.id_user} Location : {self.location}'

class Getdatetime(models.Model):
      date = models.CharField(null=True,blank=False,max_length=50)
      time = models.CharField(null=True,blank=False,max_length=50)


      def __str__(self):
           return f'{self.date} Booking time {self.time}'




class Bookings(models.Model):
     
    #   user = models.ForeignKey(User , on_delete=models.CASCADE)
    #   court =models.ForeignKey(Court, on_delete=models.CASCADE)
      user = models.CharField(null=True,blank=False,max_length=20) 
      user_id = models.IntegerField(null=True,blank=False) 
      booking_date = models.CharField(null=True,blank=False,max_length=50)               
      bookingtime_start=  models.TimeField(null=True,blank=False,max_length=50)
      bookingtime_finish=  models.TimeField(null=True,blank=False,max_length=50)
      booking_duration = models.IntegerField(null=True,blank=False)
      unique_booking_id = models.CharField(null=True,blank=False,max_length=50)
          
      def __str__(self) -> str:
           return f'Date  ||  {self.booking_date}   ||  {self.user} with user ID {self.user_id} has booked the pitch from {self.bookingtime_start} to {self.bookingtime_finish} for {self.booking_duration} minutes with booking id {self.unique_booking_id}'



class Payment(models.Model):
      
      user = models.CharField(null=True,blank=False,max_length=20) 
      user_id = models.IntegerField(null=True,blank=False) 
      price = models.IntegerField(null=True,blank= False)
      booking_duration = models.IntegerField(null=True,blank= False)
      product_id = models.CharField(null=True,blank=False,max_length=50)
      def __str__(self) -> str :
        return f'{self.user} with userId {self.user_id} needs to pay Rs. {self.price} .'