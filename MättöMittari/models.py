from django.db import models
from django.contrib.auth.models import User

class Ruoka(models.Model):
    text = models.CharField(max_length=100)
    ainekset = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.text
    
class Arvio(models.Model):
    ruoka = models.ForeignKey(Ruoka, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'arviot'

        def __str__(self):
            return f"{self.text[:50]}..."