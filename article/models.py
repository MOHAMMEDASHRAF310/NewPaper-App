from operator import truediv
from tkinter import CASCADE
from turtle import title
from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.conf import settings



# Create your models here.
class article(models.Model):
    title=models.CharField(max_length=200)
    body=models.TextField()
    auther=models.ForeignKey(get_user_model(),on_delete=models.CASCADE,)
    date=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('article-detial',args=[str(self.id)])