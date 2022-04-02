from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class Profile(models.Model):
    profile_photo = models.ImageField(upload_to = 'images/')
    Bio = models.TextField()

class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    name = models.CharField(max_length =60)
    caption = HTMLField()
    date = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(User,on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    comments = models.TextField()

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

class Like(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ForeignKey(Image,on_delete=models.CASCADE)

class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ForeignKey(Image,on_delete=models.CASCADE)

