from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tag(models.Model):
    name=models.CharField(max_length=30, null=False, blank=False)

    def __str__(self):
        return self.name

class Post(models.Model):
    objname = models.CharField(max_length=50)
    name = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    objdetail = models.TextField()
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to="post/", blank=True, null=True)
    tags = models.ManyToManyField(Tag, related_name='posts', blank=True)
    like = models.ManyToManyField(User, related_name='likes', blank=True)
    like_count = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.objname
    
    def summary(self):
        return self.objdetail[:20]
    
class Comment(models.Model):
    comment_content = models.TextField()
    comment_date = models.DateTimeField()
    comment_writer = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.post.objname + ":" + self.comment_content[:20] + "by" + self.comment_writer.id
    