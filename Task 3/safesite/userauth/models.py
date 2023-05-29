from django.db import models

# Create your models here.
from bcrypt import hashpw, gensalt

class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)

    def set_password(self, raw_password):
        self.password = hashpw(raw_password.encode('utf-8'), gensalt()).decode('utf-8')
