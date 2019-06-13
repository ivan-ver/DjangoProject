from django.db import models

class Messages(models.Model):
    textMessage = models.CharField(max_length=200)

    def __str__(self):
        return self.textMessage


