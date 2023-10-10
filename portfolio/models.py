from django.db import models

from apps.accounts.models import Account


class Resume(models.Model):
    class ProfessionLevel(models.TextChoices):
        IINTERNSHIP = 'internship'
        JUNIOR = 'junior'
        MIDDLE = 'middle'
        SENIOR = 'senior'

    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='resume')
    full_name = models.CharField(max_length=50)
    profession = models.CharField(max_length=50)
    level = models.CharField(max_length=10, choices=ProfessionLevel.choices)
    description = models.CharField(max_length=140)

    def __str__(self):
        return self.profession


class Skills(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Education(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    start_time = models.DateField()
    finished_time = models.DateField()

    def __str__(self):
        return self.name


class Certificate(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='certificates/')

    def __str__(self):
        return self.name
