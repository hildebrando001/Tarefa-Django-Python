from django.db import models
from django.contrib.auth import get_user_model

class Task(models.Model):

    STATUS = (
        ('novo', 'novo'),
        ('fazendo', 'fazendo'),
        ('feito', 'feito'),
    )

    title = models.CharField('título', max_length=255)
    description = models.TextField('descrição')
    done = models.CharField(max_length=7, choices=STATUS)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField('data de criação', auto_now_add=True)
    updated_at = models.DateTimeField('data de atualização', auto_now=True)


    def __str__(self):
        return self.title
        
    