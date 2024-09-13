from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=200)
    disease = models.CharField(max_length=200)
    age = models.IntegerField()

    def __str__(self):
        return f'[id={self.id}, name={self.name}, disease={self.disease}, age={self.age}]'