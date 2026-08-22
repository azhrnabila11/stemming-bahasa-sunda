from django.db import models

class KamusSunda(models.Model):
    kata_dasar = models.CharField(max_length=100)
    arti = models.CharField(max_length=100) 

    def __str__(self):
        return self.kata_dasar
    
class KamusStopword(models.Model):
    kata_stopword = models.CharField(max_length=100)
    arti = models.CharField(max_length=100)

    def __str__(self):
        return self.kata_stopword

class StemmingResult(models.Model):
    tokens = models.CharField(max_length=100)
    stem = models.CharField(max_length=100)
    frek = models.IntegerField(default=1)
    is_correct = models.BooleanField(default=False)
    status_manual = models.CharField(max_length=50, default="Otomatis")