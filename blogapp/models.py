from django.db import models

# Create your models here.

class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(blank=False,null=False,max_length=250)
    content = models.TextField()
    publishedDate= models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    