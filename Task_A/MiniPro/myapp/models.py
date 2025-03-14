from django.db import models

# Create your models here.
class Info(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    sport=models.CharField(max_length=100)
    file=models.ImageField(upload_to='media/user_files')
    
    def __str__(self):
        return self.id+"  "+self.name