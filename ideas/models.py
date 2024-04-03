from django.db import models

class Idea(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, default='')
    content = models.TextField()
    
    class Meta:
        ordering = ['created']