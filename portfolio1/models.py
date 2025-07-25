from django.db import models

# Create your models here.
from django.db import models

class Project(models.Model):
  

    title = models.CharField(max_length=200)
    
    image = models.ImageField(upload_to='projects/')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    
    

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='project_images/')
    



