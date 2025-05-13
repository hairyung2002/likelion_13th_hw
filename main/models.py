from django.db import models

# Create your models here.
class Post(models.Model):
    objname = models.CharField(max_length=50)
    name = models.CharField(max_length=30)
    objdetail = models.TextField()
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to="post/", blank=True, null=True)

    def __str__(self):
        return self.objname
    
    def summary(self):
        return self.objdetail[:20]