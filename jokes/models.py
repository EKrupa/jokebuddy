from django.db import models

# Create your models here.
class Conversation(models.Model):
    user_message = models.CharField(max_length=200)
    bot_response = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.user_message} - {self.bot_response}'