from django.db import models

class Malumot(models.Model):
    sarlovha = models.CharField(max_length=500)
    malumot=models.TextField(max_length=5000)

    def strsar(self):
        return self.sarlovha
    
    def strmalumot(self):
        return self.malumot
    
