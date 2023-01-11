from django.db import models


class Creative_team(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='team', max_length=100)
    facebook = models.CharField(max_length=100)
    twitter = models.CharField(max_length=100)
    google = models.CharField(max_length=100)
    website = models.CharField(max_length=100)
    mdi_dribbble = models.CharField(max_length=100)


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=128)
    message = models.CharField(max_length=200)


class Contact_details(models.Model):
    location = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=128)
    email = models.EmailField(max_length=200)












