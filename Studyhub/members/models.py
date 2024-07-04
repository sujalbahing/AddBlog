from django.db import models

 
class Blog(models.Model):
    Title = models.CharField(max_length=100, verbose_name="Title")
    Subtitle = models.CharField(max_length=100, verbose_name="Subtitle")
    Image = models.ImageField(upload_to='images/', blank=True)
    Description = models.TextField(max_length=100, verbose_name="Description")
    
    def __str__(self):
        return str(self.id)
    
    
    

