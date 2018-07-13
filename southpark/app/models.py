from django.db import models

# Character model
class Character(models.Model):
    GENDERS = (
        ('F', 'Female'),
        ('M', 'Male'),
    )
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDERS)
    occupation = models.CharField(max_length=30)
    image = models.ImageField(upload_to='images/', default='images/none/no-img.jpg')

# Serie model
#class Serie(models.Model):
