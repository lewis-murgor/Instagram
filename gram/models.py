from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.

LIKE_CHOICE = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
)

class Profile(models.Model):
    profile_photo = models.ImageField(upload_to = 'images/')
    Bio = models.TextField()
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.Bio

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def update_profile(self, updated_profile):
        self.profile = updated_profile
        self.save()

class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    name = models.CharField(max_length =60)
    caption = HTMLField()
    date = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    likes = models.ManyToManyField(User,blank=True,related_name='likes')
    comments = models.TextField()

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_caption(self, updated_caption):
        self.caption = updated_caption
        self.save

    @classmethod
    def search_by_name(cls,name):
        image = cls.objects.filter(name__icontains=name)
        return image

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICE,default='Like',max_length=10)

    def __str__(self):
        return self.image

class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ForeignKey(Image,on_delete=models.CASCADE)
    comment = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image

