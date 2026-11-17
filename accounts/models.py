from django.db import models
from django.db.models.signals import post_save

from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
  
  ROLE_CHOICES = (
    ('student','student'),
    ('trainer','trainer')
  )
  
  phone = models.CharField(max_length=12,unique=True)
  
  role = models.CharField(max_length=100,choices=ROLE_CHOICES,default='student')
  
class StudentProfile(models.Model):
  
  student = models.OneToOneField(User,on_delete=models.CASCADE,related_name="student")
  
  course = models.CharField(max_length=100,null=True)
  
  qualification = models.CharField(max_length=100,null=True)
  
  profile_picture = models.ImageField(upload_to="cover_pics",null=True)
  
  passout_year = models.CharField(max_length=100,null=True)
  
  skills = models.CharField(max_length=200,null=True)  
  
  created_at = models.DateTimeField(auto_now_add=True)
  
  updated_at = models.DateTimeField(auto_now=True)
  
class TrainerProfile(models.Model):
  
  trainer = models.OneToOneField(User,on_delete=models.CASCADE,related_name="trainer")
    
  qualification = models.CharField(max_length=100,null=True)
  
  profile_picture = models.ImageField(upload_to="cover_pics",null=True)
  
  experience = models.CharField(max_length=100,null=True)
  
  specialization = models.CharField(max_length=200,null=True)
  
  skills = models.CharField(max_length=200,null=True)  
  
  created_at = models.DateTimeField(auto_now_add=True)
  
  updated_at = models.DateTimeField(auto_now=True)
  
def create_student_profile(sender,instance,created,*args,**kwargs):
  
  if created and instance.role=="student":
    
    StudentProfile.objects.create(student=instance)
    
post_save.connect(create_student_profile,sender=User)

def create_trainer_profile(sender,instance,created,*args,**kwargs):
  
  if created and instance.role=="trainer":
    
    TrainerProfile.objects.create(trainer=instance)
    
post_save.connect(create_trainer_profile,sender=User)


  