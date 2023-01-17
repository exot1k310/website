from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    pass
    YEAR_IN_SCHOOL_CHOICES = [
        ('7', '7 класс'),
        ('8', '8 класс'),
        ('9', '9 класс'),
        ('10', '10 класс'),
        ('11', '11 класс'),
    ]
    grade = models.CharField(
        max_length=2,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default='7',
    )

    def __str__(self):
        return self.username


class Kabinet(models.Model):
    SUBJECT = [
        ('math', 'Математика'),
        ('phys', 'Физика'),
        ('russ', 'Русский язык'),
        ('it', 'Информатика'),
    ]
    subjects = models.CharField(
        max_length=4,
        choices=SUBJECT,
        default='math',
    )
    number = models.IntegerField()
    ave_rating = models.FloatField()

    def __str__(self):
        return str(self.number)



class Ratings(models.Model):
    rating = models.IntegerField()
    user = models.ForeignKey('Users', on_delete=models.CASCADE)
    kabinet = models.ForeignKey('Kabinet', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.kabinet) + "_" + str(self.rating)


class Comments(models.Model):
    coment = models.TextField()
    user = models.ForeignKey('Users', on_delete=models.CASCADE)
    kabinet = models.ForeignKey('Kabinet', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.kabinet) + "_" + str(self.coment[0:10])
