from django.db import models
from django.contrib.auth.models import User

class Image(models.Model):
    image_name = models.CharField(max_length=30)
    image = models.ImageField(upload_to = 'posts/')
    image_caption = models.TextField()
    image_poster = models.ForeignKey(User, on_delete=models.CASCADE, default = '', null = True)



    @classmethod
    def all_images(cls):
        all_posts = cls.objects.all()
        # print(all_posts)
        return all_posts

    def save_images(self):
        self.save()

    def delete_all_image(self):
        self.delete()

    
    def __str__(self):
        return self.image_name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image =models.ImageField(default='default.jpg', upload_to='post')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save_prof(self):
        self.save()

    def delete_prof(self):
        self.delete()
# Create your models here.
