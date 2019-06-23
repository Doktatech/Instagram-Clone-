from django.contrib.auth.models import User
from django.db import models
import datetime as dt



# Create your models here.
class caption(models.Model):
    name =models.CharField(max_length=30)
class Profile(models.Model):
    profile_photo = models.ImageField(upload_to = 'profiles/', null=True)
    user_bio = models.TextField()
    user = models.ForeignKey(User)
    last_update = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering =['-last_update']

    def __str__(self):
        return self.user.username

    def save_profile(self):
        self.save()
    
class Photo(models.Model):
    pub_date = models.DateTimeField(auto_now_add=True)
    photo_name =models.CharField(max_length=30, null=True)
    photo = models.ImageField(upload_to='photos/',blank=True)
    user =models.ForeignKey(User,on_delete=models.CASCADE)
    caption = models.ManyToManyField(caption)
    likes = models.IntegerField(default=0,null=True )
    profile = models.ForeignKey(Profile, null=True)
    
    @classmethod
    def photos_newest(cls):
        today = dt.date.today()
        photos = cls.objects.filter(pub_date__date=today)
        return photos
    @classmethod
    def photo_today(cls,date):
        photos = cls.objects.filter(pub_date__date=date)
        return photos











