from django.db import models
from datetime import datetime

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=1000)
    post_time = models.DateTimeField(default= datetime.now, blank= True)

# add user model with various users having different posts    
    