from django.db import models

# Create your models here.
class Profile(models.Model):
    profile_photo = models.ImageField(upload_to = 'images/')
    Bio = models.TextField()

class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    name = models.CharField(max_length =60)
    caption = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    likes = models.IntegerField()
    comments = models.TextField()

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

