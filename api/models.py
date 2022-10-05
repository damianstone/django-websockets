from django.db import models

# Create your models here.


class ChatModel(models.Model):
    room_number = models.CharField(max_length=127)
    message = models.TextField()
