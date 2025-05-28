from django.db import models

# Create your models here.

# Data table models for student database

class Patient(models.Model):
    # a primary incremented key is created by Django
    surname = models.CharField(max_length=40)
    first_names = models.CharField(max_length=40)
    gender = models.CharField(max_length=6)
    date_of_birth = models.CharField(max_length=10, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    DisplayFields = ['id', 'surname', 'first_names']

    class Meta:
        db_table = 'Patient'