from django.db import models

class Subscriptores(models.Model): 
    mail = models.CharField(max_length=50)
