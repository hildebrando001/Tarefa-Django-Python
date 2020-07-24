from django.db import models

class Task(models.Model):

    STATUS = (
        ('novo', 'novo'),
        ('fazendo', 'fazendo'),
        ('feito', 'feito'),
    )

    title = models.CharField(max_length=255)
    description = models.TextField()
    done = models.CharField(max_length=7, choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
        
    