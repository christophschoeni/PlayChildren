from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.title}'
    
class Learn (models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f'{self.title}'